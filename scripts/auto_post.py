"""
MizuMakes auto-draft generator.

Runs in GitHub Actions. Picks a topic, researches it with Claude + web search,
writes a Hugo post in the MizuMakes voice, pulls a Pixabay cover image, converts
it to WebP under 150KB, and writes everything into the repo. The workflow then
opens a PR so Jared can review the Netlify deploy preview and merge to publish.
"""

import datetime as dt
import io
import json
import os
import re
import sys
from pathlib import Path

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


SYSTEM_PROMPT = f"""You write for mizumakes.com, a 3D printing and maker site run by Jared, an engineer in Southern California with a background in embedded systems, motion control, and manufacturing process development. He prints functional parts and cares about materials, tolerances, and what actually works.

Voice: conversational, technically grounded, honest about real-world tradeoffs, practical decision-making over hype. Write in prose with short paragraphs and a few ## subheadings. Avoid bullet-heavy articles. No generic AI phrasing ("In today's fast-paced world", "game-changer", "dive in", "unleash your creativity"). Do not invent personal printing experiences or claim Jared tested something; frame hands-on claims as what the specs and reporting suggest.

Originality: facts from sources are fine, wording must be entirely your own. Never copy or closely mirror sentences from any article or press release. No quotes longer than a few words.

Accuracy: every spec, price, weight, and date must come from your web searches. If you can't verify something, leave it out. End the body with a short "Sources" section listing the URLs you relied on.

Affiliate links: when you mention a specific product someone might buy, link it with an Amazon search URL in this exact form: https://www.amazon.com/s?k=URL+ENCODED+PRODUCT+NAME&tag={AMAZON_TAG}
Never invent Amazon product IDs. Add one line near the top of the body: "*MizuMakes may earn a commission from links in this post.*"

Internal links: link to 1-3 related existing MizuMakes posts where they genuinely fit, using the relative URLs provided.

Length: 900-1400 words.
"""


def build_user_prompt(seed: str | None, posts: list[dict]) -> str:
    today = dt.date.today().isoformat()
    existing = "\n".join(f"- {p['title']} ({p['url']})" for p in posts) or "(none)"
    if seed:
        topic_line = f"Write about this topic: {seed}"
    else:
        topic_line = (
            "Pick ONE topic yourself: a 3D printer or filament launch, firmware/slicer development, or buyer's-guide question "
            "from roughly the last two weeks that fits FDM printers, filaments, slicers, upgrades, or functional printing, "
            "has buying intent, and is NOT already covered by an existing post below."
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
"image_query": 2-4 word generic stock-photo search (e.g. "3d printer workshop"), no brand names
"image_alt": descriptive alt text for a generic photo matching image_query
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

    def search(q: str) -> list[dict]:
        params = {
            "key": key,
            "q": q[:100],
            "image_type": "photo",
            "orientation": "vertical",
            "safesearch": "true",
            "per_page": 10,
        }
        r = requests.get("https://pixabay.com/api/", params=params, timeout=30)
        r.raise_for_status()
        return r.json().get("hits", [])

    hits = search(query) or search("3d printer")
    if not hits:
        sys.exit("No Pixabay images found")

    photo = hits[0]
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
date: {dt.date.today().isoformat()}
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
