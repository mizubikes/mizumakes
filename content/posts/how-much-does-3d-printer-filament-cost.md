---
title: "How Much Does 3D Printer Filament Cost? (Live Prices Per Kg)"
date: 2026-10-25
description: "What PLA, PETG, and ASA actually cost per kg, what a printed part really costs you, and when the expensive spool is worth it, with prices that update daily."
categories: ["Guides"]
tags: ["filament", "PLA", "PETG", "ASA", "prices"]
cover:
  image: /images/p1s.webp
  alt: "Bambu Lab P1S 3D printer, used to compare filament cost per kg and cost per print"
  relative: false
ShowToc: true
draft: false
---

Short answer: a 1kg spool of decent PLA or PETG costs somewhere between **$14 and $26** at the brand's own store, and ASA runs a few dollars more. Right now the cheapest PLA I track is {{< filament-cheapest "PLA" >}}, and the cheapest PETG is {{< filament-cheapest "PETG" >}}.

That number moves, though. Filament goes on sale constantly, and the same spool can swing 20–30% in a month. So instead of writing numbers that are stale in two weeks, every price on this page is pulled from my [filament price tracker](/filament-prices/), which checks each brand's store every morning.

Here's what you're actually paying for, what a print really costs, and when it's worth paying more.

---

## Filament Cost Per Kg by Material

These are store prices for a single 1kg, 1.75mm spool. Bulk packs and Amazon prices are usually different, so tap through to check yours.

### PLA

The cheapest and easiest material. Most people print 80% of their parts in it.

{{< filament-price "elegoo-pla" >}}

{{< filament-price "polymaker-panchroma-matte-pla" >}}

{{< filament-price "hatchbox-pla" >}}

### PETG

Usually priced right alongside PLA now. A few years ago PETG carried a premium, but the budget brands have closed that gap almost completely.

{{< filament-price "elegoo-rapid-petg" >}}

{{< filament-price "polymaker-petg" >}}

{{< filament-price "hatchbox-petg" >}}

### ASA

You pay a little more for UV and heat resistance. Worth it for anything that lives outside, but overkill for indoor parts. More on that in my [ASA guide](/posts/what-is-asa-filament/).

{{< filament-price "elegoo-asa" >}}

{{< filament-price "polymaker-asa" >}}

---

## Why the Same Material Costs $14 or $26

A 1kg spool of PLA is still a 1kg spool of PLA. The spread comes from a handful of things, and only some of them matter for the parts you print.

**Diameter tolerance and consistency.** Budget and premium brands both advertise ±0.02–0.03mm. The real difference is spool-to-spool and batch-to-batch consistency. Premium brands tend to hold color and flow more consistently across rolls, which matters if you're printing a matching set of parts or running a printer unattended.

**The formula, not just the material.** "PLA" covers a lot: basic, PLA+, high-speed, matte, silk, carbon-filled. Matte and specialty blends cost more to make, and carbon or glass-filled filaments cost a lot more (and need a hardened nozzle).

**The spool itself.** Cardboard spools are cheaper and lighter. Plastic spools cost more and end up in a drawer. Refills without a spool are the cheapest way to buy from brands that offer them, if your printer or AMS can use a reusable spool.

**Ecosystem convenience.** Some printer brands sell filament with RFID tags that auto-load settings into the AMS. It's genuinely convenient, and you pay for it. Third-party filament works fine once you've dialed in a profile once.

**Packaging and drying.** Better vacuum sealing and desiccant mean less moisture out of the box. It matters more for PETG and nylon than for PLA.

My take: for brackets, jigs, enclosures, and prototypes, the budget spools are fine. I pay more when I need color consistency across a batch, or a specific formula like matte PLA for parts that will be on camera.

---

## What a 3D Print Actually Costs

The material math is simple: **grams of filament × price per kg ÷ 1000.** Your slicer tells you the grams before you print.

At today's cheapest PLA price, here's what typical parts cost in filament:

| Part | Filament used | Material cost |
|---|---|---|
| Small clip or spacer | 10g | {{< filament-cost "elegoo-pla" 10 >}} |
| Wall bracket or tool holder | 50g | {{< filament-cost "elegoo-pla" 50 >}} |
| Electronics enclosure | 150g | {{< filament-cost "elegoo-pla" 150 >}} |
| Large functional part | 400g | {{< filament-cost "elegoo-pla" 400 >}} |

*Costs update daily from the cheapest tracked PLA store price.*

The same 150g enclosure in Polymaker ASA, for an outdoor build, costs {{< filament-cost "polymaker-asa" 150 >}} in material. So even the "expensive" option is rarely the expensive part of a project.

### The costs your slicer doesn't show

**Waste.** Supports, brims, and failed first layers add up. I budget roughly 10–15% on top of the slicer estimate for single-color prints.

**Multi-color purge.** If you print multi-color with an AMS or similar single-nozzle system, every color swap flushes filament. On prints with lots of color changes, the purge waste can rival the weight of the part itself. Single-color prints don't have this problem at all.

**Electricity.** A desktop printer like a P1S averages around 100W or so while printing, depending on bed temperature and chamber. At California rates of roughly $0.30–0.40/kWh, that's a few cents per hour. Even a 10-hour print is well under a dollar.

So for most functional parts, the real cost is somewhere between a few cents and a few dollars. The printer and your time are the expensive parts.

---

## When to Buy (and When to Wait)

Filament has a lot of fake sales. A "40% off" banner sometimes just means the price went back to what it was last month. Three things actually save money:

1. **Watch the 90-day low.** The [price tracker](/filament-prices/) logs every brand's store price daily and flags when something is genuinely under its typical price, not just marked "sale."
2. **Buy bulk for your workhorse color.** If you go through black PLA or PETG constantly, multi-spool bundles usually beat single-spool prices by a meaningful margin.
3. **Don't stockpile specialty filament.** Silk, matte, and engineering materials sit for months and absorb moisture. Buy those when you have a project for them.

---

## The Bottom Line

- **PLA and PETG:** roughly $14–26 per kg at brand stores, with budget brands at the low end and nearly identical PLA and PETG pricing.
- **ASA:** a few dollars more, worth it only for outdoor or high-heat parts.
- **A typical functional part:** cents to a few dollars in filament.
- **Premium spools:** pay for consistency when it matters, not by default.

For today's prices across every brand I track, plus the 90-day range for each spool, check the [filament price tracker](/filament-prices/). It updates every morning.

*Amazon links on this page are affiliate links. Store prices are pulled from each brand's own website and don't include shipping or tax.*
