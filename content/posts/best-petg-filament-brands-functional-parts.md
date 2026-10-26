---
title: "Best PETG Filament Brands for Functional Parts, by the Numbers"
date: 2026-10-25
description: "Prusament, Bambu Lab, Polymaker, Overture and eSUN PETG compared on data-sheet HDT, layer strength, tolerance and price per kg for load-bearing parts."
slug: best-petg-filament-brands-functional-parts
categories: ["Guides"]
tags: ["PETG", "filament", "functional parts", "material selection"]
cover:
  image: "/images/best-petg-filament-brands-functional-parts-cover.webp"
  alt: "FDM 3D printer printing a functional part on a heated build plate"
  caption: "Photo: tegawi / Pixabay"
  relative: false
draft: false
---

*MizuMakes may earn a commission from links in this post.*

Most "best PETG" lists rank brands by how well they print. For a bracket, a jig, or an enclosure, I care more about three things: how much strength is left across the layers, how much temperature margin the data sheet gives you, and whether the diameter is consistent enough for flow to stay predictable. This guide compares the major brands on those criteria, using manufacturer technical data sheets (TDS) wherever I could find them.

One caveat first. TDS numbers come from ideal specimens, often printed at 100% infill with settings the maker chose. A real part with a few walls and sparse infill will land lower, and it will be weakest across the layers (Z). Treat the numbers below as a way to compare brands, not as design allowables.

If you're still deciding whether PETG is the right material, start with [PLA vs PETG](/posts/pla-vs-petg/).

## What PETG can and can't do

PETG's thermal ceiling is modest. Bambu's current PETG Basic sheet lists a <cite index="54-8">glass transition of 69 °C</cite> and heat deflection of <cite index="54-8">68 °C at 1.8 MPa and 71 °C at 0.45 MPa</cite>. Prusament lists <cite index="1-8">68 °C at both loads</cite>. A buyer's guide that compared several makers' sheets found published figures <cite index="59-9">between 64 and 72 °C at 0.45 MPa</cite>.

HDT is a short-test deflection point, not a continuous-use rating. A part that carries sustained load will creep well below those temperatures. Plan on PETG staying under roughly 50–55 °C in service if it's loaded. That's my engineering margin, not a number from any data sheet.

Chemistry is another limit. Bambu's PETG sheet says the material is <cite index="50-7">not resistant to acid or alkali</cite> and not resistant to some organic solvents. If the part sees a hot car interior, a motor housing, or months of direct sun, step up to ASA. I cover that in [What is ASA Filament?](/posts/what-is-asa-filament/).

## The comparison

All values are from each maker's TDS or listing unless noted. "XY" is in-plane. "Z" is across layers.

| Brand / product | HDT @ 0.45 MPa | Tensile XY / Z (MPa) | Diameter tolerance | 1 kg price |
| --- | --- | --- | --- | --- |
| Prusament PETG | <cite index="1-8">68 °C</cite> | <cite index="1-8">47 horizontal / 50 vertical (XZ)</cite> | <cite index="81-10">±0.02 mm</cite> | <cite index="78-6">$29.99</cite> |
| Bambu Lab PETG Basic (V3.0) | <cite index="54-8">71 °C</cite> | <cite index="54-8">51 / 35</cite> | not verified | not verified |
| Polymaker PolyLite PETG (V6.0) | <cite index="23-9">78 °C</cite> | varies by sheet revision, see below | not verified | not verified |
| Overture PETG | not published | <cite index="60-8">47.9 / 45.7</cite> (high-speed sheet) | <cite index="31-4">±0.02 mm</cite> (listing) | <cite index="31-1">$17.99</cite> (one color) |
| eSUN PETG | <cite index="68-5">64 °C</cite> | <cite index="68-5">34.8 / 28.7</cite> | <cite index="72-6">±0.03 mm</cite> | not verified |

Two things stand out. First, Prusament's "vertical" specimen is oriented in the XZ plane, so it isn't a true layer-crossing test. Don't read its 50 MPa as a Z number. Second, the Z/XY ratio varies a lot between brands.

## Layer strength: the number that decides bracket life

Bambu's PETG Basic sheet gives <cite index="54-8">51 MPa XY against 35 MPa Z</cite>, so Z retains roughly 69% of in-plane strength. eSUN's sheet gives 34.77 and 28.65 MPa, about 82%. Overture's high-speed PETG sheet lists <cite index="60-8">47.9 MPa XY and 45.7 MPa Z</cite>, about 95%.

That 95% looks remarkable. Be careful, though. The specimens were printed at <cite index="58-7">240 °C, 45 mm/s, 80 °C bed, 100% infill</cite>. eSUN's were <cite index="68-5">260 °C with 100% fan</cite>. Different conditions, different labs, different test fixtures. The ratios are suggestive, not conclusive.

The sheets also drift between revisions. Overture's older sheet lists <cite index="64-3">31.9 MPa XY</cite>. Polymaker's PolyLite sheets show a <cite index="21-6">Z tensile of 13.4 MPa</cite> in one revision and <cite index="25-6">42.8 MPa</cite> in another. A swing like that is more likely a change in test method or print settings than a change in the polymer. When a sheet is vague about specimen conditions, I trust it less.

## Brand by brand

### Prusament PETG: best for dimensional consistency

Prusa makes this filament in-house and <cite index="81-6">guarantees ±0.02 mm precision</cite>. Tight diameter control matters most for parts with press fits, snap fits, or thin walls, where a 3% flow error shows up in the dimensions. The TDS lists <cite index="3-8">250 ± 10 °C nozzle, 80 ± 10 °C bed, and 50% fan</cite>.

The cost is price. Prusa's store lists the 1 kg Jet Black spool at <cite index="78-6">$29.99</cite>. Its category page also showed <cite index="82-5">sale pricing of $23.99</cite> at the time of writing, and 2 kg spools are cheaper per kilogram. The product page also notes <cite index="78-6">possible stringing that may call for occasional drying</cite>.

For electronics housings, Prusa also sells a flame-retardant version. It's described as a <cite index="83-7">UL-certified self-extinguishing PETG</cite> and lists at <cite index="83-6">$54.99</cite>. Standard PETG is flammable, so this is the only variant in this list that fits an enclosure with a fire requirement. [Prusament PETG on Amazon](https://www.amazon.com/s?k=Prusament+PETG+1.75mm+1kg&tag=mizubikes-web-20) is an option if you want to compare retailers.

### Bambu Lab PETG Basic: best if you run an AMS

Bambu reformulated PETG Basic, and the current sheet reports an in-plane tensile strength of 51 MPa. Bambu's store says the new formula <cite index="53-1">matches the strength of PLA Basic</cite> while keeping toughness. The same table gives <cite index="53-3">56 MPa Z bending strength</cite>.

The weak spot is Z tensile at 35 ± 6 MPa. That tolerance is wide, so orient anything that pulls on layers with margin in mind. An independent reviewer's reading of the sheet likewise recommends <cite index="57-6,57-7">testing the installed load direction</cite>.

Drying matters here. Bambu's store says to <cite index="53-1">dry before use</cite>. Its PETG HF sheet specifies <cite index="18-9">65 °C for 8 hours</cite> in an oven and storage under <cite index="18-9">20% RH</cite>. A related HF review notes that Bambu's older HF grade shows <cite index="17-13">only 23 MPa across layers on its sheet</cite> (per a third-party aggregator of the TDS). For load-bearing parts, Basic looks like the better pick of the two. Search [Bambu Lab PETG Basic](https://www.amazon.com/s?k=Bambu+Lab+PETG+Basic+1.75mm&tag=mizubikes-web-20) to compare listings.

### Polymaker PolyLite PETG: best temperature margin

PolyLite PETG is the thermal standout on paper. The June 2026 V6.0 sheet lists <cite index="23-8">a glass transition of 81 °C</cite> and <cite index="23-9,23-10">HDT of 78 °C and 75 °C</cite>. That's a few degrees better than the others here. The equilibrium water absorption is listed at <cite index="23-8">0.54% at 70% RH, 23 °C</cite>, so it still needs drying.

Polymaker also sells a newer "Polymaker PETG" high-flow grade, with a lower <cite index="29-10,29-11">Tg of 71.24 °C</cite>. Check which one you're buying. The names are close, and the thermal and mechanical data differ. PolyLite TDS settings call for <cite index="22-9">230–260 °C nozzle and 70–80 °C bed</cite>. [Polymaker PolyLite PETG](https://www.amazon.com/s?k=Polymaker+PolyLite+PETG+1.75mm&tag=mizubikes-web-20) is the search to start with.

### Overture PETG: best value per kilogram

Overture is the budget pick that keeps showing up in roundups, and the TDS backs part of that. The high-speed sheet's Z tensile figure is close to its XY figure. The Amazon listing for one color was <cite index="31-1">$17.99 per kilogram</cite>, and a price tracker lists multipacks at <cite index="38-10">$12.83 per kg</cite> for a six-spool bundle. That's about 40–60% below Prusament's list price.

The gap is that Overture doesn't publish HDT on the sheet I found. The same sheet gives a <cite index="58-7">Vicat softening point of 85.1 °C</cite>. Vicat isn't HDT, so I wouldn't use it for deflection margin. The maker's drying guidance, as relayed in one buyer's guide, is <cite index="59-4">60 °C for 5 hours</cite>. You can look at [Overture PETG](https://www.amazon.com/s?k=Overture+PETG+1.75mm+1kg&tag=mizubikes-web-20) listings by color and pack size.

### eSUN PETG: fine for jigs, not for heat

eSUN's July 2025 sheet gives the lowest HDT here at 64 °C and about 29 MPa across layers. The Izod impact numbers are low too, <cite index="68-5">4.86 kJ/m² XY and 1.78 kJ/m² Z</cite>. That Z impact figure is the one to notice: a part loaded across layers will be brittle compared with its in-plane behavior.

If a jig or a fixture sits on a bench at room temperature, none of that matters much. For a part near a hotend, a motor, or a car dash, there are better options on this list. [eSUN PETG](https://www.amazon.com/s?k=eSUN+PETG+1.75mm+1kg&tag=mizubikes-web-20) is easy to find if you just need a cheap general-purpose spool.

## Print settings that protect layer strength

Layer bonding in PETG is a thermal process, so print hot and cool lightly. Most TDS ranges run 230–260 °C. For load-bearing parts, aim for the upper half of your maker's range, and cap the part-cooling fan around 50% on walls. Bambu's HF sheet lists <cite index="18-9">0–60% fan</cite>, and Prusa's lists 50%. Very cold layers print prettier overhangs, but they bond worse.

Wall count matters more than infill percentage for stiffness and strength. Use at least 4 walls on brackets, and orient the part so the main load runs along the layers, not across them. Make sure fasteners clamp in compression through the layer stack rather than pulling layers apart.

On the bed, a thin release layer helps. PETG <cite index="30-3">bonds so aggressively to bare PEI and glass that removal can tear chunks out of the surface</cite>. A glue-stick layer between the plate and the part is the usual fix.

If you're using heat-set inserts, remember that PETG's Tg is near 70 °C. A hot iron softens a large zone around the insert. Go slowly and use bosses with generous wall thickness.

## Which one I'd pick

For precision parts with press fits or tight snap features, Prusament's ±0.02 mm guarantee is worth the premium. For AMS-based printing where you want a Bambu profile, PETG Basic is the natural choice, provided you dry it and design around the Z number. For the most thermal margin on paper, PolyLite PETG. For volume and cost, Overture. eSUN is fine for room-temperature jigs.

No PETG here belongs in a part that sees sustained heat, sustained load, or strong solvents. Use ASA, or something like nylon or PC, for those.

Prices and TDS revisions change often, so check the current sheet for the exact spool before you commit to a design.

## Sources

- https://www.prusa3d.com/file/2765253/prusament-petg-technical-data-sheet.pdf
- https://prusament.com/wp-content/uploads/2022/10/PETG_Prusament_TDS_2021_10_EN.pdf
- https://www.prusa3d.com/product/prusament-petg-jet-black-1kg-nfc/
- https://www.prusa3d.com/category/prusament-petg/
- https://www.prusa3d.com/product/prusament-petg-v0-jet-black-1kg-nfc/
- https://www.prusa3d.com/product/prusament-petg-jet-black-1kg-refill/
- https://store.bblcdn.com/s1/default/cb94589bf7994fdcbfa833badefae9cd/Bambu_PETG_Basic_Technical_Data_Sheet.pdf
- https://us.store.bambulab.com/products/petg-basic
- https://store.bblcdn.com/3a230e260a3a47c2b0db0156e07eef91.pdf
- https://store.bblcdn.com/s6/default/20423d7f839c4a66b9712508549c68b4/Bambu_PETG_HF_TDS.pdf
- https://www.scribd.com/document/1013020255/Bambu-PETG-Basic-Technical-Data-Sheet-b1d7a52e-Ddf4-47b3-8e3e-694084b5197e
- https://www.goodprints3d.com/blogs/reviews/bambu-lab-petg-basic-review-a-mainstream-petg-lane-for-utility-parts-that-need-more-heat-margin-than-pla
- https://3dfilamentprofiles.com/filament/details/439
- https://polymaker.com/wp-content/uploads/TDS_Polymaker_PolyLite-PETG_V6.0_2026-06-09_EN.pdf
- https://wiki.polymaker.com/polymaker-products/more-about-our-products/documents/technical-data-sheets/petg-pet/polylite-tm-petg
- https://assets.lulzbot.com/polylite-petg-tds-v5-2-16701.pdf
- https://www.poly-maker.jp/download/TDS/PolyLite_PETG_TDS_EN_V5.4.pdf
- https://3d.nice-cdn.com/upload/file/Polymaker-PETG_TDS_EN_V1.0.pdf
- https://www.amazon.com/OVERTURE-Filament-Consumables-Dimensional-Accuracy/dp/B0991YSBDG
- https://www.scribd.com/document/827544694/OVERTURE-PETG-TDS-EN-V5-1-dd9a50e3-8cc9-4067-b95b-870f56031a85
- https://assets.spoolscout.com/tds-sds/overture/tds/overture-petg-tds.pdf
- https://www.spoolscout.com/product/B07XRKRYTV
- https://www.esun3d.com/media/esun/catalog/certification/product/PETG/eSUN_PETG_Filament_TDS_1.pdf
- https://www.spoolscout.com/data-sheets/esun/petg-petg
- https://3dprinterlab.net/guides/petg-filament-buying-guide-what-to-check-before-you-buy-for-3d-printing/
- https://3dprinting.com/filament/best-petg-filament/
