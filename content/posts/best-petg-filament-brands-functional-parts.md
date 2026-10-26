---
title: "Best PETG Filament Brands for Functional Parts, by the Numbers"
date: 2026-10-25
description: "Prusament, Polymaker, Overture, Bambu Lab and eSUN PETG compared on data sheet heat deflection, layer strength, tolerance and US price."
slug: best-petg-filament-brands-functional-parts
categories: ["Guides"]
tags: ["PETG", "filament", "functional parts", "data sheets"]
cover:
  image: "/images/best-petg-filament-brands-functional-parts-cover.webp"
  alt: "FDM 3D printer printing a functional part on a heated bed"
  caption: "Photo: jaziaraujo / Pixabay"
  relative: false
draft: false
---

*MizuMakes may earn a commission from links in this post.*

Most "best PETG" roundups rank spools on first-layer success and how pretty the gloss looks. That's not what decides whether a bracket survives. For a load-bearing part, I'd look at three things: how much heat margin the material has, how much strength you keep across layers, and whether the manufacturer publishes enough data to trust either number.

This guide compares five common PETG options on published data sheet (TDS) values. It's a data-sheet comparison, not a bench test. TDS numbers come from ideal specimens, and your printed part will land lower, especially in Z.

## What PETG can and can't do

Every PETG here shares a thermal ceiling. Bambu Lab's PETG Basic sheet lists a <cite index="55-8">glass transition of 69 °C</cite>, and its HDT is <cite index="55-8">68 °C at 1.8 MPa and 71 °C at 0.45 MPa</cite>. Prusament's sheet gives <cite index="2-8">68 °C at both load levels</cite>. A hot car dashboard, a motor mount, or a part near a heater is outside that envelope. For those, see [what ASA offers over PETG](/posts/what-is-asa-filament/).

HDT isn't a service rating, either. It marks where a loaded bar deflects a set amount over a short test. A part under sustained load will creep well below that temperature, so I'd treat roughly 50 °C as a practical ceiling for anything holding tension. That's an engineering rule of thumb, not a published number.

For the general PETG-versus-PLA tradeoff, see [PLA vs PETG](/posts/pla-vs-petg/). The rest of this article is about choosing between PETG brands.

## The comparison

| Filament | HDT at 0.45 MPa | Layer-direction data (published) | Price I could verify |
|---|---|---|---|
| Prusament PETG | 68 °C | 18 ± 4 MPa interlayer adhesion | $29.99 list (Prusa store) |
| Polymaker PETG | 69–78 °C, depending on sheet revision | 42.8 MPa Z tensile vs 50.8 MPa X-Y (one revision) | $18.99 (Polymaker store) |
| Overture PETG | Not published (Vicat 85.1 °C) | 38.9 MPa Z tensile vs 44.3 MPa X-Y | $14.99 per 1 kg (Overture store) |
| Bambu Lab PETG Basic | 71 °C | 75 MPa X-Y bending strength; 56 MPa Z per a reseller review of the sheet | Not verified |
| eSUN PETG | 64 °C | 28.65 MPa Z tensile vs 34.77 MPa X-Y | Not verified |

Test methods differ across brands. Prusa and Bambu cite ISO, eSUN cites Chinese GB/T standards, and each company prints its own specimens with its own settings. Compare the ratio between Z and X-Y within one data sheet more than raw numbers across sheets.

## Prusament PETG: the one with the best paper trail

Prusament's TDS is the most complete of the group. Its <cite index="2-8">horizontal tensile yield is 47 ± 2 MPa and the vertical xz value is 50 ± 1 MPa, with modulus around 1.5–1.6 GPa</cite>. The sheet also lists <cite index="2-8">interlayer adhesion at 18 ± 4 MPa</cite>, which is the number to care about for anything loaded across layers. It also documents the test conditions: <cite index="2-10">250 °C nozzle, 80 °C bed, 200 mm/s, two perimeters</cite>.

Prusa guarantees <cite index="76-7">±0.02 mm diameter precision</cite>, and <cite index="3-6">per-spool parameters can be checked on prusament.com</cite>. The Prusa store lists 1 kg spools at <cite index="72-6">$29.99</cite>, though some colors were <cite index="75-5">marked down to $23.99</cite> when I looked. That sale price will change.

The tradeoff is price and ordinary PETG limits. Prusa's own page flags <cite index="6-6">possible stringing and poor bridging</cite>. Look for [Prusament PETG on Amazon](https://www.amazon.com/s?k=Prusament+PETG+1.75mm+1kg&tag=mizubikes-web-20) if you'd rather not order direct.

## Polymaker PETG: strong data, but check the revision

Polymaker's published numbers look good for layer strength. One revision of the PolyLite PETG sheet lists <cite index="29-3">50.8 MPa X-Y and 42.8 MPa Z tensile strength, with Z elongation at break of 3.3%</cite>. That's a small Z penalty. The same sheet puts <cite index="26-3">Tg at 81 °C and HDT at 78 °C (0.45 MPa)</cite>.

Here's the catch. An older revision of the same product listed <cite index="30-5">Z tensile strength of just 13.4 MPa against 31.9 MPa X-Y</cite>. And Polymaker now sells a newer high-flow formula, which its store says prints <cite index="89-5">at up to 300 mm/s</cite>. One third-party buying guide reports that formula at <cite index="62-4,62-5">45.71 MPa Z and 47.96 MPa X-Y tensile, with 69 °C HDT</cite>. I couldn't verify that against Polymaker's own PDF, so treat the 78 °C figure and the 69 °C figure as belonging to different sheet versions.

If you buy it, download the TDS for the exact formula on your spool. Polymaker's store lists the new-formula 1 kg spool at <cite index="93-6">$18.99</cite>. Search [Polymaker PETG on Amazon](https://www.amazon.com/s?k=Polymaker+PETG+1.75mm+1kg&tag=mizubikes-web-20).

## Overture PETG: cheapest, but thin on thermal data

Overture is the value pick. Its July 2024 TDS lists <cite index="79-13">44.3 MPa X-Y and 38.9 MPa Z tensile strength, 7.2% elongation, and a Vicat softening point of 85.1 °C</cite>. That's a respectable Z ratio of about 88%. But there's no HDT figure, and Vicat isn't a substitute. For a part where thermal margin matters, I'd skip it or test a sample at temperature first.

Also confirm which sheet you're reading. Overture's January 2024 TDS carried <cite index="83-6">31.9 MPa X-Y tensile and 1472 MPa modulus</cite>, the same figures that appear on Polymaker's older sheet. Data sheets get recycled between products, so look at the date.

Overture's store lists <cite index="36-3">1 kg spools at $14.99</cite> and <cite index="35-4">2 kg at $28.99</cite>. The Amazon listing claims <cite index="31-1">±0.02 mm dimensional accuracy</cite>. That's a marketing figure, not a published trace like Prusa's. Find it at [Overture PETG on Amazon](https://www.amazon.com/s?k=Overture+PETG+1.75mm+1kg&tag=mizubikes-web-20).

## Bambu Lab PETG Basic: good heat margin if you're in the ecosystem

Bambu's current PETG Basic formula claims <cite index="55-5">PLA-level strength with PETG toughness</cite>. The TDS shows <cite index="55-8">71 °C HDT at 0.45 MPa</cite> and a <cite index="55-8">bending modulus of 1950 MPa X-Y and 1740 MPa Z</cite>. That makes it the stiffest of this group in bending, with HDT edging the others by a few degrees. Moisture uptake is also the highest on its sheet at <cite index="55-8">0.45% saturated water absorption</cite>, so dry it before printing.

The previous PETG HF is a different story. Its sheet lists <cite index="18-9">62 °C HDT at 1.8 MPa</cite>, and a reseller review reports it as <cite index="20-5">discontinued, with remaining stock only</cite>. If you own a Bambu machine, the [P1S vs P2S breakdown](/posts/bambu-p1s-sale-vs-p2s/) covers the hardware side. Spools are at [Bambu Lab PETG Basic on Amazon](https://www.amazon.com/s?k=Bambu+Lab+PETG+Basic+1.75mm&tag=mizubikes-web-20).

## eSUN PETG: check which product you're buying

eSUN has several PETG lines with very different sheets. The standard PETG page lists <cite index="66-5">64 °C HDT, 34.77 MPa X-Y and 28.65 MPa Z tensile, and 1.78 kJ/m² Z impact</cite>. That's the lowest HDT of the group. PETG-Basic is a different product: <cite index="60-3">68.41 MPa X-Y but 35.84 MPa Z tensile, with 73.8 °C HDT in X-Y and 68.1 °C in Z</cite>. That's a Z penalty of nearly half.

The matte version shows the same pattern at a larger scale, with <cite index="61-7">49.79 MPa X-Y against 19.51 MPa Z</cite>. A big X-Y number on a data sheet means little if the part loads across layers. Browse [eSUN PETG on Amazon](https://www.amazon.com/s?k=eSUN+PETG+1.75mm+1kg&tag=mizubikes-web-20).

## Print settings that matter more than the brand

Nozzle temperature and bed settings vary by brand, so follow the spool label. Rough published windows: Polymaker lists <cite index="22-9">230–260 °C nozzle, 70–80 °C bed, and 20% fan</cite>. Prusa recommends <cite index="3-10">250 °C nozzle and 70–90 °C bed</cite>. Bambu's sheets list a <cite index="18-8">35–50 °C chamber range</cite> for PETG HF.

For functional parts, run the nozzle at the hotter end of the range and keep the fan low. More heat and less cooling both improve layer bonding, which is the weak axis. Brass nozzles are fine, since Prusa rates unfilled PETG's <cite index="6-6">abrasivity as none</cite>.

Dry the spool. Polymaker's drying guidance is <cite index="22-8">65 °C for 6 hours</cite>, and eSUN's PETG-Basic sheet suggests <cite index="60-3">60 °C</cite>. Wet PETG leaves bubbles and weak layers that don't show up in the first-layer test.

PETG also welds itself to bare PEI. Use a glue-stick release layer on smooth sheets, or you risk tearing the surface when you pull the part off.

## Design rules for PETG parts

Orient the part so the load runs along the extrusion paths, not across layers. A bracket that bends should print on its side, not standing up. Use more walls instead of just more infill, since walls carry the load along the XY plane.

PETG stays ductile, which makes it forgiving for snap fits and clips. Size heat-set inserts and screw bosses with margin, and expect creep if you leave a screw clamped under constant load. Don't use PETG for sustained-load joints in warm places.

When the part sees heat above the mid-60s °C, UV exposure over years, or constant clamping force, step up to ASA, ABS, or a nylon. When it needs flame resistance, Prusament's <cite index="7-2,7-3">UL-certified PETG V0 is aimed at electronics housings</cite>, though it costs more, with the Natural color at <cite index="78-5">$54.99</cite>.

## My pick, by job

For parts where I'd want a documented layer-strength number, Prusament is the safest choice because its sheet reports interlayer adhesion and its test conditions. For budget bulk printing of jigs and fixtures at room temperature, Overture's price is hard to beat, as long as you accept no HDT data. Polymaker sits in between, with strong published Z data and a price below Prusa's, provided you check the revision. Bambu PETG Basic is worth it for Bambu printers where the profile integration saves time. eSUN works, but read the exact product sheet.

None of these is a substitute for printing a test coupon in your orientation and loading it to failure. Do that before committing a part to real duty.

## Sources

- https://www.prusa3d.com/file/2765253/prusament-petg-technical-data-sheet.pdf
- https://prusament.com/materials/prusament-petg/
- https://prusament.com/materials/prusament-petg-v0/
- https://www.prusa3d.com/category/prusament-petg/
- https://www.prusa3d.com/product/prusament-petg-urban-grey-1kg/
- https://www.prusa3d.com/product/prusament-petg-prusa-orange-1kg-clearance/
- https://www.prusa3d.com/product/prusament-petg-v0-natural-1kg/
- https://www.printedsolid.com/products/prusament-petg-1-75mm-1kg-clear
- https://www.poly-maker.jp/download/TDS/PolyLite_PETG_TDS_EN_V5.4.pdf
- https://incept3d.com/datasheets/polymaker-polylite-petg-v5.1.pdf
- https://www.spoolscout.com/data-sheets/polymaker/petg-polylite-petg
- https://shop.polymaker.com/products/polymaker-petg
- https://shop.polymaker.com/collections/petg-filament
- https://www.matterhackers.com/store/l/polymaker-polylite-petg-3d-printer-filament/sk/MAW5MH42
- https://3dprinterlab.net/guides/petg-filament-buying-guide-what-to-check-before-you-buy-for-3d-printing/
- https://www.scribd.com/document/827544694/OVERTURE-PETG-TDS-EN-V5-1-dd9a50e3-8cc9-4067-b95b-870f56031a85
- https://assets.spoolscout.com/tds-sds/overture/tds/overture-petg-tds.pdf
- https://overture3d.com/products/petg-3dprintingfilament
- https://overture3d.com/products/overture-petg-3d-printer-filament-1-75mm-2-kg
- https://www.amazon.com/OVERTURE-Filament-Consumables-Dimensional-Accuracy/dp/B0991YSBDG
- https://store.bblcdn.com/s1/default/cb94589bf7994fdcbfa833badefae9cd/Bambu_PETG_Basic_Technical_Data_Sheet.pdf
- https://store.bblcdn.com/3a230e260a3a47c2b0db0156e07eef91.pdf
- https://www.goodprints3d.com/blogs/reviews/bambu-lab-petg-hf-review-a-faster-petg-pick-for-makers-who-want-tougher-utility-prints-without-giving-up-modern-high-speed-workflows
- https://www.esun3d.com/petg-product
- https://www.esun3d.com/uploads/PETG-Basic-TDS21.pdf
- https://www.smith3d.com/shop/materials/petg/esun-matte-petg-filament-1-75mm-1kg/
