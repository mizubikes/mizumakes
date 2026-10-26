"""
MizuMakes auto-draft generator.

Runs in GitHub Actions. Picks a topic, researches it with Claude + web search,
writes a Hugo post in the MizuMakes voice, pulls a Pixabay cover image, converts
it to WebP under 150KB, and writes everything into the repo. The workflow then
opens a PR so Jared can review the Netlify deploy preview and merge to publish.
"""

import datetime as dt
import base64
import io
import json
import os
import re
import sys
from pathlib import Path
from zoneinfo import ZoneInfo

import anthropic
import requests
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "content" / "posts"
IMAGES_DIR = ROOT / "static" / "images"
TOPICS_FILE = ROOT / "scripts" / "topics.txt"
# Outside the repo so it doesn't get committed with the post
PR_BODY_FILE = Path(os.environ.get("RUNNER_TEMP", "/tmp")) / "pr_body.md"

MODEL = "claude-sonnet-5-5"
# Swap in a MizuMakes-specific tracking ID if you create one in Amazon Associates
AMAZON_TAG = "mizubikes-web-20"
CATEGORIES = ["Blog", "Projects", "Reviews", "Guides", "Gear"]
COVER_MAX_BYTES = 150 * 1024
PACIFIC = ZoneInfo("America/Los_Angeles")
VISION_MODEL = "claude-haiku-5-5"
MAX_VISION_CHECKS = 15
# Used when no stock photo passes the visual check; the PR flags it for a swap
FALLBACK_COVER = "/images/Parts-printed-in-printer.png"

# Reject stock results that show people, renders, or anything off-topic
BANNED_TAGS = {
    "woman", "women", "man", "men", "girl", "boy", "person", "people", "lady",
    "model", "fashion", "beauty", "portrait", "face", "female", "male", "child",
    "fantasy", "character", "render", "rendering", "3d render", "cgi", "daz",
    "costume", "dress", "sexy", "cosplay", "doll", "avatar", "animation",
    # "filament spool" otherwise matches yarn and sewing photos
    "yarn", "wool", "knit", "knitting", "crochet", "sewing", "thread", "threads",
    "embroidery", "textile", "fabric", "skein", "needle", "needlework", "craft",
    "handicraft", "cotton", "string", "twine", "rope", "ribbon", "tape",
    # "filament" and "printer" also match light bulbs and office printers
    "bulb", "light bulb", "lightbulb", "lamp", "edison", "incandescent",
    "teleprinter", "teletype", "teletypewriter", "typewriter", "telex",
    "render", "rendering", "3d rendering", "3d render", "3d model", "blender",
    "office", "paper", "ink", "inkjet", "cartridge", "toner", "document",
}
# A cover must be tagged as 3D printing specifically. Generic tags like
# "technology" or "industrial" also appear on architecture and abstract photos.
REQUIRED_TAGS = {
    "3d printer", "3d printing", "3d print", "3d printed", "3d-printer",
    "3d-printing", "3dprinter", "3dprinting", "3d", "additive manufacturing",
}
# Safe workshop/engineering queries if the model's query returns nothing usable
FALLBACK_QUERIES = ["3d printer", "3d printing", "3d printer nozzle", "3d printed"]


def today_pacific() -> dt.date:
    return dt.datetime.now(PACIFIC).date()


def set_output(name: str, value: str) -> None:
    out = os.environ.get("GITHUB_OUTPUT")
    if out:
        with open(out, "a", encoding="utf-8") as f:
            f.write(f"{name}={value}\n")
    print(f"{name}={value}")


def existing_posts() -> list[dict]:
    posts = []
    # Flat posts (name.md) and page bundles (name/index.md)
    files = list(POSTS_DIR.glob("*.md")) + list(POSTS_DIR.glob("*/index.md"))
    for p in sorted(files):
        text = p.read_text(encoding="utf-8", errors="ignore")
        stem = p.parent.name if p.name == "index.md" else p.stem
        title = re.search(r'^title:\s*"?(.+?)"?\s*$', text, re.M)
        slug = re.search(r"^slug:\s*\"?(.+?)\"?\s*$", text, re.M)
        posts.append({
            "title": title.group(1) if title else stem,
            "url": f"/posts/{slug.group(1) if slug else stem}/",
        })
    return posts


def next_seed_topic() -> str | None:
    if not TOPICS_FILE.exists():
        return None
    lines = [l.strip() for l in TOPICS_FILE.read_text(encoding="utf-8").splitlines()]
    topics = [l for l in lines if l and not l.startswith("#")]
    if not topics:
        return None
    first = topics[0]
    remaining = [l for l in lines if l.strip() != first]
    TOPICS_FILE.write_text("\n".join(remaining).strip() + "\n", encoding="utf-8")
    return first


SYSTEM_PROMPT = f"""You write for mizumakes.com, a 3D printing and maker site run by Jared, an engineer in Southern California with a background in embedded systems, motion control, and medical device process development. He prints functional, load-bearing, and heat-exposed parts, not figurines or decor, and readers come for engineering judgment.

Angle: write every post as an engineer choosing a material, machine, or method for a real functional part. Ground the article in numbers and mechanisms:
- Material properties where relevant: heat deflection temperature, glass transition, tensile strength and modulus, elongation at break, impact resistance, moisture absorption, UV and chemical resistance, shrinkage/warping tendency. Use manufacturer technical data sheets (TDS) as primary sources and note that TDS values are measured on ideal specimens, so printed parts land lower, especially across layers (Z axis).
- Concrete print settings with numbers: nozzle and bed temperature, chamber needs, speeds and volumetric flow, cooling, drying temperature and time, nozzle material.
- Design-for-printing guidance: print orientation relative to load, wall count vs infill, layer adhesion as the weak axis, tolerances and clearances, inserts and fasteners, creep under sustained load.
- Failure modes and when NOT to use something. Name the use cases it fits (brackets, enclosures, jigs and fixtures, outdoor parts, snap fits, hot environments) and the ones it does not.
- When recommending products, compare them on measurable criteria (published TDS numbers, diameter tolerance, spool weight, price per kg) rather than marketing claims.

Voice: conversational, technically grounded, honest about real-world tradeoffs, practical decision-making over hype. Write in prose with short paragraphs and ## subheadings. A compact Markdown table is welcome when comparing materials or products on numbers; otherwise avoid bullet-heavy articles and listicle filler. No generic AI phrasing ("In today's fast-paced world", "game-changer", "dive in", "unleash your creativity", "whether you're a beginner or a pro"). Do not invent personal printing experiences or claim Jared tested something; frame hands-on claims as what the data sheets, specs, and reporting suggest.

Originality: facts from sources are fine, wording must be entirely your own. Never copy or closely mirror sentences from any article or press release. No quotes longer than a few words.

Accuracy: every spec, property value, price, weight, and date must come from your web searches. If you can't verify something, leave it out. End the body with a short "Sources" section listing the URLs you relied on.

Prices: US dollars only, from US retailers or US list prices (e.g. "$24.99"). Never use euros, pounds, or any other currency, and never convert from them. If you can only find a non-USD price, omit the price.

Affiliate links: when you mention a specific product someone might buy, link it with an Amazon search URL in this exact form: https://www.amazon.com/s?k=URL+ENCODED+PRODUCT+NAME&tag={AMAZON_TAG}
Never invent Amazon product IDs. Add one line near the top of the body: "*MizuMakes may earn a commission from links in this post.*"

Internal links: link to 1-3 related existing MizuMakes posts where they genuinely fit, using the relative URLs provided.

Length: 1000-1600 words.
"""


def build_user_prompt(seed: str | None, posts: list[dict]) -> str:
    today = today_pacific().isoformat()
    existing = "\n".join(f"- {p['title']} ({p['url']})" for p in posts) or "(none)"
    if seed:
        topic_line = f"Write about this topic: {seed}"
    else:
        topic_line = (
            "Pick ONE topic yourself: an engineering-focused question about functional FDM printing, such as a material "
            "comparison for a specific use case, a design-for-strength technique, a printer or filament launch from roughly "
            "the last two weeks evaluated on measurable specs, or a buyer's-guide question with clear buying intent. "
            "It must NOT already be covered by an existing post below."
        )
    return f"""Today is {today}.

{topic_line}

Existing MizuMakes posts (avoid duplicates, use for internal links):
{existing}

Research with web search first, then respond with ONLY a JSON object (no code fence, no other text) with these keys:
"title": post title, under 70 characters
"slug": lowercase-hyphenated slug
"description": one-sentence SEO meta description, under 155 characters
"category": exactly one of {CATEGORIES} (Guides = how-tos and buyer's guides, Reviews = single-product evaluations, Gear = tools and accessories, Projects = builds, Blog = news and opinion)
"tags": 2-5 short tags; never use a category name (Blog, Projects, Reviews, Guides, Gear) as a tag
"image_query": 2-4 word stock-photo search naming a physical object or machine, e.g. "3d printer", "3d printing", "3d printer nozzle", "3d printed parts". It must contain "3d print" or "printer". For filament or material topics use "3d printer" or "3d printing", never "filament spool" (it returns yarn photos). No brand names, no material abbreviations alone (never just "PETG" or "PLA"), no people, no abstract words.
"image_alt": descriptive alt text for a generic photo of that object
"body": the full article body in Markdown, without front matter or an H1
"""


def generate_post(seed: str | None, posts: list[dict]) -> dict:
    client = anthropic.Anthropic()
    messages = [{"role": "user", "content": build_user_prompt(seed, posts)}]
    tools = [{
        "type": "web_search_20250305",
        "name": "web_search",
        "max_uses": 10,
        "allowed_callers": ["direct"],
    }]

    for _ in range(6):
        resp = client.messages.create(
            model=MODEL,
            max_tokens=16000,
            system=SYSTEM_PROMPT,
            tools=tools,
            messages=messages,
        )
        if resp.stop_reason == "pause_turn":
            messages.append({"role": "assistant", "content": resp.content})
            continue
        break

    text = "".join(b.text for b in resp.content if b.type == "text").strip()
    match = re.search(r"\{.*\}", text, re.S)
    if not match:
        sys.exit(f"Model did not return JSON:\n{text[:2000]}")
    data = json.loads(match.group(0))

    if data["category"] not in CATEGORIES:
        data["category"] = "Guides"
    # A term used as both a category and a tag breaks the PaperMod nav build
    cats_lower = {c.lower() for c in CATEGORIES}
    data["tags"] = [t for t in data["tags"] if t.lower() not in cats_lower]
    data["slug"] = re.sub(r"[^a-z0-9-]+", "-", data["slug"].lower()).strip("-")
    return data


def fetch_cover(query: str, slug: str) -> tuple[str, str, str]:
    """Returns (image path for front matter, caption, Pixabay page URL)."""
    key = os.environ["PIXABAY_API_KEY"]

    def search(q: str, category: str | None = None) -> list[dict]:
        params = {
            "key": key,
            "q": q[:100],
            "image_type": "photo",
            "orientation": "all",
            "safesearch": "true",
            "per_page": 30,
        }
        if category:
            params["category"] = category
        r = requests.get("https://pixabay.com/api/", params=params, timeout=30)
        r.raise_for_status()
        return r.json().get("hits", [])

    def tag_sets(hit: dict) -> tuple[set, set]:
        tags = {t.strip().lower() for t in hit.get("tags", "").split(",")}
        return tags, {w for t in tags for w in t.split()}

    def not_banned(hit: dict) -> bool:
        tags, words = tag_sets(hit)
        return not (tags & BANNED_TAGS or words & BANNED_TAGS)

    def has_print_tag(hit: dict) -> bool:
        tags, _ = tag_sets(hit)
        return bool(tags & (REQUIRED_TAGS - {"3d"}))

    def looks_right(hit: dict) -> bool:
        """Ask Claude to look at the photo. Pixabay tags are keyword-stuffed and can't be trusted."""
        try:
            img_bytes = requests.get(hit["webformatURL"], timeout=30).content
            resp = anthropic.Anthropic().messages.create(
                model=VISION_MODEL,
                max_tokens=5,
                messages=[{"role": "user", "content": [
                    {"type": "image", "source": {
                        "type": "base64", "media_type": "image/jpeg",
                        "data": base64.b64encode(img_bytes).decode()}},
                    {"type": "text", "text": (
                        "Is this a real photograph whose main subject is clearly a 3D printer, "
                        "3D printed parts, or 3D printer filament spools? Not yarn or thread, not an "
                        "office or paper printer, not a typewriter, not architecture, not a person, "
                        "not a CGI render. Answer only YES or NO.")},
                ]}],
            )
            answer = "".join(b.text for b in resp.content if b.type == "text").strip().upper()
            return answer.startswith("YES")
        except Exception as e:
            print(f"Vision check failed for {hit.get('pageURL')}: {e}")
            return False

    photo = None
    seen: set[int] = set()
    checks = 0
    attempts = [(query, None), (query, "industry"), (query, "science")]
    attempts += [(q, None) for q in FALLBACK_QUERIES]
    for q, cat in attempts:
        hits = [h for h in search(q, cat) if h["id"] not in seen and not_banned(h)]
        # Photos tagged as 3D printing first, then the rest
        hits.sort(key=lambda h: not has_print_tag(h))
        for h in hits:
            seen.add(h["id"])
            if checks >= MAX_VISION_CHECKS:
                break
            checks += 1
            ok = looks_right(h)
            print(f"Cover check {checks}: {'PASS' if ok else 'reject'} {h['pageURL']} tags={h.get('tags')!r}")
            if ok:
                photo = h
                break
        if photo or checks >= MAX_VISION_CHECKS:
            break
    if not photo:
        print("No stock photo passed the visual check; using fallback cover")
        return FALLBACK_COVER, "", "NONE (fallback cover used, swap in a real one before merging)"

    raw = requests.get(photo["largeImageURL"], timeout=60).content
    img = Image.open(io.BytesIO(raw)).convert("RGB")
    img.thumbnail((1200, 1600))

    quality = 75
    while True:
        buf = io.BytesIO()
        img.save(buf, "WEBP", quality=quality, method=6)
        if buf.tell() <= COVER_MAX_BYTES or quality <= 40:
            break
        quality -= 5
        if quality <= 55:
            img.thumbnail((int(img.width * 0.85), int(img.height * 0.85)))

    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    filename = f"{slug}-cover.webp"
    (IMAGES_DIR / filename).write_bytes(buf.getvalue())
    caption = f"Photo: {photo['user']} / Pixabay"
    return f"/images/{filename}", caption, photo["pageURL"]


def yaml_str(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def main() -> None:
    posts = existing_posts()
    seed = next_seed_topic()
    data = generate_post(seed, posts)

    image_path, caption, pixabay_url = fetch_cover(data["image_query"], data["slug"])

    tags = ", ".join(yaml_str(t) for t in data["tags"])
    front = f"""---
title: {yaml_str(data["title"])}
date: {today_pacific().isoformat()}
description: {yaml_str(data["description"])}
slug: {data["slug"]}
categories: [{yaml_str(data["category"])}]
tags: [{tags}]
cover:
  image: "{image_path}"
  alt: {yaml_str(data["image_alt"])}
  caption: {yaml_str(caption)}
  relative: false
draft: false
---

"""
    post_file = POSTS_DIR / f"{data['slug']}.md"
    post_file.write_text(front + data["body"].strip() + "\n", encoding="utf-8")

    PR_BODY_FILE.write_text(
        f"""**{data["title"]}**

{data["description"]}

- Category: {data["category"]}
- Topic source: {"seed list: " + seed if seed else "picked by Claude from recent news"}
- Cover photo: {pixabay_url}

Check the Netlify deploy preview below. Merge to publish, close to skip.
Spot-check specs and prices against the Sources section before merging.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_012nBX9arnGcA8nn1be6PAsX
""",
        encoding="utf-8",
    )

    set_output("slug", data["slug"])
    set_output("title", data["title"].replace("\n", " "))
    set_output("pr_body", str(PR_BODY_FILE))


if __name__ == "__main__":
    main()
