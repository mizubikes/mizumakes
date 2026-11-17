#!/usr/bin/env python3
"""
Daily 3D printing deal finder for mizumakes.com/3d-printer-deals/

Reads   data/deal_stores.yaml     (the store list + thresholds you edit)
Writes  data/deals.json           (today's deals, grouped by category)
        static/deals-all.json     (every deal found, for the page's search box)
        data/deal_history.json    (first-seen date + lowest price per deal)

Most stores are Shopify shops: the script pages through the public
/products.json catalog. Bambu Lab (type: jsonld) is read from its public
product pages, which list each variant's sale price and strikethrough price
in their schema.org data. It keeps new, in-stock items marked down from the
store's own list price (refurbished and open-box are left out), sorts them
into categories, and ranks them. Each row can carry an Amazon search link with your Associates
tag; Amazon prices are never fetched or shown.

Run locally:   python scripts/deal_finder.py
Dry run:       python scripts/deal_finder.py --dry-run   (prints, writes nothing)
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import os
import pathlib
import re
import sys
import time
import urllib.parse
from zoneinfo import ZoneInfo

import requests
import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
STORES = ROOT / "data" / "deal_stores.yaml"
DEALS = ROOT / "data" / "deals.json"
HISTORY = ROOT / "data" / "deal_history.json"
ALL = ROOT / "static" / "deals-all.json"    # every deal, for the page's search box

TIMEOUT = 30
PAGE_SIZE = 250                 # Shopify's maximum for products.json
HISTORY_KEEP_DAYS = 45          # forget deals not seen for this long
ENDED_DAYS = 7                  # "Recently ended" shows deals that left in the last week
ENDED_MAX = 30                  # ...and at most this many
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; MizuMakesPriceBot/1.0; "
                  "+https://mizumakes.com/3d-printer-deals/)",
    "Accept": "application/json",
}

DEFAULTS = {
    "min_discount": 0.20,       # at least 20% under the store's list price
    "max_discount": 0.80,       # above this the "list price" is usually bogus
    "min_price": 12.0,          # skip tiny spares (single filament spools start around $13)
    "per_category": 25,         # rows per category on the main deals page
    "per_category_page": 120,   # deals listed on each category's own page
    "per_store_per_category": 8,  # stop one store from filling a category
    "top_count": 10,            # rows in "Best deals today"
    "max_pages": 100,           # 100 x 250 = 25,000 products per store
    "delay_seconds": 1.0,       # pause between requests to the same store
    "site_brands_only": True,   # only brands the site's own articles mention
    "brand_min_mentions": 2,    # how many times a brand must appear in the articles
    "brands_allow": [],         # always include these brands
    "brands_block": [],         # never include these brands
    "brands_boost": [],         # favorite brands, ranked higher
    "max_age_years": 2,         # skip items whose model year is older than this
    # not every deal has to be 20% off
    "rare_min_discount": 0.10,  # brands/parts that rarely go on sale count from here
    "rare_sale_rate": 0.05,     # a brand is "rarely on sale" when under 5% of its products are discounted
    "rare_sale_brands": [],     # always treated as rarely on sale
    "rare_sale_min_products": 25,  # ...measured over at least this many products
    "big_save_min_discount": 0.12,
    "big_save_min": 150,        # ...or at least $150 off, at 12%+ off
    "popular_terms": [],        # current-generation parts: ranked higher, count from rare_min_discount
    "older_gen_terms": [],      # previous generations: left off the main lists
    "wanted_terms": [],         # product lines people buy; the main lists need a match (see keep_main)
    "amazon_tag": "",           # Amazon Associates tag; empty = no Amazon buttons
    "amazon_skip": ["printers"],             # categories Amazon links aren't wanted for
    "jsonld_max_products": 400, # product pages read per jsonld store per run
}

# Display order on the page. Keys are used as anchors.
CATEGORIES = [
    ("printers", "3D printers"),
    ("filament", "Filament"),
    ("resin", "Resin"),
    ("upgrades", "Nozzles, hotends and upgrades"),
    ("accessories", "Dryers, tools and accessories"),
    ("lasers", "Lasers and engravers"),
]

USED = re.compile(r"refurb|renewed|pre-?owned|\bused\b|open[ -]?box|b-?stock|\bdemo\b|"
                  r"blemish|\bblem\b|cosmetic(ally)? (damage|flaw)|scratch (and|&) dent|"
                  r"returned|second ?hand", re.I)

SKIP = re.compile(r"gift ?card|e-?gift|warranty|protection plan|shipping protection|"
                  r"route package|donation|service fee|deposit|insurance|"
                  r"membership|subscription|free gift|\bgift\b(?! box)|"
                  r"sample|swatch|test product", re.I)

# Printer families: a product named after one of these (and priced like a
# printer) is a 3D printer, unless the title says it is a part for one.
PRINTER_MODEL = re.compile(
    r"\b3d printer\b|\bresin printer\b|"
    r"\b(a1|a1 mini|a2|p1s|p1p|p2s|x1c|x1e|x1 carbon|x2d|h2d|h2s|h2c|h3c)\b|"
    r"\bcentauri\b|\bneptune\b|\bsaturn\b|\bmars \d|\bjupiter\b|"
    r"\bkobra\b|\bphoton\b|\bhalot\b|\bender[ -]?\d|\bk1\b|\bk1c\b|\bk1 max\b|\bk2\b|\bk3\b|"
    r"\bsparkx\b|\bhi combo\b|\badventurer\b|\bad5[xm]\b|\bcreator (5|4|3|pro)|\bguider\b|"
    r"\bq1 pro\b|\bq2\b|\bplus ?4\b|\bmax ?4\b|\bx-?max ?3\b|\bx-?plus ?3\b|"
    r"\bsv0[5-9]\b|\bsnapmaker (u1|j1|artisan|a350|a250|2\.0)\b|\bu1\b|"
    r"\bcore one\b|\bmk4s?\b", re.I)
PART_FOR = re.compile(
    r"\b(nozzles?|hot ?ends?|hotend|extruder|plates?|sheets?|bed|pei|fans?|boards?|mainboard|"
    r"motherboard|belts?|motors?|screens?|display|cable|wires?|harness|heater|thermistor|"
    r"cutter|blade|wiper|ptfe|tube|fitting|lid|cover|door|panel|enclosure|cabinet|"
    r"parts?|spare|replacement|kit|upgrade|module|toolhead|tool head|vat|tank|fep|film|"
    r"filament|resin|spool|dryer|camera|lamp|light|filter|purifier|stand|table|"
    r"bracket|mount|holder|knob|screw|bearing|rod|rail|carriage|sensor|probe|"
    r"ams|cfs|ace|buffer|hub|switch|power supply|psu|accessor\w*)\b", re.I)

# First match wins. Checked against "product_type | title", then tags.
RULES = [
    ("lasers", re.compile(r"laser engrav|laser cutt|\bengraver\b|\blaser\b(?!.*\b(printer|filament)\b)|"
                          r"\bco2\b|\bfiber laser\b|\bdiode\b|rotary attach")),
    ("resin", re.compile(r"\bresin\b(?!.*\b(printer|vat|tank|fep|film|washer|curing|cure)\b)|"
                         r"\bphotopolymer\b|\b(abs|water)[ -]?like\b")),
    ("accessories", re.compile(r"dryer|dry ?box|drybox|filament (storage|holder|rack)|spool holder|"
                               r"storage|\btools?\b|tool kit|toolkit|scraper|deburr|glue|"
                               r"\bstands?\b|\btables?\b|cabinet|enclosure|purifier|air filter|"
                               r"wash (and|&) cure|washer|curing|\bcure\b|\bcamera\b|\blamps?\b|"
                               r"\blights?\b|cleaning|\bbag\b|\bcase\b|\bgloves?\b|\bmat\b")),
    ("filament", re.compile(r"filament|\bpla\b|\bpla\+|petg|\bpctg\b|\babs\b|\basa\b|\btpu\b|"
                            r"\bpa6|\bpa12|\bpa-?cf|\bnylon\b|\bpps\b|\bpc\b|\bpet-?cf|"
                            r"\bcarbon fiber\b(?!.*\b(rod|plate|tube)\b)|\bspool\b|\brefill\b|\b\d(\.\d+)? ?kg\b")),
    ("upgrades", re.compile(r"nozzle|hot ?end|hotend|extruder|build plate|print bed|\bbed\b|\bplates?\b|"
                            r"\bpei\b|\bsheets?\b|toolhead|tool head|\bams\b|\bcfs\b|\bace( 2)? pro\b|"
                            r"multi-?colou?r|multi-?material|\bvats?\b|\bfep\b|\bfilm\b|"
                            r"mainboard|motherboard|\bboard\b|stepper|\bmotors?\b|\bfans?\b|\bbelts?\b|"
                            r"upgrade|\bkit\b|cooling|ptfe|\bprobe\b|screen|display|cutter|"
                            r"heater|thermistor|\bmodule\b|\bparts?\b|replacement|spare")),
]

# Words dropped from a store's vendor name before looking for it in the articles
BRAND_FILLER = re.compile(r"\b(3d|printing|printers?|filaments?|technology|tech|official|"
                          r"store|shop|co|company|inc|ltd|usa|us|lab|labs|products?)\b\.?", re.I)
# Brand names that are also everyday words: these must appear capitalized more often
AMBIGUOUS = {"slice", "printed", "solid", "push", "atomic", "fusion", "overture", "elegant",
             "polar", "titan", "dragon", "revo", "hero", "ender", "creator"}


# ---------------------------------------------------------------- helpers

def load_json(path: pathlib.Path, default):
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print(f"WARN: {path.name} is not valid JSON, starting fresh")
    return default


def write_json(path: pathlib.Path, data) -> None:
    path.write_text(json.dumps(data, indent=1, sort_keys=True, ensure_ascii=False) + "\n",
                    encoding="utf-8")


def money(value) -> float | None:
    """products.json gives "129.99" (string dollars); product .js gives cents."""
    if value in (None, "", 0, "0", "0.00"):
        return None
    try:
        if isinstance(value, int):
            return round(value / 100.0, 2)
        return round(float(value), 2)
    except (TypeError, ValueError):
        return None


def get_json(url: str) -> dict:
    for attempt in range(3):
        try:
            r = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
            if r.status_code == 200:
                return r.json()
            if r.status_code in (429, 500, 502, 503, 504):
                time.sleep(8 * (attempt + 1))
                continue
            raise RuntimeError(f"HTTP {r.status_code}")
        except (requests.RequestException, ValueError) as e:
            if attempt == 2:
                raise RuntimeError(type(e).__name__) from e
            time.sleep(8 * (attempt + 1))
    raise RuntimeError("gave up after 3 tries (rate limited or server errors)")


def fetch_catalog(store: dict, cfg: dict) -> list[dict]:
    """All products for a store, de-duplicated across collections."""
    base = store["base"].rstrip("/")
    collections = store.get("collections") or [None]
    max_pages = int(store.get("max_pages", cfg["max_pages"]))
    seen, out = set(), []
    for coll in collections:
        path = f"/collections/{coll}/products.json" if coll else "/products.json"
        for page in range(1, max_pages + 1):
            try:
                data = get_json(f"{base}{path}?limit={PAGE_SIZE}&page={page}")
            except RuntimeError:
                if page == 1:
                    raise
                break       # store stops serving deep pages: keep what we have
            products = data.get("products") or []
            for p in products:
                if p.get("id") not in seen:
                    seen.add(p.get("id"))
                    out.append(p)
            if len(products) < PAGE_SIZE:
                break
            time.sleep(float(cfg["delay_seconds"]))
    return out


# ---------------------------------------------------------------- JSON-LD stores (Bambu Lab)

PAGE_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/131.0 Safari/537.36 MizuMakesPriceBot/1.0",
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "en-US,en;q=0.9",
}
LD_BLOCK = re.compile(r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>', re.S | re.I)
OG_IMAGE = re.compile(r'<meta[^>]+property="og:image"[^>]+content="([^"]+)"', re.I)


def get_html(url: str) -> str:
    for attempt in range(3):
        try:
            r = requests.get(url, headers=PAGE_HEADERS, timeout=TIMEOUT)
            if r.status_code == 200:
                return r.text
            if r.status_code in (429, 500, 502, 503, 504):
                time.sleep(8 * (attempt + 1))
                continue
            raise RuntimeError(f"HTTP {r.status_code}")
        except requests.RequestException as e:
            if attempt == 2:
                raise RuntimeError(type(e).__name__) from e
            time.sleep(8 * (attempt + 1))
    raise RuntimeError("gave up after 3 tries (rate limited or server errors)")


def sitemap_products(base: str) -> list[str]:
    """Product URLs from the store's public sitemap(s)."""
    index = get_html(f"{base}/sitemap.xml")
    maps = [m.replace("&amp;", "&") for m in re.findall(r"<loc>([^<]+)</loc>", index)
            if "sitemap" in m and "product" in m]
    urls = re.findall(r"<loc>([^<]+/products/[^<]+)</loc>", index)
    for m in maps:
        urls += re.findall(r"<loc>([^<]+/products/[^<]+)</loc>", get_html(m))
    return list(dict.fromkeys(u.replace("&amp;", "&") for u in urls))


def ld_offer(o: dict) -> tuple[float | None, float | None, bool]:
    """(price, strikethrough price, in stock) from one schema.org Offer."""
    price = money(str(o.get("price")) if o.get("price") is not None else None)
    was = None
    specs = o.get("priceSpecification") or []
    for sp in specs if isinstance(specs, list) else [specs]:
        if isinstance(sp, dict) and "Strikethrough" in str(sp.get("priceType") or "") \
                and str(sp.get("priceCurrency") or "USD") == "USD":
            was = money(str(sp.get("price")))
    avail = str(o.get("availability") or "")
    return price, was, ("InStock" in avail or "PreOrder" in avail)


def jsonld_product(html: str, url: str) -> dict | None:
    """A product page's schema.org data -> the Shopify-like dict the rest of the
    script expects (one variant per offer)."""
    group = None
    for block in LD_BLOCK.findall(html):
        try:
            data = json.loads(block)
        except ValueError:
            continue
        for d in data if isinstance(data, list) else [data]:
            if isinstance(d, dict) and d.get("@type") in ("ProductGroup", "Product"):
                group = d
                break
        if group:
            break
    if not group:
        return None
    name = (group.get("name") or "").strip()
    variants = []
    for v in group.get("hasVariant") or [group]:
        offers = v.get("offers") or []
        for o in offers if isinstance(offers, list) else [offers]:
            if not isinstance(o, dict):
                continue
            price, was, stock = ld_offer(o)
            vname = (v.get("name") or o.get("name") or "").strip()
            if name and vname.lower().startswith(name.lower()):
                vname = vname[len(name):].strip(" -/")
            vimg = v.get("image")
            variants.append({"id": None, "sku": v.get("sku") or o.get("sku"),
                             "title": vname or "Default Title", "available": stock,
                             "price": f"{price:.2f}" if price else None,
                             "compare_at_price": f"{was:.2f}" if was else None,
                             "image": vimg if isinstance(vimg, str) else ""})
    if not variants:
        return None
    img = group.get("image")
    img = img[0] if isinstance(img, list) and img else img
    if isinstance(img, dict):
        img = img.get("url") or img.get("contentUrl")
    if not isinstance(img, str) or not img:
        img = next((v["image"] for v in variants if v.get("image")), "")
    if not img:
        m = OG_IMAGE.search(html)
        img = m.group(1) if m else ""
    brand = group.get("brand")
    brand = brand.get("name") if isinstance(brand, dict) else (brand or "")
    handle = url.rstrip("/").split("/products/")[-1].split("?")[0]
    return {"id": handle, "handle": handle, "title": name, "vendor": brand,
            "product_type": str(group.get("category") or ""), "tags": [],
            "url_path": "/products/" + handle,
            "images": [{"src": img}] if img else [],
            "options": [],
            "variants": variants}


def fetch_jsonld(store: dict, cfg: dict) -> list[dict]:
    """Products from a store's public product pages, found through its sitemap.
    `include` / `exclude` (regexes on the product URL) keep the run small."""
    base = store["base"].rstrip("/")
    urls = sitemap_products(base)
    inc = re.compile(store["include"], re.I) if store.get("include") else None
    exc = re.compile(store["exclude"], re.I) if store.get("exclude") else None
    urls = [u for u in urls if (not inc or inc.search(u)) and not (exc and exc.search(u))]
    cap = int(store.get("max_products", cfg["jsonld_max_products"]))
    print(f"      {store['id']}: {len(urls)} product pages match in the sitemap; reading {min(len(urls), cap)}")
    out, fails = [], 0
    for u in urls[:cap]:
        try:
            p = jsonld_product(get_html(u), u)
        except RuntimeError:
            fails += 1
            if fails >= 10 and not out:
                raise
            continue
        if p:
            out.append(p)
        time.sleep(float(cfg["delay_seconds"]))
    if not out:
        raise RuntimeError("no product data found on the product pages")
    return out


def categorize(product: dict, price: float) -> str:
    ptype = (product.get("product_type") or "").lower()
    title = (product.get("title") or "").lower()
    tags = product.get("tags") or []
    if isinstance(tags, str):
        tags = tags.split(",")
    text = " | ".join([ptype, title, " ".join(t.strip().lower() for t in tags[:25])])
    head = f"{ptype} | {title}"
    # a printer (or printer combo) is named after its model and priced like one;
    # "Hardened Nozzle for P1S" or "K2 Build Plate" are parts for one
    if price >= 129 and re.search(r"\b(3d|resin|fdm) printers?\b", title) \
            and not re.search(r"\b(for|compatible|fits)\b.*\bprinters?\b|\bparts?\b|\bspare|\bkit\b|"
                              r"\b(enclosure|cabinet|cover|tent|stand|table|dryer|camera|lights?|lamp|mat|"
                              r"tools?|cart|filament|storage|filter|purifier)\b", title):
        return "printers"
    if price >= 129 and not PART_FOR.search(title) and not re.search(r"laser engrav|engraver", title) \
            and (PRINTER_MODEL.search(title) or re.search(r"\b(3d|resin) printers?\b", ptype)):
        return "printers"
    for key, rx in RULES:
        if rx.search(head):
            return key
    for key, rx in RULES:
        if rx.search(text):
            return key
    return "accessories"


def floor_discount(cfg: dict) -> float:
    """Lowest markdown any rule accepts; the final cut happens after every
    store has been read (see keep_deal)."""
    return min(cfg["min_discount"], cfg["rare_min_discount"], cfg["big_save_min_discount"])


def best_variant(product: dict, cfg: dict):
    """In-stock variant with the biggest real markdown, or None."""
    best = None
    for v in product.get("variants") or []:
        if not v.get("available"):
            continue
        price, was = money(v.get("price")), money(v.get("compare_at_price"))
        if not price or not was or was <= price:
            continue
        pct = 1 - price / was
        if price < cfg["min_price"] or not (floor_discount(cfg) <= pct <= cfg["max_discount"]):
            continue
        if best is None or pct > best[2] or (pct == best[2] and price < best[0]):
            best = (price, was, pct, v)
    return best


def link_for(store: dict, url: str) -> tuple[str, bool]:
    """Wrap the product URL in the store's affiliate template, if it has one."""
    tpl = (store.get("affiliate") or "").strip()
    if not tpl:
        return url, False
    return (tpl.replace("{url_encoded}", urllib.parse.quote(url, safe=""))
               .replace("{url}", url)), True


def amazon_link(brand: str, title: str, tag: str) -> str:
    """Amazon search link carrying the Associates tag. Never a price: Amazon
    only allows prices pulled from its own API, so this is a "check it" link."""
    words = re.sub(r"\[[^\]]*\]|\([^)]*\)", " ", title)       # drop [notes] and (notes)
    words = re.sub(r"[^\w\s.\-/+]", " ", words)
    if brand and not words.lower().lstrip().startswith(brand.lower()):
        words = f"{brand} {words}"
    query = " ".join(words.split()[:10])
    return f"https://www.amazon.com/s?k={urllib.parse.quote_plus(query)}&tag={tag}"


# Words too common to count as a model name when matching titles to articles
GENERIC = {"3d", "printer", "printers", "printing", "filament", "pla", "petg", "abs", "asa", "tpu",
           "kg", "1kg", "spool", "spools", "refill", "combo", "black", "white", "grey", "gray",
           "nozzle", "mm", "1", "75", "0", "4", "high", "speed", "new", "pro", "plus", "max", "mini",
           "set", "kit", "with", "and", "for", "the", "matte", "silk", "basic", "multi", "color",
           "colors", "pack", "bundle", "resin", "standard", "edition"}

# Older gear most makers aren't shopping for
DATED = re.compile(r"\b2\.85 ?mm\b|\b3\.0 ?mm\b|\b3 ?mm filament\b|\bbowden kit\b|"
                   r"\bender[ -]?3 (v2|pro|s1)\b|\bender[ -]?5 (pro|plus|s1)\b|\bcr-?10\b|\bcr-?6\b|"
                   r"\bkobra (2|go|neo|max)\b|\bneptune (2|3)\b|\bmars (2|3)\b|\bsaturn (2|s)\b|"
                   r"\bphoton mono (x|se|4k)\b|\badventurer (3|4)\b|\bsnapmaker (2\.0|a250|a350|a150)\b", re.I)
HALF_SET = re.compile(r"(?!x)x")        # never matches: nothing in 3D printing is sold as half a set
# Parts almost nobody is shopping for: left out completely
NOBODY_WANTS = re.compile(r"\bscrews?\b|\bnuts?\b|\bwashers?\b(?! (and|&) cur)|\bthermistor\b|"
                          r"silicone sock|\bwiper\b|limit switch|\bfuse\b|\bknob\b|o-?ring|"
                          r"sticker|decal|\blogo\b|keychain|\bbearings?\b|\bbushings?\b|\bpulley\b|\bidler\b|"
                          r"\bsprings?\b|\bhinge\b|\bfeet\b|\brubber foot\b|\bcables?\b|\bwires?\b|"
                          r"\bharness\b|ribbon|\bshell\b|\bhousing\b|front cover|side cover|"
                          r"\bpanel\b|\bdoor\b|\blid\b|\bfan duct\b|\bfan cover\b|"
                          r"\bmotherboard\b|\bmainboard\b|\bpower supply\b|\bpsu\b|\bscreen\b(?! protector)|"
                          r"\bdisplay\b|\bsensor\b|\bcutter blade\b|\bptfe\b|\bfitting\b|\bcoupler\b", re.I)
# Small spares: listed, but ranked well below real upgrades
SMALL_PARTS = re.compile(r"\b(fans?|sock|wiper|heater|heating block|spare|"
                         r"replacement|scraper|glue|tubes?|nozzle cleaning|"
                         r"vat|fep|release film|filters?|cartridges?)\b", re.I)
MODEL_YEAR = re.compile(r"\b(20[12]\d)\b")

# How much shoppers come looking for each category
CATEGORY_WEIGHT = {"printers": 1.25, "filament": 1.10, "resin": 0.90, "upgrades": 1.05,
                   "accessories": 0.85, "lasers": 0.85}


def words(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", (text or "").lower()))


def term_lists(entries) -> list[list[str]]:
    """"SRAM E1" -> ["sram", "e1"]: an item matches when its brand + title
    contain every word of an entry, in any order. A word ending in * matches
    any word starting with it ("R92*" matches R9200, R9250, R9270)."""
    out = []
    for e in entries or []:
        toks = re.findall(r"[a-z0-9]+\*?", str(e).lower())
        if toks:
            out.append(toks)
    return out


def matches(item_words: set[str], terms: list[list[str]]) -> bool:
    for toks in terms:
        if all((any(w.startswith(t[:-1]) for w in item_words) if t.endswith("*") else t in item_words)
               for t in toks):
            return True
    return False


def relevance(item: dict, n_available: int, brands: "SiteBrands", this_year: int) -> float:
    """Rank by how likely a reader is to want it, not by discount alone."""
    pct, price, title = item["pct"], item["price"], item["title"]
    # discount: full credit up to 45% off, little extra beyond, and a penalty
    # past 60% where the list price is usually inflated or the item is obsolete.
    # Gear that rarely goes on sale gets double credit: 12% off Slice Engineering is news.
    d = pct if pct <= 0.45 else 0.45 + (pct - 0.45) * 0.2
    if item.get("rare") or item.get("popular"):
        d = max(d, min(pct * 2, 0.45))
    if pct > 0.60:
        d -= (pct - 0.60) * 0.8
    s = d * (1 + math.log10(min(max(price, 10), 3000)) / 2)
    s *= brands.weight(item["brand"])                       # brands the site covers most
    s *= 1 + 0.15 * brands.topic_hits(item["brand"], title)  # models the site writes about
    s *= 1 + 0.05 * min(max(n_available - 1, 0), 3)          # several colors/options still in stock
    s *= CATEGORY_WEIGHT.get(item["category"], 1.0)
    if item.get("popular"):
        s *= 1.35                                           # current generation people are shopping for
    elif item.get("older_gen"):
        s *= 0.7                                            # previous generation
    if SMALL_PARTS.search(title):
        s *= 0.35
    if HALF_SET.search(title):
        s *= 0.8
    years = [int(y) for y in MODEL_YEAR.findall(title)]
    if years and max(years) <= this_year - 2:    # still allowed, but not current
        s *= 0.85
    return round(s, 4)


class SiteBrands:
    """Answers "does the site write about this brand?" from the article text."""

    def __init__(self, cfg: dict):
        self.on = bool(cfg.get("site_brands_only"))
        self.min = int(cfg.get("brand_min_mentions", 2))
        self.allow = {self.norm(b) for b in cfg.get("brands_allow") or []}
        self.block = {self.norm(b) for b in cfg.get("brands_block") or []}
        self.boost = {self.norm(b) for b in cfg.get("brands_boost") or []}
        self.cache: dict[str, bool] = {}
        self.mentions: dict[str, int] = {}
        self.topic_cache: dict[str, bool] = {}
        self.text = ""
        self.lower = ""
        if True:    # article text is also used for ranking, even with the filter off
            parts = []
            for f in sorted((ROOT / "content" / "posts").rglob("*.md")):
                try:
                    parts.append(f.read_text(encoding="utf-8", errors="ignore"))
                except OSError:
                    pass
            self.text = "\n".join(parts)
            self.lower = self.text.lower()
        if not self.text:               # no articles found: don't filter everything out
            self.on = False

    @staticmethod
    def norm(name: str) -> str:
        return " ".join(BRAND_FILLER.sub(" ", name or "").split()).lower().strip(" -.&")

    @staticmethod
    def listed(key: str, names: set) -> bool:
        """Exact match, match ignoring spaces/hyphens ("raceface" = "race face"),
        or the vendor starts with a listed name ("wahoo fitness" = "wahoo")."""
        squash = key.replace(" ", "").replace("-", "")
        return any(key == n or squash == n.replace(" ", "").replace("-", "")
                   or key.startswith(n + " ") for n in names if n)

    def ok(self, vendor: str) -> bool:
        key = self.norm(vendor)
        if key in self.cache:
            return self.cache[key]
        if not self.on:
            self.cache[key] = True
            self.mentions[key] = self.count(key)
            return True
        if self.listed(key, self.block) or len(key) < 2:
            res = False
        elif self.listed(key, self.allow):
            res = True
        else:
            # brand name as written in an article: must start with a capital letter
            hits = self.count(key)
            res = hits >= (max(self.min, 5) if key in AMBIGUOUS else self.min)
        self.cache[key] = res
        self.mentions.setdefault(key, self.count(key) if res else 0)
        return res

    def count(self, key: str) -> int:
        """Times the brand appears in the articles, written with a capital letter."""
        if not self.text or len(key) < 2:
            return 0
        rx = re.compile(r"(?<![\w-])" + re.escape(key).replace(r"\ ", r"[\s-]?") + r"(?![\w])", re.I)
        return sum(1 for m in rx.finditer(self.text) if m.group(0)[:1].isupper())

    def weight(self, vendor: str) -> float:
        """1.0 for a brand the site never mentions, up to 1.5 for its most-covered brands."""
        key = self.norm(vendor)
        if self.listed(key, self.boost):
            return 1.5
        n = self.mentions.get(key, 0)
        return 1 + min(math.log10(1 + n), 2.0) / 4

    def topic_hits(self, brand: str, title: str) -> int:
        """How many two-word model names from the title the articles also use
        (e.g. "GX Eagle", "SES 3.4"). Capped at 2."""
        words = re.findall(r"[a-z0-9][a-z0-9.\-]*", title.lower())
        skip = set(self.norm(brand).split())
        words = [w for w in words if w not in skip]
        hits = 0
        for a, b in zip(words, words[1:]):
            if len(a) < 2 or len(b) < 2 or (a.isdigit() and b.isdigit()) or a in GENERIC or b in GENERIC:
                continue
            pair = f"{a} {b}"
            if pair not in self.topic_cache:
                self.topic_cache[pair] = pair in self.lower
            if self.topic_cache[pair]:
                hits += 1
                if hits >= 2:
                    break
        return hits


def image_for(product: dict, width: int = 400) -> str:
    """First product photo, sized down when it comes from Shopify's image CDN."""
    imgs = product.get("images") or []
    src = (imgs[0].get("src") if imgs and isinstance(imgs[0], dict) else "") or ""
    if not src.startswith("http"):
        return ""
    if "cdn.shopify.com" in src or "/cdn/shop/" in src:
        src += ("&" if "?" in src else "?") + f"width={width}"
    return src


SIZE_OPTION = re.compile(r"colou?r", re.I)      # filament colors in stock at the deal price


def sizes_on_sale(product: dict, cfg: dict) -> list[str]:
    """Colors still in stock at a deal price, in the store's own order.
    Empty when the product has no color option (or only one color exists)."""
    opts = product.get("options") or []
    pos = None
    for i, o in enumerate(opts):
        name = o.get("name") if isinstance(o, dict) else str(o)
        if name and SIZE_OPTION.search(name):
            pos = (o.get("position") if isinstance(o, dict) else None) or i + 1
            order = [str(v) for v in (o.get("values") or [])] if isinstance(o, dict) else []
            break
    if pos is None:
        return []
    all_sizes, live = [], []
    for v in product.get("variants") or []:
        size = str(v.get(f"option{pos}") or "").strip()
        if not size:
            continue
        if size not in all_sizes:
            all_sizes.append(size)
        price, was = money(v.get("price")), money(v.get("compare_at_price"))
        if v.get("available") and price and was and was > price \
                and 1 - price / was >= cfg["min_discount"] and size not in live:
            live.append(size)
    if len(all_sizes) < 2:
        return []                       # one-size product: nothing useful to show
    rank = {s: i for i, s in enumerate(order or all_sizes)}
    return sorted(live, key=lambda s: rank.get(s, 999))


KEEP_CAPS = {"PLA", "PETG", "ABS", "ASA", "TPU", "PA", "PC", "CF", "GF", "HF", "AMS", "CFS", "ACE",
             "PEI", "PTFE", "UV", "LCD", "MSLA", "FDM", "SLA", "USB", "HT", "QIDI", "BIQU", "E3D", "PRO"}


def tidy_brand(brand: str) -> str:
    """SPECIALIZED -> Specialized, ROCKSHOX -> RockShox stays as the store wrote
    it only when it is a real acronym."""
    if not brand or not brand.isupper() or len(brand) <= 3:
        return brand
    fixed = {"ELEGOO": "Elegoo", "ANYCUBIC": "Anycubic", "SUNLU": "Sunlu", "HATCHBOX": "Hatchbox",
             "OVERTURE": "Overture", "FLASHFORGE": "Flashforge", "BIGTREETECH": "BigTreeTech",
             "XTOOL": "xTool", "CREALITY": "Creality", "SOVOL": "Sovol", "QIDI": "Qidi"}
    if brand in fixed:
        return fixed[brand]
    return " ".join(w if w in KEEP_CAPS else w.capitalize() for w in brand.split())


def display_name(brand: str, title: str) -> str:
    """Card title without the repeated brand or a leading model year, so the
    model name is what shows first: "2026 Specialized S-Works Crux Frameset"
    under brand Specialized becomes "S-Works Crux Frameset (2026)"."""
    t = re.sub(r"^\s*(\[[^\]]*\]\s*)+", "", title or "").strip()
    year = ""
    m = re.match(r"(20[12]\d)\s+(.*)", t)
    if m:
        year, t = m.group(1), m.group(2)
    for cut in filter(None, [brand, (brand or "").split()[0] if brand else ""]):
        if len(cut) >= 2 and t.lower().startswith(cut.lower() + " "):
            t = t[len(cut):].lstrip(" -:")
            break
    if not year:                                  # brand first, then the year
        m = re.match(r"(20[12]\d)\s+(.*)", t)
        if m:
            year, t = m.group(1), m.group(2)
    t = t.strip() or title
    if year and year not in t:
        t = f"{t} ({year})"
    return t


def family(item: dict) -> str:
    """Store + brand + first two words of the model, so "URS 01 ONE" and
    "URS 01 TWO" count as one family and don't stack up in a list."""
    brand = (item.get("brand") or "").lower()
    title = (item.get("title") or "").lower()
    if brand and title.startswith(brand):
        title = title[len(brand):]
    words = [w for w in re.findall(r"[a-z0-9]+", title) if not re.fullmatch(r"20[12]\d", w)]
    return f"{item.get('store')}|{brand}|{' '.join(words[:2])}"


def score(item: dict) -> float:
    """Relevance score set in scan_store (rows carried over from an older run fall back)."""
    return item.get("score") or item["pct"] * (1 + math.log10(max(item["price"], 10)) / 2) * 0.5


def scan_store(store: dict, cfg: dict, brands: "SiteBrands", seen: dict) -> tuple[list[dict], int]:
    base = store["base"].rstrip("/")
    products = fetch_jsonld(store, cfg) if store.get("type") == "jsonld" \
        else fetch_catalog(store, cfg)
    this_year = dt.date.today().year
    deals = []
    for p in products:
        title = (p.get("title") or "").strip()
        label = f"{title} {p.get('product_type') or ''}"
        if not title or SKIP.search(label) or USED.search(label):
            continue        # new gear only: used, demo and pre-owned are left out
        vkey = SiteBrands.norm((p.get("vendor") or "").strip())
        if vkey:                                     # how often does this brand go on sale?
            st = seen.setdefault(vkey, [0, 0])
            st[0] += 1
            if any((money(x.get("compare_at_price")) or 0) > (money(x.get("price")) or 0) > 0
                   for x in p.get("variants") or []):
                st[1] += 1
        hit = best_variant(p, cfg)
        if not hit:
            continue
        if store.get("brand") or not (p.get("vendor") or "").strip():
            p["vendor"] = store.get("brand") or store["name"]   # one-brand store: its own name
        if not brands.ok((p.get("vendor") or "").strip() or store["name"]):
            continue        # brand the site doesn't write about
        # old standards, old model years and parts nobody shops for stay
        # searchable but never appear in the main lists
        years = [int(y) for y in MODEL_YEAR.findall(title)]
        on_main = not (DATED.search(title) or NOBODY_WANTS.search(title)
                       or (years and max(years) < this_year - int(cfg["max_age_years"])))
        price, was, pct, v = hit
        n_avail = sum(1 for x in p.get("variants") or []
                      if x.get("available") and (money(x.get("compare_at_price")) or 0)
                      > (money(x.get("price")) or 0) > 0)
        if p.get("url_path"):
            url = f"{base}{p['url_path']}"
        else:
            url = f"{base}/products/{p.get('handle')}"
            if v.get("id"):
                url += f"?variant={v['id']}"
        href, sponsored = link_for(store, url)
        vtitle = (v.get("title") or "").strip()
        brand = (p.get("vendor") or "").strip()
        if brand and title.lower().startswith(brand.lower()):
            brand = title[:len(brand)]      # use the title's spelling, e.g. SPECIALIZED -> Specialized
        elif brand and len(brand.split()[0]) >= 3 and \
                title.lower().startswith(brand.split()[0].lower() + " "):
            brand = title[:len(brand.split()[0])]   # "Bambu Lab" + "Bambu PLA" -> "Bambu"
        brand = tidy_brand(brand)
        category = categorize(p, price)
        tag = (cfg.get("amazon_tag") or "").strip()
        deals.append({
            "key": f"{store['id']}:{p.get('id')}",
            "store": store["id"],
            "store_name": store["name"],
            "title": title,
            "name": display_name(brand, title),
            "brand": brand,
            "variant": "" if vtitle.lower() == "default title" else vtitle,
            "price": price,
            "was": was,
            "pct": round(pct, 3),
            "save": round(was - price, 2),
            "category": category,
            "amazon": amazon_link(brand, title, tag)
                      if tag and category not in (cfg.get("amazon_skip") or []) else "",
            "url": href,
            "sponsored": sponsored,
            "image": image_for(p),
            "sizes": sizes_on_sale(p, {**cfg, "min_discount": floor_discount(cfg)}),
            "vendor_key": vkey,
            "stock": n_avail,
            "stale": False,
            "main": on_main,
        })
        deals[-1]["score"] = relevance(deals[-1], n_avail, brands, this_year)
    return deals, len(products)


def pick(pool: list[dict], limit: int, per_store: int, per_category: int | None = None,
         per_family: int = 1):
    """Top `limit` by score, capped per store, per category and per model
    family so one shop, category or product line can't dominate."""
    out, by_store, by_cat, by_fam = [], {}, {}, {}
    for it in sorted(pool, key=score, reverse=True):
        fam = family(it)
        if by_store.get(it["store"], 0) >= per_store:
            continue
        if per_category is not None and by_cat.get(it["category"], 0) >= per_category:
            continue
        if by_fam.get(fam, 0) >= per_family:
            continue
        out.append(it)
        by_store[it["store"]] = by_store.get(it["store"], 0) + 1
        by_cat[it["category"]] = by_cat.get(it["category"], 0) + 1
        by_fam[fam] = by_fam.get(fam, 0) + 1
        if len(out) >= limit:
            break
    return out


# ---------------------------------------------------------------- main

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="print results, write nothing")
    ap.add_argument("--only", help="scan just these store ids (comma-separated), for testing")
    args = ap.parse_args()

    raw = yaml.safe_load(STORES.read_text(encoding="utf-8")) or {}
    cfg = {**DEFAULTS, **(raw.get("settings") or {})}
    # stores flagged `used: true` sell mostly second-hand gear and are skipped
    stores = [s for s in raw.get("stores", [])
              if s.get("enabled", True) and not s.get("used")]
    if args.only:
        wanted = {x.strip() for x in args.only.split(",")}
        stores = [s for s in raw.get("stores", []) if s["id"] in wanted]

    brands = SiteBrands(cfg)
    old = load_json(DEALS, {})
    history = load_json(HISTORY, {})
    first_run = not history

    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
    today = now.astimezone(ZoneInfo("America/Los_Angeles")).date()
    today_s = today.isoformat()

    old_items = [it for c in old.get("categories", []) for it in c.get("items", [])
                 if not USED.search(it.get("title", "")) and brands.ok(it.get("brand", ""))
                 and not DATED.search(it.get("title", ""))
                 and not NOBODY_WANTS.search(it.get("title", ""))]
    pool, status, ok_count = [], [], 0
    seen: dict[str, list[int]] = {}          # brand -> [products, products on sale]

    for s in stores:
        rec = {"id": s["id"], "name": s["name"], "home": s["base"].rstrip("/")}
        try:
            deals, scanned = scan_store(s, cfg, brands, seen)
            pool.extend(deals)
            rec.update({"ok": True, "scanned": scanned, "deals": len(deals)})
            ok_count += 1
            print(f"OK    {s['id']:24s} {scanned:6d} products  {len(deals):5d} deals")
        except Exception as e:  # keep yesterday's rows for this store, flagged stale
            # keep yesterday's rows while a store is briefly down, but not for
            # more than two days (e.g. a sale page that has been taken down)
            stale_cutoff = (today - dt.timedelta(days=2)).isoformat()
            carried = [dict(it, stale=True) for it in old_items if it.get("store") == s["id"]
                       and history.get(it.get("key"), {}).get("last", "") >= stale_cutoff]
            pool.extend(carried)
            rec.update({"ok": False, "error": str(e)[:200], "deals": len(carried)})
            print(f"FAIL  {s['id']:24s} {e}  (kept {len(carried)} from last run)")
        status.append(rec)

    if ok_count == 0:
        print("No store could be scanned — leaving yesterday's data in place.")
        return 1

    # ---- which deals make the cut ----
    # 20%+ off as before, OR 10%+ off gear that rarely goes on sale (brands
    # that discount under 8% of their catalog, the rare_sale_brands list, or
    # current-generation parts on popular_terms), OR 12%+ off with $400+ saved.
    rare_brands = {SiteBrands.norm(b) for b in cfg.get("rare_sale_brands") or []}
    for k, (n, on_sale) in seen.items():
        if n >= int(cfg["rare_sale_min_products"]) and on_sale / n < float(cfg["rare_sale_rate"]):
            rare_brands.add(k)
    popular, older = term_lists(cfg.get("popular_terms")), term_lists(cfg.get("older_gen_terms"))
    wanted = term_lists(cfg.get("wanted_terms"))
    this_year = today.year
    kept = []
    for it in pool:
        if it.get("stale"):
            kept.append(it)
            continue
        w = words(f"{it.get('brand', '')} {it['title']}")
        bkey = it.get("vendor_key") or SiteBrands.norm(it.get("brand", ""))
        it["rare"] = bkey in rare_brands or SiteBrands.listed(bkey, rare_brands)
        it["popular"] = matches(w, popular)
        it["older_gen"] = not it["popular"] and matches(w, older)
        pct = it["pct"]
        ok = (pct >= cfg["min_discount"]
              or ((it["rare"] or it["popular"]) and pct >= cfg["rare_min_discount"])
              or (pct >= cfg["big_save_min_discount"] and it["save"] >= float(cfg["big_save_min"])))
        if ok:
            it["score"] = relevance(it, int(it.get("stock") or 1), brands, this_year)
            # main lists and homepage: only gear with a reason to be there.
            # Everything else stays in search.
            years = [int(y) for y in MODEL_YEAR.findall(it["title"])]
            current_printer = it["category"] == "printers" and \
                (not years or max(years) >= this_year - 1)
            reason = it["popular"] or it["rare"] or matches(w, wanted) or current_printer
            it["main"] = bool(it.get("main", True) and not it["older_gen"] and reason)
            kept.append(it)
    print(f"Main lists: {sum(1 for i in kept if i.get('main'))} of {len(kept)} deals qualify "
          f"(current gen, wanted lines, rarely-on-sale brands, current printers)")
    print(f"Deal cut: {len(kept)} of {len(pool)} candidates kept; "
          f"{sum(1 for i in kept if i.get('rare'))} rarely-on-sale, "
          f"{sum(1 for i in kept if i.get('popular'))} current-gen, "
          f"{sum(1 for i in kept if i.get('pct', 1) < cfg['min_discount'])} under {cfg['min_discount']:.0%} off")
    print("Rarely-on-sale brands: " + ", ".join(sorted(b for b in rare_brands if b in seen)[:80]))
    pool = kept

    # history: first-seen date and lowest price per deal
    for it in pool:
        h = history.get(it["key"])
        if h is None:
            # deals found on the very first run are a baseline, not "new today"
            h = history[it["key"]] = {"first": today_s, "last": today_s, "low": it["price"]}
            if first_run:
                h["seed"] = True
            it["lower"] = False
        else:
            it["lower"] = it["price"] < h["low"] - 0.005
            h["low"] = min(h["low"], it["price"])
            h["last"] = today_s
        it["new"] = h["first"] == today_s and not h.get("seed")
        it["since"] = history[it["key"]]["first"]
    cutoff = (today - dt.timedelta(days=HISTORY_KEEP_DAYS)).isoformat()
    history = {k: v for k, v in history.items() if v["last"] >= cutoff}

    main_pool = [it for it in pool if it.get("main", True)]
    categories = []
    for key, title in CATEGORIES:
        cand = [it for it in main_pool if it["category"] == key]
        # first per_category: the balanced top picks the main page shows;
        # then the rest, up to per_category_page, for the category's own page
        rows = pick(cand, int(cfg["per_category"]), int(cfg["per_store_per_category"]))
        chosen = {it["key"] for it in rows}
        more_n = max(int(cfg["per_category_page"]) - len(rows), 0)
        rows += pick([it for it in cand if it["key"] not in chosen], more_n,
                     max(int(cfg["per_category_page"]) // 3, 1))
        if rows:
            categories.append({"key": key, "title": title, "items": rows,
                               "main_total": len(cand),
                               "total": sum(1 for it in pool if it["category"] == key)})

    shown = [it for c in categories for it in c["items"][:int(cfg["per_category"])]]

    # remember what each listed deal looked like, so it can be shown as
    # "recently ended" once it drops out of the scan
    for it in shown:
        history[it["key"]]["info"] = {
            "title": it.get("name") or it["title"], "brand": it["brand"], "variant": it["variant"],
            "store": it["store"], "store_name": it["store_name"], "category": it["category"],
            "price": it["price"], "was": it["was"], "pct": it["pct"], "url": it["url"],
            "sponsored": it.get("sponsored", False),
        }
    live = {it["key"] for it in pool}
    ok_stores = {r["id"] for r in status if r["ok"]}
    ended_cutoff = (today - dt.timedelta(days=ENDED_DAYS)).isoformat()
    ended = []
    for key, h in history.items():
        info = h.get("info")
        if not info or key in live:
            continue
        if h["last"] < ended_cutoff:
            del h["info"]               # too long ago: stop carrying the details
            continue
        # only call it ended if its store was actually scanned today
        if h["last"] < today_s and info["store"] in ok_stores:
            ended.append({**info, "last_seen": h["last"], "since": h["first"]})
    ended.sort(key=lambda e: (e["last_seen"], e["pct"]), reverse=True)
    ended = ended[:ENDED_MAX]
    top = pick(shown, int(cfg["top_count"]), per_store=3, per_category=2)

    out = {
        "updated": now.astimezone(ZoneInfo("America/Los_Angeles")).isoformat(),
        "min_discount_pct": round(cfg["min_discount"] * 100),
        "total_found": len(pool),
        "stores": status,
        "top": top,
        "categories": categories,
        "ended": ended,
    }

    summary = (f"{ok_count}/{len(stores)} stores scanned, {len(pool)} deals found, "
               f"{len(shown)} shown, {len(ended)} recently ended")
    if brands.on:
        kept = sorted(k for k, v in brands.cache.items() if v)
        dropped = sorted(k for k, v in brands.cache.items() if not v)
        print(f"Brands kept ({len(kept)}): {', '.join(kept)}")
        print(f"Brands skipped ({len(dropped)}): {', '.join(dropped[:150])}")
    print(summary)
    if args.dry_run:
        for it in top:
            print(f"  {it['pct']*100:4.0f}%  ${it['price']:>8.2f}  {it['store_name']}: {it['title']}")
        for c in categories:
            print(f"  [{c['key']}] {c['total']} found")
            for it in c["items"][:5]:
                print(f"      {it['pct']*100:3.0f}%  ${it['price']:>8.2f}  {it.get('name') or it['title']}"
                      f"  {it['url']}  img={'y' if it.get('image') else 'n'}")
        return 0

    write_json(DEALS, out)
    write_json(HISTORY, history)

    # compact full list for the search box: one array per deal, best first
    rows = [[it.get("name") or it["title"], it["brand"], it["variant"], it["store_name"], it["price"], it["was"],
             round(it["pct"] * 100), it["category"], it["url"], it.get("amazon", ""),
             1 if it.get("sponsored") else 0, it.get("image", ""),
             " · ".join(it.get("sizes") or [])]
            for it in sorted(pool, key=score, reverse=True)]
    ALL.parent.mkdir(parents=True, exist_ok=True)
    ALL.write_text(json.dumps({"updated": out["updated"], "cats": dict(CATEGORIES), "items": rows},
                              ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")

    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as fh:
            fh.write(f"### 3D printing deals\n{summary}\n\n| Store | Result |\n|---|---|\n")
            for r in status:
                res = (f"{r['scanned']} products, {r['deals']} deals" if r["ok"]
                       else f"❌ {r['error']}")
                fh.write(f"| {r['name']} | {res} |\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
