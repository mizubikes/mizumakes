---
title: "PLA vs PETG vs ASA for Outdoor Prints: What the TDS Says"
date: 2026-11-01
description: "PLA, PETG, and ASA compared for outdoor parts using data-sheet heat deflection, Z-axis strength, UV behavior, print settings, and current US prices."
slug: pla-vs-petg-vs-asa-outdoor-prints
categories: ["Guides"]
tags: ["ASA", "PETG", "PLA", "outdoor printing", "filament"]
cover:
  image: "/images/Parts-printed-in-printer.png"
  alt: "Enclosed desktop 3D printer printing a functional part"
  caption: ""
  relative: false
draft: false
---

*MizuMakes may earn a commission from links in this post.*

Outdoor parts fail in three ways. They soften from heat, they get brittle from UV, or they crack across layer lines after a few thermal cycles. Each of PLA, PETG, and ASA handles those three failures differently. The choice is mostly about which failure your part can tolerate.

I'm using Bambu Lab and Polymaker data sheets because they publish ISO-style numbers. Treat every TDS figure as a ceiling. Those specimens are printed under ideal conditions, and a real part with perimeters, seams, and a Z-axis load path will land lower.

## The numbers side by side

| Property | PLA Basic (Bambu) | PETG (Bambu) | ASA (Bambu) | ASA (Polymaker) |
|---|---|---|---|---|
| HDT at 1.8 MPa | <cite index="20-6">54 °C</cite> | <cite index="17-10">68 °C</cite> (PETG Basic) | <cite index="2-8">92 °C</cite> | <cite index="56-3">100 °C</cite> |
| HDT at 0.45 MPa | <cite index="20-6">57 °C</cite> | <cite index="17-10">71 °C</cite> (PETG Basic) | <cite index="2-8">100 °C</cite> | <cite index="56-3">103 °C</cite> |
| Glass transition | <cite index="20-6">60 °C</cite> | <cite index="19-7">66 °C</cite> (PETG HF sheet) | not reported | <cite index="56-3">98 °C</cite> |
| Water absorption | <cite index="20-6">0.43%</cite> | n/a | n/a | <cite index="56-3">0.4%</cite> |

The heat gap is the main driver. PLA's glass transition sits near 60 °C, so a dark part sitting in direct summer sun is working close to its limit before you add any load. PETG buys you a margin of roughly 10 °C. ASA buys you a different regime, with HDT around 100 °C.

Bambu's own marketing line says <cite index="7-10">ASA can keep its shape at 100 °C, which PETG or ABS cannot</cite>. The HDT table above is consistent with that.

## PLA: indoor-grade, with one outdoor exception

PLA is the cheapest option. Bambu's US store lists <cite index="68-3">PLA Basic at an MSRP of $14.99 per roll</cite>, with a printing window of <cite index="22-11">190–230 °C nozzle and 35–45 °C bed</cite>. It also prints stiff, with <cite index="25-12">a bending modulus around 2750 MPa</cite>.

Outdoors, though, it loses on every axis. It has the lowest Tg here. Aggregated material guides report that <cite index="37-4">PLA degrades fastest of the four, turning brittle and crumbling under prolonged UV</cite>. A rough lifespan table in the same source puts it at weeks to months in direct sun. That table is a compiled estimate, not a controlled weathering test, so use it for ranking only.

PLA is fine for a part that lives outdoors for a weekend, such as a one-off jig for a field repair or a temporary stake. It is not fine for a bracket, a latch, or anything under sustained load, because sustained load plus warm sun is how creep starts.

## PETG: the shade-and-moisture workhorse

PETG sits in the middle on UV. Sources consistently describe its UV resistance as moderate: <cite index="38-13">acceptable for protected or shorter-term outdoor use, since it handles moisture well</cite>. The same aggregated lifespan table gives it 1–2+ years in direct sun, which I'd read as "expect yellowing and embrittlement eventually."

Its strengths are practical. Bambu's PETG Basic is cheap, with a US store listing of <cite index="60-4">$13.99 MSRP for a 1 kg refill</cite>. It also prints without an enclosure. PETG's softer failure mode is useful too. Bambu's HF sheet shows a bending modulus of <cite index="16-9">2050 MPa in XY</cite>. In the same table, <cite index="16-9">impact strength drops from 31.5 kJ/m² in XY to 10.6 kJ/m² in Z</cite>.

That Z-axis penalty is the design lesson for every material here. Orient the part so tension and bending run along the extrusion lines, not across them.

A product note: Bambu <cite index="59-3">retired PETG HF in 2026 and relaunched PETG Basic as its successor</cite>. Some retailers still list HF, and the HF sheet is where I pulled Tg. If you want a [Bambu Lab PETG Basic spool](https://www.amazon.com/s?k=Bambu+Lab+PETG+Basic&tag=mizubikes-web-20), check which version you're getting. For brand-by-brand numbers, see the [PETG brands TDS comparison](/posts/best-petg-filament-brands-functional-parts/).

## ASA: what you pick when the part has to last

ASA is an ABS variant, and the difference is the rubber phase. The acrylate rubber <cite index="35-2">has no double bonds, which gives about ten times ABS's weathering and UV resistance</cite>. That is a chemical reason, not a marketing one. ASA <cite index="35-4">retains gloss, color, and mechanical properties in outdoor exposure</cite>.

The same aggregated table puts ASA at 3–5+ years in direct sun. That is an estimate, but the direction matches the chemistry.

Bambu's ASA TDS lists <cite index="4-9">37 MPa tensile, 9.2% elongation at break, 1920 MPa bending modulus, and 41 kJ/m² impact strength</cite>. Polymaker's PolyLite ASA sheet is more useful for layer-adhesion planning because it reports both orientations. <cite index="49-1">Tensile strength is 43.8 MPa in XY versus 32 MPa in Z, and elongation at break falls from 6.7% to 1.65%</cite>.

That low Z elongation means ASA is stiff and fairly unforgiving across layers. Don't design a snap-fit hook that flexes across layer lines, and don't hang a point load off a printed ASA tab in the Z direction.

## Print settings and what they cost you

ASA is the difficult one. Bambu's sheet lists <cite index="4-9">240–270 °C nozzle, 80–100 °C bed with glue, and under 250 mm/s</cite>, with <cite index="4-9">drying at 80 °C for 8 hours</cite>. Bambu's ASA-CF sheet calls for a <cite index="10-3">45–60 °C chamber</cite>, so I'd plan on an enclosure or a heated chamber. The [Prusa CORE One+ chamber post](/posts/prusa-core-one-plus-heated-chamber-features/) covers one way to get there. Bambu also flags its plain ASA as <cite index="44-3">not compatible with AMS Lite</cite>.

Warping comes from the outside of the part cooling faster than the inside, so the fix is smaller temperature gradients. That means a warm chamber, a brim, and low part-cooling fan. Keep the fan off or low, because <cite index="78-8,78-9">a heated or enclosed chamber greatly reduces layer splitting, and the fan should stay off or very low</cite>.

Then there is ventilation. ASA <cite index="80-2">releases styrene and other volatile compounds when heated</cite>, so vent it outside or filter it, and don't print it in a living space.

PETG and PLA are easier. For reference, Bambu's HF sheet lists <cite index="15-8">230–260 °C nozzle, 65–75 °C bed, and 65 °C drying for 8 hours</cite>. For PLA, <cite index="20-5">drying is 50 °C for 8 hours</cite>.

## Cost per kilogram

ASA costs more, but not enough to change the decision when the part is a keeper. I found Bambu ASA at <cite index="43-5">$29.99 per kg at one US reseller</cite>, while MatterHackers lists <cite index="41-10">$46.99 for the black spool</cite>. Prices vary a lot by channel, so check before you buy.

Polymaker's ASA shows up around <cite index="57-5">$25.99 on a price-tracking site</cite>. If you're shopping, compare [Bambu Lab ASA](https://www.amazon.com/s?k=Bambu+Lab+ASA+Filament&tag=mizubikes-web-20) with [Polymaker PolyLite ASA](https://www.amazon.com/s?k=Polymaker+PolyLite+ASA+Filament&tag=mizubikes-web-20) on HDT, spool weight, and diameter tolerance. Both publish <cite index="4-8">±0.03 mm diameter</cite>-class specs, so price and drying behavior end up being the tiebreakers.

The [filament cost post](/posts/how-much-does-3d-printer-filament-cost/) tracks prices more broadly.

## How I'd choose

Pick ASA when the part sees direct sun, sits on a hot surface, or carries load for months. Examples include a mount on a vehicle, a sensor housing on a fence post, or a bracket on a south-facing wall. The extra cost and the enclosure are cheap compared with replacing a failed part.

Pick PETG when the part is outdoors but shaded or short-lived, when moisture is the main concern, or when you don't have an enclosure. Examples are a garden drip-line clip under a roof, or a rain-exposed cover in shade. PETG's HDT is only about 68–71 °C in the Bambu data, so keep it away from dark surfaces in direct sun.

Pick PLA only for temporary or indoor-adjacent parts. If you need the PLA-versus-PETG argument in more detail, see [PLA vs PETG](/posts/pla-vs-petg/).

One caveat applies to all three. UV life figures in vendor and aggregator material are estimates. If a part is safety-critical, such as a load-bearing clamp or something over someone's head, don't trust a single data-sheet number. Add margin, orient layers away from the load, and plan to inspect or replace it.

## Sources

- https://cdn.shopify.com/s/files/1/0584/7236/6216/files/Bambu_ASA_Technical_Data_Sheet.pdf?v=1690434954
- https://stemfinity.com/products/bambu-lab-pla-asa
- https://device.report/manual/15698189
- https://wiki.bambulab.com/filament-acc/abs-asa-pc/bambu_pla_basic_technical_data_sheet.pdf
- https://hartsmartproducts.com/products/bambu-pla-basic
- https://www.dynamism.com/bambu-lab/bambu-lab-pla-basic.html
- https://manuals.plus/bambu-filament/petg-hf-launches-new-high-speed-manual
- https://solidprint3d.ie/product/bambu-lab-petg-hf-filament/
- https://www.smith3d.com/shop/materials/petg/bambu-lab-petg-hf-filament-1kg-1-75mm-fast-printing-petg-high-flow-rfid-durable-filament-low-warping-petg-ams-compatible/
- https://filamentcompare.com/petg-hf-vs-petg-filament/
- https://3dprinting.com/filament/best-petg-filament/
- https://us.store.bambulab.com/products/petg-basic
- https://us.store.bambulab.com/products/pla-basic-filament
- https://wiki.polymaker.com/polymaker-products/more-about-our-products/documents/technical-data-sheets/abs-asa/polymaker-tm-asa
- https://3dfilamentprofiles.com/filament/details/727
- https://filascope.com/filament/polymaker-asa-polymakertm-asa--jet-black--45104685
- https://www.matterhackers.com/store/c/bambu-lab-asa-filament
- https://shop3duniverse.com/products/bambu-lab-asa-1-75mm-1kg
- https://ultimate3dprintingstore.com/products/bambu-lab-asa-filament-1-75mm-1kg-gray
- https://en.wikipedia.org/wiki/Acrylonitrile_styrene_acrylate
- https://filaments.ai-driven.ai/content/pla-vs-petg-vs-abs-vs-asa-outdoor-uv-resistance
- https://www.tripo3d.ai/blog/asa-vs-petg
- https://3dtrcek.com/en/blog/post/how-to-print-asa-filament-a-practical-guide-for-durable-prints
- https://1c3d.com/howtos/how-to-print-asa-filament-enclosure-ventilation-and-warping-solutions
- https://www.crea3d.com/en/filaments/1306-bambu-asa.html
