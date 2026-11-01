---
title: "PLA vs PETG vs ASA for Outdoor Prints: Pick by the Numbers"
date: 2026-11-01
description: "PLA, PETG, or ASA for outdoor parts? Compare glass transition, HDT, Z-axis strength, print settings, and price per kg from data sheets."
slug: pla-vs-petg-vs-asa-outdoor-prints
categories: ["Guides"]
tags: ["ASA", "PETG", "PLA", "outdoor prints", "filament"]
cover:
  image: "/images/pla-vs-petg-vs-asa-outdoor-prints-cover.webp"
  alt: "Enclosed desktop 3D printer printing a functional part"
  caption: "Photo: mebner1 / Pixabay"
  relative: false
draft: false
---

*MizuMakes may earn a commission from links in this post.*

Outdoor parts fail in three ways: they soften in the sun, they crack from UV and moisture over months, or they creep under a steady load until they sag. PLA, PETG, and ASA each handle those three differently. The data sheets let you rank them, even though no data sheet gives you a service life.

All the numbers below are manufacturer TDS values from ideal test specimens. Printed parts land lower, and the layer-to-layer (Z) direction lands lowest.

## The numbers side by side

| Property | PLA (Bambu PLA Basic) | PETG (Bambu PETG HF) | ASA (Bambu ASA) | ASA (Polymaker PolyLite) |
|---|---|---|---|---|
| Glass transition | 60 °C | 66 °C | not reported (Vicat 106 °C) | N/A in wiki table; ~98 °C on spec sheet |
| HDT at 0.45 / 1.8 MPa | 57 / 54 °C | 69 / 62 °C | 100 / 92 °C | 103 / 100 °C |
| Tensile, XY | 35 ± 4 MPa | 34 MPa | 37 ± 3 MPa | 43.8 MPa |
| Tensile, Z | not published | 23 MPa | not published | 32 MPa |
| Elongation at break, XY / Z | 12.2% / n/a | 8.6% / 5.1% | 9.2% / n/a | 6.7% / 1.65% |

The heat numbers decide most of this. PLA's glass transition sits around 60 °C, and sustained load above that point produces creep. Rapid Protos puts PLA's Tg at 55–65 °C, above which sustained load drives irreversible creep. PETG buys you about 10 °C. ASA buys you roughly 40 °C of headroom over PLA on the 0.45 MPa test.

## PLA: a temporary material outdoors

PLA has two problems outside, and they compound. The first is heat. A sun-baked cabin can reach PLA's 55–61 °C softening range, and a part in direct sun can run hotter than the air around it. The second is moisture. Elevated temperature plus humidity degrades PLA quickly through hydrolysis. A 2025 study of amorphous PLA found that it creeps significantly under small loads before much chemical degradation has happened.

UV is a third strike. Most comparisons rate PLA's UV resistance as poor, and one guide says outdoor PLA parts go brittle or discolor within months. I'd treat that as a rough guide, not a measured lifespan.

PLA is fine for a fit-check you'll carry outside for an afternoon, or a jig that lives in a shaded garage. It is the wrong choice for anything permanently mounted, load-bearing, or in direct sun.

## PETG: the sheltered-outdoor workhorse

PETG is a reasonable default for outdoor parts that don't see full sun. Its water resistance and impact behavior are good, and it prints without an enclosure. The weak spots are the thermal margin and UV. PETG is usually described as having moderate UV performance, and no TDS I found quantifies it, so the "moderate" label rests on general reporting.

The margin is thin. A Tg of 66 °C and an HDT of 62 °C at 1.8 MPa leave little room above a sun-heated surface. Bambu's PETG Basic V3 sheet lists a Tg of 69 °C and HDT of 68–71 °C, which is a small improvement and not a different class of material.

The Z axis is the other weak point. The PETG HF figures show 23 MPa tensile across layers versus 34 MPa in-plane, with elongation dropping from 8.6% to 5.1%. Orient parts so the load runs along the filament, not across layer lines. For brand-by-brand numbers, see [Best PETG Filament Brands for Functional Parts](/posts/best-petg-filament-brands-functional-parts/). For the indoor tradeoffs, see [PLA vs PETG](/posts/pla-vs-petg/).

One buying note: Bambu's store lists PETG HF as discontinued and not restocked once sold out. PETG Basic is the current alternative, and I'd compare any spool on its own TDS. A [Bambu PETG Basic](https://www.amazon.com/s?k=Bambu+Lab+PETG+Basic+1.75mm+1kg&tag=mizubikes-web-20) is a reasonable place to start.

## ASA: the one built for weather

ASA is the material designed for this. It is a modified ABS with an added acrylate component that improves weather adaptability and UV resistance. Thermally it is also in a different class. Bambu's sheet lists HDT of 100 °C at 0.45 MPa and 92 °C at 1.8 MPa, and Prusa says its ASA shows no deformation up to temperatures near 93 °C.

That makes ASA the choice for sun-exposed brackets, enclosures, vehicle-adjacent parts, and anything that has to hold a load on a hot day. I covered the PETG-to-ASA switch in [What is ASA Filament?](/posts/what-is-asa-filament/).

The cost is printability and Z-axis ductility. Polymaker's published data show 1.65% elongation across layers versus 6.7% in-plane, and Z tensile of 32 MPa versus 43.8 MPa. Different revisions of the same Polymaker sheet list different values (one revision gives 30.0 MPa Z tensile and 2.4% Z elongation), so read the version number. Either way, a part that fails across layers fails with almost no stretch. Design for it:

- Put the load in-plane.
- Add generous fillets and extra wall loops where a bracket meets a mounting boss.
- Use heat-set inserts or through-bolts with washers instead of printed threads that carry load.

## Print settings that matter

**PLA** is the easy one. Bambu lists 190–230 °C nozzle and 35–45 °C bed. Drying is 50 °C for 8 hours if the spool has been sitting out.

**PETG** (HF data) runs a 35–50 °C chamber range per the TDS and dries at 65 °C for 8 hours. Bambu says PETG HF must be dried before use for best quality.

**ASA** wants hot and enclosed:

- Bambu specifies 240–270 °C nozzle, 80–100 °C bed, under 250 mm/s, and drying at 80 °C for 8 hours.
- Retailer listings flag that an enclosed printer is required.
- Prusa recommends 260 ± 5 °C nozzle and 110 ± 5 °C bed for Prusament ASA, and notes significant warping that calls for higher ambient temperature.

ASA also contains styrene, so ventilate the enclosure. If you're choosing a machine mainly for ASA, a heated chamber helps with large parts. The [Prusa CORE One+ with its 55 °C chamber](/posts/prusa-core-one-plus-heated-chamber-features/) is the kind of printer I'd look at for that.

## What the filament costs

Prices move constantly, so treat these as snapshots. Bambu ASA was $29.99 per 1 kg spool at 3D Universe, while MatterHackers listed several colors at $46.99, so shop around. Best Buy listed Bambu PETG HF at $18.99. A Bambu price roundup put PLA at roughly $25 per kg. For live numbers, see [How Much Does 3D Printer Filament Cost?](/posts/how-much-does-3d-printer-filament-cost/).

On diameter tolerance, Bambu lists 1.75 mm ± 0.03 mm for its ASA. Since May 2024, Prusa lists ± 0.04 mm for Prusament ASA spools, widened from 0.03 because of a manufacturing change. Both are fine for functional work, but check the spool you actually receive.

ASA options worth comparing on their sheets:

- [Bambu Lab ASA](https://www.amazon.com/s?k=Bambu+Lab+ASA+filament+1.75mm+1kg&tag=mizubikes-web-20)
- [Prusament ASA](https://www.amazon.com/s?k=Prusament+ASA+filament+1.75mm&tag=mizubikes-web-20)
- [Polymaker PolyLite ASA](https://www.amazon.com/s?k=Polymaker+PolyLite+ASA+filament+1.75mm&tag=mizubikes-web-20)

## How I'd choose

If a part is in direct sun, carries a sustained load, or sits near a heat source, go straight to ASA. The extra $5–15 per kg is small next to the cost of reprinting a failed bracket.

If it's shaded or sheltered and needs water resistance, such as irrigation fittings, under-eave mounts, or planter hardware, PETG is a sensible compromise. Keep the load light and the temperature below its Tg, which is under 70 °C.

PLA stays indoors, or is a throwaway for short outdoor jobs.

None of the three tolerates a heavy sustained load near its softening point. HDT is a short-term test, so size the part with margin and expect creep over months. Choose ASA for the hot, loaded, sun-facing parts, and consider an annealing step or a different material if the part must hold tight tolerances. And if you're still weighing printers, the [P1S review](/posts/bambu-p1s-review-1000-hours/) covers an enclosed machine that can run ASA.

## Sources

- https://cdn.shopify.com/s/files/1/0584/7236/6216/files/Bambu_ASA_Technical_Data_Sheet.pdf?v=1690434954
- https://stemfinity.com/products/bambu-lab-pla-asa
- https://wiki.bambulab.com/filament-acc/abs-asa-pc/bambu_pla_basic_technical_data_sheet.pdf
- https://www.indus3design.com/en/3d-printing-materials/fff/bambu-lab-pla-basic/
- https://www.dynamism.com/bambu-lab/bambu-lab-pla-basic.html
- https://store.bblcdn.com/3a230e260a3a47c2b0db0156e07eef91.pdf
- https://3dfilamentprofiles.com/defaults/bambu-lab/petg/hf
- https://store.bblcdn.com/s1/default/cb94589bf7994fdcbfa833badefae9cd/Bambu_PETG_Basic_Technical_Data_Sheet.pdf
- https://us.store.bambulab.com/products/petg-hf
- https://wiki.polymaker.com/polymaker-products/more-about-our-products/documents/technical-data-sheets/abs-asa/polymaker-tm-asa
- https://polymaker.com/wp-content/uploads/lana-downloads/PolyLite_ASA_TDS_V5.3.pdf
- https://www.prusa3d.com/product/prusament-asa-filament/
- https://help.prusa3d.com/article/asa_1809
- https://www.sciencedirect.com/science/article/pii/S0141391025005804
- https://www.researchgate.net/publication/321263824_Weathering_degradation_performance_of_PLA_and_its_glass_fiber_reinforced_composite
- https://www.rapid-protos.com/pla-melting-point/
- https://knowdepot.com/3d-printing/will-pla-melt-in-a-hot-car/
- https://printpal.io/wiki/pla-complete-guide
- https://www.sovol3d.com/blogs/news/pla-vs-petg-vs-asa-for-outdoor-3d-printing-which-is-best
- https://shop3duniverse.com/products/bambu-lab-asa-1-75mm-1kg
- https://www.matterhackers.com/store/c/bambu-lab-asa-filament
- https://www.bestbuy.com/product/bambu-lab-1-75mm-petg-hf-filament-black/CZTZV9ZS24
- https://stacksheriff.com/3d-printing/bambu-lab-pricing/
- https://ultimate3dprintingstore.com/products/bambu-lab-asa-filament-1-75mm-1kg-red
