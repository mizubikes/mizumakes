---
title: "Best PETG Filament Brands for Functional Parts, Compared"
date: 2026-10-24
description: "Prusament, Bambu, Polymaker, Overture, Elegoo and eSUN PETG compared on data-sheet heat resistance, layer strength, tolerance and price per kg."
slug: best-petg-filament-brands-functional-parts
categories: ["Guides"]
tags: ["PETG", "filament", "functional parts", "material selection"]
cover:
  image: "/images/best-petg-filament-brands-functional-parts-cover.webp"
  alt: "FDM 3D printer printing a functional part on a heated bed"
  caption: "Photo: jaziaraujo / Pixabay"
  relative: false
draft: false
---

*MizuMakes may earn a commission from links in this post.*

Most PETG on the market is the same base polymer, so the differences between brands are smaller than the marketing suggests. What does vary is the heat deflection temperature (HDT), how much strength survives across layers, how tight the diameter is, and what a kilogram costs. Those four numbers matter more than the color range or the spool design.

This is a data-sheet comparison, not a bench test. Technical data sheet (TDS) numbers come from ideal specimens printed under each maker's own conditions. They are useful for ranking filaments against each other, but your printed part will land lower, especially in the Z direction.

## What actually separates PETG brands

**Heat.** PETG's glass transition sits close to where it starts to creep. Bambu lists <cite index="45-9">a 69 °C glass transition and 68/71 °C HDT (1.8/0.45 MPa)</cite> for PETG Basic. Polymaker's current sheet lists <cite index="25-3">81 °C Tg and 75/78 °C HDT</cite>. That 7 °C gap matters if the part lives near a motor or in a parked car. Neither number is a continuous service rating. A reviewer's reading of Bambu's sheet makes the same point: <cite index="47-10">it is not a 68–71 °C continuous service rating</cite>, because creep, restraint, and geometry still decide the outcome.

**Layer strength.** Compare the Z-axis number, not the headline XY tensile. Bambu's PETG Basic sheet shows <cite index="47-11">51 MPa XY against 35 MPa in Z, and notched-free impact of 34.2 versus 10.5 kJ/m²</cite>. A bracket loaded across layers has about two-thirds of the strength you read off the front page.

**Speed-tuned formulas cost strength.** Bambu's discontinued PETG HF listed <cite index="46-6">34 MPa XY and 23 MPa Z tensile</cite>, well below Basic. High-flow PETG exists to print fast, not to carry load. Reporting says <cite index="18-6">Bambu has since discontinued it</cite>, so verify before chasing remaining stock.

**Drying.** Every maker here says to dry. Polymaker suggests <cite index="21-8">65 °C for 6 hours</cite>, Elegoo and eSUN say 60 °C for 8 hours, and Overture says <cite index="57-2">60 °C for 5 hours and warns that drying longer can make it brittle</cite>. Saturated absorption is modest (Bambu lists <cite index="45-9">0.45%</cite> for Basic), but wet PETG strings and bubbles, and it bonds worse between layers.

## The numbers side by side

| Filament | HDT @ 0.45 MPa | Tensile XY / Z (MPa) | Diameter tolerance | Recent US price, 1 kg |
| --- | --- | --- | --- | --- |
| Prusament PETG | <cite index="3-8">68 °C</cite> | <cite index="3-8">47 / 50 (horizontal / vertical specimens)</cite> | <cite index="64-2">±0.02 mm</cite> | <cite index="60-4">$23.99 sale, $29.99 list</cite> |
| Bambu Lab PETG Basic | <cite index="45-9">71 °C</cite> | <cite index="47-11">51 / 35</cite> | Not found for Basic | <cite index="83-3">$22.99 spool</cite> (3D Universe), <cite index="81-3">$19.99 refill</cite> |
| Polymaker PolyLite PETG | <cite index="25-3">78 °C</cite> | <cite index="25-3">50.8 / 42.8</cite> | <cite index="21-9">±0.05 mm listed</cite> | <cite index="92-3">$19.99</cite> (B&H) |
| Elegoo Rapid PETG | <cite index="76-3">72 °C</cite> | <cite index="76-3">42 / not published</cite> | <cite index="69-3">±0.02 mm</cite> | <cite index="75-3">$13.99</cite> |
| Overture PETG | Not published | <cite index="55-9">47.9 / 45.7</cite> (via SpoolScout) | <cite index="48-2">±0.02 mm</cite> | <cite index="51-5">$14.99</cite> (Overture site) |
| eSUN PETG | <cite index="33-5">64 °C</cite> | <cite index="33-5">34.8 / 28.7</cite> | Not found | Not found |

Prices move weekly with sales, so use them for ranking, not budgeting. Prusa's "vertical" specimens are not a pure through-layer pull, and Prusa doesn't publish a clean Z tensile figure for standard PETG. Treat that 50 MPa as not comparable to Bambu's Z number.

## Brand by brand

### Prusament PETG: the tight-tolerance, well-documented pick

Prusa's sheet is the most complete of the group: <cite index="3-8">250 ± 10 °C nozzle, 80 ± 10 °C bed, up to 200 mm/s, 50% fan</cite>. The mechanical table includes flexural data and Charpy numbers. The notched Charpy values (<cite index="3-8">6 ± 1 kJ/m² horizontal and 3 ± 1 vertical</cite>) are a reminder that PETG is notch-sensitive. Don't design sharp internal corners on load paths.

The HDT is a modest 68 °C. You pay for consistency and a known profile, and it's the dearest filament in the table. Prusa also sells a UL-certified flame-retardant variant that suits <cite index="65-10">housings and insulating parts in electronics</cite>, but that one is $54.99.

[Prusament PETG on Amazon](https://www.amazon.com/s?k=Prusament+PETG+1.75mm+1kg&tag=mizubikes-web-20) is worth a search if you prefer it to ordering direct.

### Bambu Lab PETG Basic: the best published layer-strength story

The V3.0 sheet is a real step up from the earlier Basic formula. Older sheets showed <cite index="41-1">32 ± 4 MPa XY tensile</cite>, while V3.0 claims 51 MPa. It's the strongest XY number in the table and a decent 35 MPa in Z. If you run a Bambu printer, the RFID profile saves tuning time. Bambu's own data sheet says it is <cite index="45-7">still a good choice for outdoor accessories and functional tools</cite>.

The catch is the data sheet's chemical line. An older Basic TDS lists <cite index="41-1">no resistance to acid or alkali and none to some organic solvents</cite>. Don't put it in a fixture that sees cleaners or fuel.

[Bambu Lab PETG Basic on Amazon](https://www.amazon.com/s?k=Bambu+Lab+PETG+Basic+1.75mm+1kg&tag=mizubikes-web-20)

### Polymaker PolyLite PETG: the highest heat numbers

The current V5.4 sheet gives the best thermal figures here (81 °C Tg, 78 °C HDT at 0.45 MPa). It also reports <cite index="25-3">weak-acid resistance as good and strong acids and alkalis as poor</cite>, which is more specific than most makers bother to be.

Be careful with old data. An earlier V5.1 sheet listed Z tensile at <cite index="28-3">13.4 MPa</cite>, while V5.4 lists 42.8 MPa. Same product name, very different story. That's a good argument for checking the TDS revision and not trusting an aggregator's cached numbers. Print speed guidance on the older sheet is slow (30–50 mm/s), so expect to tune upward.

[Polymaker PolyLite PETG on Amazon](https://www.amazon.com/s?k=Polymaker+PolyLite+PETG+1.75mm+1kg&tag=mizubikes-web-20)

### Elegoo and Overture: cheap, and fine for non-critical parts

Elegoo's Rapid PETG lists <cite index="76-3">72 °C HDT, 42 ± 2 MPa tensile, and 8.9% elongation</cite> from a retailer's copy of the spec, with a <cite index="76-3">240–270 °C nozzle range</cite>. At $13.99 it is the cheapest filament here. The catch is that I found no Z-axis numbers.

Overture publishes a layer-adhesion figure of <cite index="52-3">45.7 ± 1.7 MPa</cite>, but I couldn't find a published HDT. Its Vicat figures also differ between pages, so I'd treat heat resistance as unverified. A buying guide that compared makers on published figures found Overture's <cite index="57-3">heat deflection and tensile values listed as not published</cite>. Use it for jigs, spacers, and covers, not parts that get warm.

[Elegoo Rapid PETG on Amazon](https://www.amazon.com/s?k=Elegoo+Rapid+PETG+1.75mm+1kg&tag=mizubikes-web-20) and [Overture PETG on Amazon](https://www.amazon.com/s?k=Overture+PETG+Filament+1.75mm+1kg&tag=mizubikes-web-20)

### eSUN PETG: read the TDS before buying

eSUN's July 2025 standard PETG sheet shows <cite index="33-5">34.77 MPa XY and 28.65 MPa Z tensile, with Izod impact of 4.86 XY versus 1.78 kJ/m² Z</cite>. It also lists applications as <cite index="33-5">prototype design, translucent models, and architectural decoration</cite>, not mechanical parts. The PETG+ product page does better at 70 °C HDT and is pitched at <cite index="30-4">mechanical jigs and structural housings</cite>. Treat those as separate products with separate numbers.

## Print settings that protect layer adhesion

Start with the maker's nozzle range, then bias hot. Prusa's 250 °C target is 10–20 °C above where many profiles default. Run the bed at 70–85 °C on PEI, and keep part cooling low: Prusa specs 50%, and a typical profile guide warns that <cite index="10-14">too much cooling weakens layer adhesion</cite>. For structural parts, I'd go lower than 50% and accept slightly rougher overhangs.

Plain PETG doesn't need a hardened nozzle, but the carbon- and glass-filled versions do. Elegoo recommends <cite index="72-3">a hardened steel nozzle in 0.4, 0.6, or 0.8 mm</cite> for PETG-CF.

## Design rules for PETG load-bearing parts

Orient the part so the main tensile and bending loads run along the layers, not across them. Use more perimeters (four or more) before adding infill, since walls carry most of the load. Pad sharp corners with fillets because of that notch sensitivity.

Budget for creep. With Tg in the high 60s to low 80s °C, a part under sustained load will deform well below its HDT. Keep clamps, spring tabs, and snap fits away from anything running warm, and size them for long-term strain rather than the first insertion.

For tolerances, a ±0.02 mm filament helps with flow consistency but doesn't replace calibrating your holes. Print a test coupon and set a hole-compensation value for your machine.

## When not to use PETG

Skip PETG for parts above roughly 60 °C in service, for sustained-load clamps near heat, and for anything seeing strong acids, alkalis, or solvents. For outdoor parts in direct sun, read [what ASA is and when to stop using PETG outdoors](/posts/what-is-asa-filament/). For a general comparison against PLA, see [PLA vs PETG](/posts/pla-vs-petg/). If your printer has an active chamber, the [Prusa CORE One+ breakdown](/posts/prusa-core-one-plus-heated-chamber-features/) covers what that opens up beyond PETG.

## What I'd buy

For a Bambu machine, PETG Basic is the one I'd choose on the numbers: the best XY strength and a respectable Z. For maximum heat margin, Polymaker's PolyLite has the best published HDT, provided you use the current TDS. For consistency and documentation, Prusament is the safe pick. For jigs, covers, and spacers, Elegoo and Overture at about $14 per kg are hard to argue with.

## Sources

- https://www.prusa3d.com/file/2765253/prusament-petg-technical-data-sheet.pdf
- https://prusament.com/wp-content/uploads/2022/10/PETG_Prusament_TDS_2021_10_EN.pdf
- https://www.prusa3d.com/category/prusament-petg/
- https://www.prusa3d.com/product/prusament-petg-pistachio-green-1kg-clearance/
- https://www.prusa3d.com/product/prusament-petg-v0-natural-1kg/
- https://store.bblcdn.com/s1/default/cb94589bf7994fdcbfa833badefae9cd/Bambu_PETG_Basic_Technical_Data_Sheet.pdf
- https://store.bblcdn.com/3a230e260a3a47c2b0db0156e07eef91.pdf
- https://www.goodprints3d.com/blogs/reviews/bambu-lab-petg-basic-review-a-mainstream-petg-lane-for-utility-parts-that-need-more-heat-margin-than-pla
- https://stacksheriff.com/3d-printing/bambu-petg-hf-review/
- https://www.scribd.com/document/1013020255/Bambu-PETG-Basic-Technical-Data-Sheet-b1d7a52e-Ddf4-47b3-8e3e-694084b5197e
- https://shop3duniverse.com/products/bambu-lab-petg-basic-1-75mm-1kg
- https://shop3duniverse.com/products/bambu-lab-petg-basic-1-75mm-1kg-refill
- https://www.poly-maker.jp/download/TDS/PolyLite_PETG_TDS_EN_V5.4.pdf
- https://incept3d.com/datasheets/polymaker-polylite-petg-v5.1.pdf
- https://www.matterhackers.com/store/l/polymaker-polylite-petg-3d-printer-filament/sk/MAW5MH42
- https://www.bhphotovideo.com/c/product/1809141-REG/polymaker_pb01041_polylite_petg_1_75mm_1000g.html
- https://www.esun3d.com/media/esun/catalog/certification/product/PETG/eSUN_PETG_Filament_TDS_1.pdf
- https://www.esun3d.com/petg-pro-product
- https://overture3d.com/products/overture-high-speed-petg
- https://overture3d.com/products/petg-3dprintingfilament
- https://www.spoolscout.com/product/B07SB761QR
- https://www.amazon.com/OVERTURE-Filament-Consumables-Dimensional-Accuracy/dp/B0991YSBDG
- https://3dprinterlab.net/guides/petg-filament-buying-guide-what-to-check-before-you-buy-for-3d-printing/
- https://us.elegoo.com/products/rapid-petg-filament-1-75mm-colored-1kg
- https://us.elegoo.com/products/petg-cf-filament-1-75mm-colored-1kg
- https://www.smith3d.com/shop/materials/petg/elegoo-petg/
- https://www.amazon.com/ELEGOO-Filament-30-600mm-Dimensional-Cardboard/dp/B0CPF7FDTG
- https://www.printlog3d.com/library/petg/prusament-petg-standard
