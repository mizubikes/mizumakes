---
title: "Best PETG Filament Brands for Functional Parts, by the Numbers"
date: 2026-10-25
description: "Prusament, Polymaker, Overture, eSUN and Bambu PETG compared on data-sheet HDT, layer strength, tolerance and price per kg for functional parts."
slug: best-petg-filament-brands-functional-parts
categories: ["Guides"]
tags: ["petg", "filament", "functional parts", "material selection"]
cover:
  image: "/images/best-petg-filament-brands-functional-parts-cover.webp"
  alt: "FDM 3D printer printing a functional part on the build plate"
  caption: "Photo: jaziaraujo / Pixabay"
  relative: false
draft: false
---

*MizuMakes may earn a commission from links in this post.*

PETG is the default material for brackets, enclosures, jigs and fixtures when PLA is too brittle or too heat-sensitive and ASA or nylon is more machine than the job needs. Brands are not interchangeable, though, and the differences show up in the data sheets. This post compares the common options on published numbers. It is based on data sheets and listings, not hands-on testing. If you're still deciding between materials, start with [PLA vs PETG](/posts/pla-vs-petg/).

## What a PETG data sheet can and can't tell you

TDS values come from ideal specimens printed under the manufacturer's best conditions. Your part will land lower, and the biggest gap is across layers (the Z axis). That's the axis where PETG parts fail.

The Z-axis numbers show it. Polymaker's data set lists <cite index="28-3">Z-axis tensile strength of 42.8 MPa and 3.3% elongation at break</cite>, against <cite index="27-3">8.4% elongation in the X-Y plane</cite>. Overture's listed values follow the same pattern, with <cite index="37-6">9.3% elongation in X-Y versus 3.5% in Z</cite>. A material that stretches 9% in-plane and breaks at 3.5% across layers is not isotropic, whatever the headline tensile number says.

Compare numbers carefully, too. Test standards differ (eSUN's sheet cites <cite index="40-5">GB/T methods</cite>, while Prusa and Polymaker cite ISO), and specimen prep varies. Sheets also get revised. An older Polymaker PolyLite PETG revision listed <cite index="29-5">13.4 MPa tensile strength in Z with 1.3% elongation</cite>, far below the later figures. Check the revision date before you trust a number.

## PETG brands compared on published numbers

| Brand / product | HDT @ 0.45 MPa | Tensile, in-plane | Tensile, Z | US price (1 kg) |
| --- | --- | --- | --- | --- |
| Prusament PETG | <cite index="3-8">68 °C</cite> | <cite index="9-6">47 MPa</cite> | not reported as a Z test | <cite index="58-3">$29.99</cite> |
| Polymaker PolyLite PETG | <cite index="25-3">78 °C</cite> | <cite index="28-3">50.8 MPa</cite> | <cite index="28-3">42.8 MPa</cite> | <cite index="74-3">$19.99</cite> |
| Overture PETG | Vicat <cite index="37-6">75 °C</cite> (no HDT found) | <cite index="37-6">47.9 MPa</cite> | <cite index="37-6">45.7 MPa</cite> | <cite index="36-6">$14.99</cite> (black) |
| eSUN PETG | <cite index="40-5">64 °C</cite> | <cite index="42-4">34.8 MPa</cite> | <cite index="42-4">28.7 MPa</cite> | not verified |
| Bambu Lab PETG HF (discontinued) | <cite index="16-4">69 °C</cite> | <cite index="16-4">34 ± 4 MPa</cite> | <cite index="18-13">23 MPa</cite> | n/a |

Two caveats on the table. Prusa's sheet reports <cite index="9-6">horizontal and vertical xz print directions</cite> rather than a through-layer test, so I left its Z cell empty rather than guess. And the Overture Z value sitting this close to its X-Y value looks optimistic to me. I'd treat it as a best-case specimen result.

## Prusament PETG: tight tolerance, plus a flame-retardant option

Prusa states <cite index="56-7">±0.02 mm precision</cite> on its in-house filament. That matters for AMS or MMU feeding and for consistent extrusion on thin walls. Its TDS lists <cite index="9-5">250 ± 10 °C nozzle, 80 ± 10 °C bed, 50% fan and speeds up to 200 mm/s</cite>. The notched Charpy numbers are modest at <cite index="3-8">6 kJ/m² horizontal and 3 kJ/m² vertical</cite>, which is a reminder to put fillets on internal corners. PETG doesn't like sharp notches.

The variant I'd watch for electronics work is PETG V0. Prusa calls it <cite index="52-5">a UL-certified self-extinguishing PETG</cite> and positions it for <cite index="52-7">housings and insulating parts in electronics</cite>. It lists at <cite index="52-4">$54.99</cite>, so use it where flammability actually matters. It's overkill for a cable clip.

Search for [Prusament PETG on Amazon](https://www.amazon.com/s?k=Prusament+PETG+1.75mm+1kg&tag=mizubikes-web-20) if you prefer that route, though Prusa's own US warehouse is the primary listing.

## Polymaker PolyLite PETG: the best heat numbers in the group

This is the pick if heat margin matters. The TDS gives a <cite index="25-3">glass transition of 81 °C, Vicat of 84 °C, and HDT of 78 °C at 0.45 MPa and 75 °C at 1.8 MPa</cite>. That's the highest HDT of the filaments I could source. Equilibrium water absorption is <cite index="25-3">0.54%</cite>, so it's hygroscopic. Polymaker suggests <cite index="21-8">drying at 65 °C for 6 hours</cite>.

Its FAQ makes a point worth applying to structural parts: the cooling fan gives <cite index="22-3,22-4">a nicer surface, but no fan gives stronger, more durable parts</cite>. A 20% fan is their compromise. Chemical ratings changed between revisions. One revision rates weak acids <cite index="25-3">good</cite> and another says <cite index="29-3">not resistant</cite>. If a part will see solvents or cleaners, test a coupon.

[PolyLite PETG on Amazon](https://www.amazon.com/s?k=Polymaker+PolyLite+PETG+1.75mm+1kg&tag=mizubikes-web-20) runs around $20 per kilogram at retailers like B&H.

## Overture PETG: the budget option for fixtures and jigs

Overture is the cheapest here. A black spool is <cite index="36-6">$14.99 per 1 kg</cite>, and a 2-pack works out to <cite index="36-6">$14.49/kg</cite>. Listings claim <cite index="31-1">±0.02 mm dimensional accuracy</cite>, though other retail listings quote ±0.03 mm, so I wouldn't treat that figure as settled. The company also states a <cite index="33-4">one-year shelf life for unopened spools</cite>.

The gap is thermal data. I couldn't find an HDT, only a <cite index="37-6">Vicat softening temperature of 75 °C</cite>, about 9 °C below Polymaker's Vicat. For jigs, drill guides, soldering-station holders and shop fixtures at room temperature, that's fine. For anything near a warm motor or a sun-baked dash, I'd choose a filament with published HDT numbers. Get the [Overture PETG](https://www.amazon.com/s?k=Overture+PETG+Filament+1.75mm&tag=mizubikes-web-20) in bulk if you burn through spools.

## eSUN PETG: check which product line you're buying

eSUN sells several PETG formulations with different numbers, and the names are easy to confuse. The standard PETG sheet lists <cite index="40-5">HDT of 64 °C at 0.45 MPa</cite> and <cite index="42-4">Z-axis Izod impact of 1.78 kJ/m²</cite>. PETG-Basic claims <cite index="43-7">73 °C</cite>, and PETG+HS lists <cite index="44-2">68 °C</cite>. The standard grade has the lowest HDT in this comparison. Buy by the exact product name and download that sheet. I couldn't verify a current US price, so I've left it out. Here's the [eSUN PETG search](https://www.amazon.com/s?k=eSUN+PETG+1.75mm+1kg&tag=mizubikes-web-20).

## Bambu Lab: PETG HF is gone

Bambu's own store now states that <cite index="61-7,61-8">PETG HF is discontinued and won't be restocked, and points buyers to a new PETG</cite>. The old sheet showed <cite index="16-4">34 ± 4 MPa tensile, 8.6% elongation and 69 °C HDT</cite>. A Z-axis tensile of 23 MPa is the weakest layer figure in my table. Pull the current PETG sheet from Bambu before you commit, because I couldn't verify its numbers from a primary source.

## Print settings that matter for load-bearing PETG

The data sheets agree on a window of roughly 230–260 °C at the nozzle. Bambu and Polymaker both list <cite index="19-9">230–260 °C</cite>, and eSUN's standard grade lists <cite index="46-6">230–250 °C</cite>. For strength, I'd stay in the upper half of that range to improve layer fusion, and turn the fan down to 20–50% rather than 100%. The tradeoff is more stringing and sagging bridges.

Bed temperatures run 65–90 °C depending on the brand. PETG welds itself to bare surfaces, and one buyer's guide notes that it <cite index="30-3">can tear chunks out of PEI or glass</cite>. Use a thin release layer such as glue stick on smooth PEI.

Dry it. Bambu specifies <cite index="12-3">65 °C for 8 hours in a blast drying oven</cite>, and Polymaker says 65 °C for 6. Wet PETG gives weak, bubbly walls, and you won't see it until the part cracks.

A brass nozzle is fine for unfilled PETG. On flow, one filament database lists a <cite index="18-14,18-15">maximum volumetric speed of 21 mm³/s for Bambu's HF</cite>, but I'd plan on a conservative 10–12 mm³/s for structural parts and tune up from there.

## Design rules for PETG parts that carry load

Orient the part so the main load runs along the layers, not across them. Use four or more walls instead of raising infill, because walls carry most of a printed part's strength. Put fillets on internal corners, given the notch sensitivity above. Design snap fits with long, gentle arms, since PETG yields at a few percent strain.

Use heat-set inserts or through-bolts with washers instead of threading plastic. And design for creep. PETG under sustained load deforms well below its tensile number. As a rule of thumb, I'd derate heavily for anything that stays loaded for months, and I'd test a prototype.

## When not to use PETG

Skip PETG for sustained temperatures near 60 °C and above. HDT figures are measured under a short test load, and PETG's glass transition sits around 81 °C at best. Skip it for long outdoor exposure too. For that, [ASA is the better choice](/posts/what-is-asa-filament/). And skip it for precision sliding fits, where PETG's tackiness and creep both work against you. If you need ASA, PC or a CF nylon, an enclosed machine such as the [Prusa CORE One+](/posts/prusa-core-one-plus-heated-chamber-features/) is the better match.

## My pick, by use case

For shop jigs and fixtures at room temperature, Overture's price per kilogram wins. For a part with more thermal headroom, Polymaker PolyLite has the best published HDT and the most complete data set. For tight tolerance and an in-house quality guarantee, choose Prusament, and choose PETG V0 when the part is an electronics enclosure that needs a flame rating. Skip eSUN standard PETG if you need heat margin, and don't build a workflow around Bambu's discontinued HF.

## Sources

- https://prusament.com/wp-content/uploads/2022/10/PETG_Prusament_TDS_2021_10_EN.pdf
- https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-prusament-prod/2023/10/9f8d2165-tds_prusament-petg_n_en.pdf
- https://www.prusa3d.com/product/prusament-petg-jet-black-1kg-nfc/
- https://www.prusa3d.com/product/prusament-petg-v0-natural-1kg/
- https://www.prusa3d.com/product/prusament-petg-pistachio-green-1kg-clearance/
- https://www.poly-maker.jp/download/TDS/PolyLite_PETG_TDS_EN_V5.4.pdf
- https://incept3d.com/datasheets/polymaker-polylite-petg-v5.1.pdf
- https://www.spoolscout.com/data-sheets/polymaker/petg-polylite-petg
- https://3dfilamentprofiles.com/defaults/polymaker/petg/polylite
- https://eu-wholesale.polymaker.com/products/polylite-petg
- https://www.matterhackers.com/store/l/polymaker-polylite-petg-3d-printer-filament/sk/MAW5MH42
- https://www.bhphotovideo.com/c/product/1809141-REG/polymaker_pb01041_polylite_petg_1_75mm_1000g.html
- https://www.spoolscout.com/product/B07SB761QR
- https://www.spoolscout.com/product/B07XRKRYTV
- https://www.amazon.com/OVERTURE-Filament-Consumables-Dimensional-Accuracy/dp/B0991YSBDG
- https://overture3d.com/products/overture-petg-3d-printer-filament-1-75mm-2-kg
- https://www.esun3d.com/media/esun/catalog/certification/product/PETG/eSUN_PETG_Filament_TDS_1.pdf
- https://www.esun3d.com/petg-product
- https://www.esun3d.com/epetg-lite-product
- https://www.esun3d.com/epetg-hs-product
- https://www.spoolscout.com/data-sheets/esun/petg-petg
- https://us.store.bambulab.com/products/petg-hf
- https://store.bblcdn.com/3a230e260a3a47c2b0db0156e07eef91.pdf
- https://www.crea3d.com/en/filaments/1537-bambu-petg-hf.html
- https://3dfilamentprofiles.com/filament/details/439
- https://stemfinity.com/products/bambu-lab-petg-hf
- https://3dprinting.com/filament/best-petg-filament/
