---
title: "Best PETG Filament Brands for Functional Parts (TDS Compared)"
date: 2026-10-29
description: "Prusament, Bambu Lab, Polymaker, Overture, Elegoo and eSUN PETG compared on data-sheet heat, strength, Z-axis numbers, tolerance and US price."
slug: best-petg-filament-brands-functional-parts
categories: ["Guides"]
tags: ["petg", "filament", "functional parts", "material selection"]
cover:
  image: "/images/best-petg-filament-brands-functional-parts-cover.webp"
  alt: "FDM 3D printer printing a functional part on a heated build plate"
  caption: "Photo: mebner1 / Pixabay"
  relative: false
draft: false
---

*MizuMakes may earn a commission from links in this post.*

PETG is the filament I'd reach for when PLA is too brittle or too heat-sensitive and ASA or ABS is more printer than the job needs. But PETG is not one material. Different brands tune the copolymer, additives and drying history differently, and the data sheets show it. This post compares the major brands the way I'd pick one for a bracket, jig or enclosure: published numbers first, marketing last.

If you're still deciding between materials, start with [PLA vs PETG](/posts/pla-vs-petg/). If the part lives in the sun, read [what ASA is and when to stop using PETG outdoors](/posts/what-is-asa-filament/).

## How to read a PETG data sheet

Three numbers matter most for functional parts: heat deflection temperature (HDT), tensile strength in X-Y versus Z, and elongation. The Z-axis number is the one that predicts whether a part splits between layers.

Treat every TDS figure as a best case. They're measured on small coupons printed under tuned conditions. One third-party comparison notes that Bambu's sheets are mostly measured on specimens that were annealed and dried before testing, <cite index="82-14">which a real part off your printer won't have been</cite>. Test standards also differ between makers (ISO versus Chinese GB/T), so close numbers across brands are not a ranking.

HDT is a screening number, not a service rating. A reviewer of Bambu's sheet puts it well: <cite index="89-10">68-71 °C HDT is not a continuous service rating, and creep, geometry and safety margin still need proof</cite>.

## PETG brands compared on published numbers

| Brand / product | HDT at 0.45 MPa | Tensile X-Y / Z (MPa) | Diameter tolerance | US price, 1 kg |
| --- | --- | --- | --- | --- |
| Prusament PETG | <cite index="1-8">68 °C</cite> | <cite index="2-8">47 horizontal / 50 vertical xz</cite> | <cite index="1-8">±0.02 mm</cite> | <cite index="53-1">$28.79 on sale, $35.99 regular (Printed Solid)</cite> |
| Bambu Lab PETG Basic (V3.0) | <cite index="87-9">71 °C</cite> | <cite index="89-11">51 / 35</cite> | <cite index="40-4">±0.03 mm</cite> | <cite index="40-4">$13.99 refill, $16.99 with spool</cite> |
| Polymaker PolyLite PETG (TDS v5.4) | <cite index="28-3">78 °C</cite> | <cite index="28-3">50.8 / 42.8</cite> | <cite index="20-1">±0.05 mm</cite> | <cite index="65-2">$19.99 (Polymaker shop)</cite> |
| Elegoo Rapid PETG | <cite index="71-6">72 °C</cite> | <cite index="71-6">42 / 28</cite> | <cite index="70-2">±0.02 mm</cite> | not verified |
| eSUN PETG | <cite index="72-3">64 °C</cite> | <cite index="77-9">34.77 / 28.65</cite> | <cite index="70-7">±0.05 mm</cite> | not verified |
| Overture PETG | not published (Vicat <cite index="35-3">85.1 °C</cite>) | not published | <cite index="31-2">±0.02 mm</cite> | <cite index="35-2">$14.99 sale, $22.99 list</cite> |

Prices move constantly, so check the live number. I've used maker or retailer prices rather than Amazon ones, and I'd rather leave a cell blank than guess. For a broader look at cost per kilo, see [how much filament costs](/posts/how-much-does-3d-printer-filament-cost/).

## Prusament PETG: the best-documented spec

Prusament's sheet is the most transparent here. It gives HDT of <cite index="1-8">68 °C at both 0.45 and 1.80 MPa</cite>, so there's no big drop as load increases. It also reports <cite index="2-8">tensile modulus of 1.5 to 1.6 GPa and elongation at yield around 5.1%</cite>.

The notched impact number is the useful warning. <cite index="1-8">Notched Charpy falls from 6 kJ/m² in the horizontal orientation to 3 kJ/m² in the vertical one</cite>. A sharp internal corner in a part loaded across the layers behaves differently from the unnotched "no break" headline.

Recommended settings are <cite index="1-8">250 ± 10 °C nozzle, 80 ± 10 °C bed, 50% fan, up to 200 mm/s</cite>. The cost is the issue: it's roughly double Bambu's refill price. Buy it when you want tight diameter control and predictable batches. Search: [Prusament PETG](https://www.amazon.com/s?k=Prusament+PETG&tag=mizubikes-web-20).

## Bambu Lab PETG Basic: strongest numbers per dollar

Bambu reformulated this filament, and the V3.0 sheet is a clear step up. It lists <cite index="87-9">tensile strength of 51 ± 1 MPa in X-Y, HDT of 71 °C at 0.45 MPa and 68 °C at 1.8 MPa, and a Tg of 69 °C</cite>. The old PETG HF, by comparison, <cite index="86-2">lists 34 MPa in X-Y</cite>, and <cite index="49-2">it has since been discontinued</cite>.

The Z axis is where you pay. The same sheet shows <cite index="89-11">35 ± 6 MPa across layers versus 51 MPa in-plane, and Z impact of 10.5 versus 34.2 kJ/m²</cite>. That's roughly a third lower tensile and two-thirds lower impact. Orient load paths along the layers.

Price is the draw. <cite index="41-3">Bambu cut refills to $13.99 in September 2026</cite>, and bulk tiers go lower, down to <cite index="40-2">$9.09 a roll at 10 or more</cite>. The drying spec is firm: <cite index="11-3">65 °C for 8 hours, storage under 20% RH</cite>. Search: [Bambu Lab PETG Basic](https://www.amazon.com/s?k=Bambu+Lab+PETG+Basic&tag=mizubikes-web-20).

## Polymaker: watch the version of the data sheet

Polymaker shows why you should check the TDS revision. An older PolyLite PETG sheet (v5.1) lists <cite index="27-3">Z tensile strength of 13.4 MPa against 31.9 in X-Y, with Z elongation of 1.3%</cite>. The later v5.4 values are <cite index="28-3">50.8 MPa X-Y and 42.8 MPa Z</cite>. Same product name, very different Z story, likely from different test prints.

Polymaker is also moving lines. <cite index="63-2">PolyLite PETG is being replaced by a faster successor, Polymaker PETG</cite>. Polymaker claims the new one reaches <cite index="67-6">45.71 MPa in Z, about 95% of its XY strength</cite>. That's a vendor claim from a marketing page, so I'd want to see the TDS before designing around it. The company puts HDT at <cite index="23-7">about 70 °C</cite> and recommends <cite index="23-4,23-5">240-260 °C nozzle and 60-70 °C bed</cite>. Search: [Polymaker PETG](https://www.amazon.com/s?k=Polymaker+PETG&tag=mizubikes-web-20).

## Overture, Elegoo and eSUN

Overture is a value pick, with a caveat. The store lists <cite index="35-3">layer adhesion of 45.7 ± 1.7 MPa and elongation of 9.3 ± 6.5%</cite>. That elongation scatter is large. It publishes Vicat softening, not HDT, and the figure varies by listing: <cite index="35-3">85.1 °C</cite> on one page, <cite index="38-8">75 °C</cite> on another for the transparent version. Its drying advice is <cite index="35-3">60 °C for 5 hours, with a warning that over-drying makes the filament brittle</cite>. Search: [Overture PETG](https://www.amazon.com/s?k=Overture+PETG&tag=mizubikes-web-20).

Elegoo Rapid PETG has the sharpest Z-axis penalty of the group. Its sheet shows <cite index="71-6">impact of 67.6 kJ/m² in X-Y versus 8.9 in Z, and tensile of 42 versus 28 MPa</cite>. It's tough in-plane and weak across layers, so orientation matters a great deal. Search: [Elegoo Rapid PETG](https://www.amazon.com/s?k=Elegoo+Rapid+PETG&tag=mizubikes-web-20).

eSUN's current sheet gives the lowest HDT here, <cite index="72-3">64 °C at 0.45 MPa</cite>. Its tolerance and Z figures are also the loosest of the group. I'd save it for light-duty parts. Search: [eSUN PETG](https://www.amazon.com/s?k=eSUN+PETG&tag=mizubikes-web-20).

## Print settings that matter for strength

Most brands cluster around a 230-260 °C nozzle and a 65-80 °C bed. For strength, print at the hotter end of the maker's range so the layers fuse, then control stringing with drying and retraction rather than by dropping temperature. Polymaker's older guidance even suggests <cite index="22-4">fan low for surface quality, off for better strength</cite>, which is worth testing on a bracket.

Dry every spool, even a new one. Bambu quotes <cite index="87-9">0.45% saturated water absorption</cite>, which is modest, but wet PETG steams, strings and bonds poorly between layers. Typical oven settings are 60-65 °C for 5-8 hours, depending on the maker.

Use a brass nozzle for plain PETG. Filled variants are different: Prusament's glow PETG, for example, <cite index="7-4">requires a hardened nozzle</cite>.

On speed, don't trust the maximum on the label. Community profile data lists about <cite index="29-2,29-3">15 mm³/s for PolyLite PETG</cite>, so a 300 mm/s claim doesn't mean structural quality at that flow.

## Design rules for PETG parts

Put the principal load along the layer lines. Tension across layers is the failure path, and the Z numbers above show how much strength you lose there. For clips and hooks, print them flat so the bend runs along the filament.

Use more perimeters instead of more infill. Walls carry the load, and infill mostly adds weight and print time. Add ribs and fillets at corners: the notched impact figures show how sharp corners hurt a tough material.

Use heat-set or threaded inserts for repeated fastening. PETG is tough, but a screw threaded straight into a printed hole can creep and loosen over time.

## When PETG is the wrong choice

Sustained load plus warmth is where PETG fails. <cite index="92-1,92-5">PETG suits moderate heat but not constant stress in a hot environment, and a part fine on a table may deform at 70-80 °C while holding weight</cite>. A closed car in summer <cite index="97-1">can reach roughly 70-85 °C</cite>. That's right at the limit of the HDTs above, so a loaded dashboard clip is a poor use.

Outdoor in full sun is the other case. For UV plus heat plus time, <cite index="92-4">ASA is usually the safer choice</cite>. Anything near a heater block, motor or power supply that gets hot should move to ABS, ASA or PC. PETG also isn't a bearing or wear material, and it's a poor fit for precise sliding fits, because it grips mating surfaces and softens with friction heat.

Where PETG fits well: brackets, enclosures, jigs and fixtures, shaded outdoor parts, snap fits and water-exposed housings that stay below about 60 °C.

## My picks

For most functional parts, Bambu PETG Basic is the best value on paper: the highest published X-Y tensile in the table and the lowest price. If you want the strongest Z-axis documentation and tight diameter control, Prusament is the most defensible choice, at a premium. Polymaker is worth buying once you've checked the current TDS revision. Overture suits non-critical parts when price matters most.

Whichever you buy, print a test bracket in your orientation and load it before committing.

## Sources

- https://www.prusa3d.com/file/3464616/prusament-petg-technical-data-sheet.pdf
- https://prusament.com/wp-content/uploads/2022/10/PETG_Prusament_TDS_2021_10_EN.pdf
- https://prusament.com/materials/prusament-petg-ultraglow/
- https://www.printedsolid.com/products/prusament-petg-1-75mm-1kg-jungle-green
- https://store.bblcdn.com/s1/default/cb94589bf7994fdcbfa833badefae9cd/Bambu_PETG_Basic_Technical_Data_Sheet.pdf
- https://us.store.bambulab.com/products/petg-basic
- https://forum.bambulab.com/t/filament-prices-drop-across-all-regions/259832
- https://www.goodprints3d.com/blogs/reviews/bambu-lab-petg-basic-review-a-mainstream-petg-lane-for-utility-parts-that-need-more-heat-margin-than-pla
- https://filamentcalcs.com/tools/material-comparison
- https://filamentpicks.com/bambu-petg-basic-vs-petg-hf/
- https://store.bblcdn.com/3a230e260a3a47c2b0db0156e07eef91.pdf
- https://incept3d.com/datasheets/polymaker-polylite-petg-v5.1.pdf
- https://www.spoolscout.com/data-sheets/polymaker/petg-polylite-petg
- https://shop.polymaker.com/products/polylite-translucent-petg
- https://us.polymaker.com/products/polylite-petg
- https://us-wholesale.polymaker.com/products/polymaker-petg
- https://polymaker.com/best-petg-filament-for-3d-printing-speed-strength-value/
- https://overture3d.com/products/overture-high-speed-petg
- https://www.spoolscout.com/product/B07SB761QR
- https://www.amazon.com/OVERTURE-Filament-Consumables-Dimensional-Accuracy/dp/B0991YSBDG
- https://www.spoolscout.com/data-sheets/elegoo/petg-rapid-petg
- https://www.esun3d.com/media/esun/catalog/certification/product/PETG/eSUN_PETG_Filament_TDS_1.pdf
- https://www.esun3d.com/petg-product
- https://3dprinterlab.net/guides/petg-filament-buying-guide-what-to-check-before-you-buy-for-3d-printing/
- https://3dfilamentprofiles.com/filament/details/121
- https://www.sovol3d.com/blogs/news/best-high-temperature-filament-functional-parts
- https://www.tripo3d.ai/blog/asa-vs-petg
