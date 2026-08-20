---
title: "Why an 8-Tool Prusa INDX Might Be My Next Printer"
date: 2026-08-19
draft: false
description: "The Prusa/Bondtech INDX adds up to 8 independent toolheads to a CORE One+ for true multi-material printing. Here's why the ~$999 8-tool kit is on my upgrade shortlist — and why 'Nozzlegate' means it isn't in my cart yet."
tags: ["prusa", "core one", "indx", "toolchanger", "multi-material", "bondtech"]
categories: ["Guides"]
cover:
  image: "/images/prusa-indx-8-tool.jpg"
  alt: "Prusa CORE One+ fitted with the INDX toolchanger and its row of docked nozzles"
  caption: "The INDX conversion kit turns a CORE One+ into an 8-tool changer. Image: Prusa Research"
  relative: false
  hiddenInList: false
---

I don't need a printer that goes faster. The one I have now is fine on speed. What I keep bumping into is a wall the machine can't get past no matter how good my profiles are: one nozzle, one melt zone, one material at a time. Every color change is a purge. Mixing a flexible part with a rigid one in the same print is a non-starter. Different nozzle sizes in one job? Forget it.

That's the wall the Prusa INDX walks straight through, and it's the first upgrade in a while that's made me seriously reconsider what I'm printing on. It's also, right now, in the middle of a bumpy launch — which is exactly why it's on my shortlist and not in my cart.

## What the INDX actually is

The INDX is a toolchanger — but not the kind that costs as much as a car. It's a conversion kit that Prusa built with Bondtech, and it adds up to **eight independent toolheads** onto a CORE One or CORE One+. Each material gets its own dedicated hotend and nozzle. There's no shared melt path, so there's no cross-contamination and no purge tower eating half your plate.

The clever bit is that the eight tools are *passive* — no motors, no heaters, no wires hanging off each one. The heavy, expensive parts (the extruder and the induction heating) live on the main "smart head," which grabs a parked tool and heats its nozzle on the fly using an induction coil, with wireless, contactless temperature sensing. That's why adding tools stays cheap: you're buying a nozzle and a dock, not a whole second print head.

A few numbers that got my attention:

- **Tool changes take about 12 seconds** — the gap from one nozzle stopping to the next one laying material.
- On big multi-material jobs, total waste can come in around **20–30 g**. Compared to a filament-switching system chewing through a purge block on every swap, that's a different universe.
- You can load **different nozzle sizes at once** — the toolheads accept 0.2, 0.4, 0.5, 0.6, 0.8 and 1.0 mm+ nozzles, so you might keep a fine 0.2 mm for detail and organic supports, a 0.4 mm for general work, and a big 0.8 mm for large jigs and fixtures, all staged before the print even starts. (Kits ship with high-flow 0.4 mm nozzles; other sizes are sold separately.)

It's worth being precise about what this *isn't*: it's not a filament-switcher that feeds many spools into one hotend (that's the MMU/AMS approach). It's a true toolchanger, which is exactly why it can do the material-mixing tricks a single-nozzle machine physically cannot.

## Why the heated chamber matters here too

The reason the INDX rides on the CORE One+ and not a bed-slinger is the platform underneath it. The CORE One is a fully enclosed CoreXY with active chamber temperature control up to **55 °C**, which is what lets it run ASA, PC, and nylon without the enclosure fighting you — I break down the printer itself in my [CORE One+ features overview](/posts/prusa-core-one-plus-heated-chamber-features/). The INDX toolheads themselves are rated to at least 300 °C and to operate in that warm chamber.

Pair the chamber with eight tools and the pitch clicks into place: it's not just eight *colors*, it's eight *materials* — a rigid composite structure, a flexible TPU gasket, and a dissolvable support interface, printed together in one enclosed, temperature-stable job. That combination is the actual reason I'd move, more than any single feature on its own.

*(If your interest is purely "what filament can I run," most of that comes from the CORE One's chamber, not the INDX — see my notes on [PLA vs PETG and where each earns its place](/posts/pla-vs-petg/) for the lower-temp end of that spectrum.)*

## The rollout is rough right now — and that's the honest headline

Here's the part the marketing pages won't lead with. As of mid-August 2026, the INDX is real and shipping in pieces, but it is *not* a settled product you can just click and buy.

The limited **Founders Edition** (1,000 units, sold through Bondtech) reached early adopters in early July, and hands-on reports confirm the mechanism does what it claims. The broader **standard Prusa Edition** kits are the ones most people are waiting on — and that first batch sold out back in April but still hasn't shipped. The date has slipped more than once, from end of July, to end of August, to mid-August, and then slipped again.

The reason has a nickname now: **Nozzlegate.** The community discovered that the nozzles shipping with early kits weren't the through-hardened steel the marketing described, and Prusa's and Bondtech's pages quietly dropped the word "hardened." Bondtech confirmed the substitution in late July, and nozzle production became the bottleneck holding up wider shipping. Prusa's mid-August update pointed to compensation details and a firmer shipping timeline landing shortly after — so by the time you're reading this, the situation may look different. **Check the current status before ordering; this is exactly the kind of thing that changes week to week.**

On top of that, it's first-generation hardware in every sense: early reviewers describe a multi-hour install (roughly five to six hours), and the firmware is still being ironed out through rapid updates. None of that is disqualifying for an early adopter. It's very disqualifying if you want something that just works on day one.

## What it actually costs

Budget for two purchases, not one:

- The **CORE One+** itself starts around **$999** for the kit (as listed alongside the INDX in August 2026; assembled and "Ultimate" configurations run higher — verify the current price and what's in the box on Prusa's store).
- The **INDX kit** on top: first-batch US pricing was **$749 for the 4-tool** and **$999 for the 8-tool** version, tariffs included (about €669/€899 with VAT). You can start at four tools and expand to eight later, since the passive tools are cheap to add.

Yes, that's two different "$999" figures — the printer's from-price and the 8-tool kit — so don't let them blur together. All of these move around; confirm against the live cart before you count on any of them.

One compatibility note before you buy the printer: Prusa lists the INDX as fitting the **CORE One and the CORE One+**, but **not the larger CORE One L**. So if you're eyeing the L for its bigger bed, the toolchanger isn't an option there yet — the standard-size machine is the one to get if the eight tools are the goal.

## Where it sits next to the Bambu path

I've made the case elsewhere that if you mostly want easy, affordable *color* printing, a Bambu with an AMS is hard to beat — that's still the honest answer in my [P1S vs P2S buyer's guide](/posts/bambu-p1s-sale-vs-p2s/), and it's why the [2026 Bambu lineup](/posts/bambu-lab-new-printers-2026/) is where I keep pointing people who just want to hit print.

The INDX is a different axis entirely. A filament-switcher fundamentally can't combine incompatible materials in one melt path — run TPU through the same hotend as PLA and you'll be clearing jams, not printing gaskets. The moment you need *functional* multi-material — mixed flexibility, soluble supports, different nozzle sizes in one part — the toolchanger stops being a luxury and becomes the only thing that does the job.

There's also a money angle worth naming: Bambu's own true multi-material answer, the H2C, is a whole new machine in the ~$2,400 range, while the INDX is a $749–$999 upgrade to a CORE One+ you might want anyway. If you're already eyeing an enclosed CoreXY, that reframes the toolchanger from "expensive luxury" to "the cheaper path to capability" — assuming the rollout settles down.

So the way I'm framing my own decision: color-on-a-budget stays with Bambu; capability-I-can't-get-anywhere-else is what the INDX is for.

## Bottom line

[PLACEHOLDER — YOUR HONEST PERSONAL HOOK: what you currently print on, the specific job or material combo you keep wishing you could do, and roughly what your budget window is. This is the "my next printer" heart of the piece — keep it true.]

For now it stays firmly on the shortlist rather than in my cart, and Nozzlegate is a big part of why. But it's the first machine in a while where the reason to buy isn't "a bit faster" or "a bit bigger" — it's "does something mine literally can't." That's a more interesting reason to spend money. I want to see the standard kits actually land, the nozzle situation resolved, and a few independent long-term reviews first. If those go well, this is the top of my list.

*Pricing, availability, and the nozzle situation noted here reflect mid-to-late August 2026 and are changing quickly — verify against the live Prusa store and the latest INDX status update before ordering.*
