---
title: "PCTG vs ASA vs PETG for Functional and Outdoor Parts"
date: 2026-11-15
description: "PCTG vs ASA vs PETG compared on data-sheet heat deflection, impact, UV and chemical resistance, printability, and cost per kg, plus who should pick which."
slug: pctg-vs-asa-vs-petg
categories: ["Guides"]
tags: ["PCTG", "ASA", "PETG", "filament comparison"]
cover:
  image: "/images/pctg-vs-asa-vs-petg-cover.webp"
  alt: "FDM 3D printer printing a functional part on the build plate"
  caption: "Photo: ZMorph3D / Pixabay"
  relative: false
draft: false
---

*MizuMakes may earn a commission from links in this post.*

In a PCTG vs ASA vs PETG decision, the split is simple. ASA is for parts that live in sun and heat. PCTG is for parts that get hit, flexed, or wiped down with chemicals indoors. PETG is for everything that doesn't need either. They aren't interchangeable. Each one wins on a different property, and the data sheets show where.

The usual caveat applies. TDS numbers come from ideal specimens, and printed parts land lower, especially across layers (the Z axis). I'll use TDS values for a like-for-like comparison, then add independent printed-part tests where they exist.

## PCTG vs ASA vs PETG: what do the data sheets say?

These are representative data-sheet values. PETG is Bambu PETG HF, ASA is Bambu ASA, and PCTG is Fiberlogy PCTG. Other brands vary, so check the sheet for the spool you actually buy.

| Property | PETG (Bambu PETG HF) | PCTG (Fiberlogy) | ASA (Bambu) |
|---|---|---|---|
| HDT | 69 °C | 76 °C @ 0.45 MPa, 64 °C @ 1.8 MPa | 100 °C |
| Tensile strength | 34 MPa | 43 MPa (yield) | 37 MPa |
| Elongation at break | 8.6% | 220% | 9.2% |
| Flexural modulus | 2050 MPa | 1600 MPa | 1920 MPa |
| Impact (TDS) | 31.5 kJ/m² unnotched, 6.2 notched | 92 kJ/m² notched Izod | 41 kJ/m² (notch not stated) |
| Nozzle / bed | 230–260 / 65–75 °C | ~250–280 °C (3D-Fuel) | 240–270 / 80–100 °C |

Sources for the table: the PETG HF sheet lists an HDT of 69 °C, tensile strength of 34 MPa, elongation of 8.6%, and flexural modulus of 2050 MPa. The notched figure is 6.2 kJ/m², per the Bambu sheet. For PCTG, Fiberlogy lists 64 °C HDT at 1.8 MPa, 76 °C at 0.45 MPa, 43 MPa tensile yield, 92 kJ/m² notched Izod, 1600 MPa flexural modulus, and 220% elongation at break. For ASA, Bambu's sheet gives 100 °C HDT, 106 °C Vicat, 37 MPa tensile, 9.2% elongation, 1920 MPa bending modulus, and 41 kJ/m² impact strength.

Two takeaways. First, PCTG's HDT is only a few degrees above PETG's. It is not a heat upgrade. Second, the elongation at break gap (220% vs under 10%) is the real signature of PCTG. It yields and stretches instead of snapping.

## Is PCTG actually tougher than PETG and ASA?

Yes, but the TDS headline number overstates it. A 92 kJ/m² notched Izod is a data-sheet figure, and printed parts don't get close. In independent testing of an Essentium PCTG, CNC Kitchen measured 24 kJ/m² on the notched impact test, well past PETG and level with ABS. In a separate article, PETG measured 8.6 kJ/m² and ASA 18 kJ/m². Those are different tests on different brands, so treat the ranking as directional: PCTG > ASA > PETG for impact.

Orientation matters here too. The same PCTG test found that samples printed standing averaged only 1.5 kJ/m². Layer adhesion is better than most filaments, with 38 MPa standing and about 75% of flat strength. But impact across layers is still the weak axis. Orient the part so that impact loads cross the layers in the XY plane, not along Z.

For comparison, CNC Kitchen measured ASA layer adhesion at only 29% of flat strength, against 46% for PETG. ASA's toughness in the data sheet doesn't rescue a part printed with cold layers.

PCTG isn't a free win everywhere. One reviewer's oven and creep tests found that PETG deformed less overall in the creep test, though PCTG crept more slowly from the second day. For a bracket under sustained load, none of these three is a good choice. Use a stiffer, higher-Tg material or add metal.

## Which handles heat better: PCTG, ASA, or PETG?

ASA, clearly. Prusa says its ASA shows no signs of deformation up to temperatures near 93 °C, and Bambu's TDS lists 100 °C HDT. PCTG's Tg is around 84–85 °C and its HDT is 76 °C at light load, falling to 64 °C at 1.8 MPa.

Independent tests disagree on PCTG. CNC Kitchen reported that it goes soft at 80 °C. A separate oven test found PETG deformed around 73 °C while PCTG held until roughly 100 °C. Specimen geometry, load, and grade all matter. I'd design to the TDS number and leave margin. For anything in a closed car in a California summer, ASA is the safe choice.

## Which is best for outdoor use: UV and chemical resistance

ASA's UV advantage is chemical. Its acrylate rubber has no double bonds, which gives about ten times the weathering resistance of ABS. PETG isn't built for this and chalks and embrittles over seasons. PCTG sits in between. 3D-Fuel reports that after 2,000 hours of accelerated weathering its Pro PCTG held its color about twice as well as its own Pro PETG. That is vendor data, not independent testing. A part supplier is blunter: PCTG is not UV-stabilized and isn't the right choice for permanent outdoor service. Even 3D-Fuel says ASA is still the right call for years in full sun.

Chemicals flip the ranking. In Prusa's soak tests, ASA does not resist acetone, and PETG lost strength after a week in ethanol, IPA, and acetone. PCTG is reported to be more resistant. 3D-Fuel says its soak tests showed no cracking in isopropyl alcohol or ethanol and no swelling in engine oil or hydraulic fluid. Again, that is vendor testing. If a part sees solvents, run a soak test on your own prints under realistic strain, because stress cracking depends on load.

For a broader look at when PETG falls short outdoors, see [PLA vs PETG vs ASA for outdoor prints](/posts/pla-vs-petg-vs-asa-outdoor-prints/) and [what ASA filament is and when to switch](/posts/what-is-asa-filament/).

## How hard are they to print? Enclosure, warping, and fumes

PETG is the easy one. Bambu's TDS gives 230–260 °C nozzle, 65–75 °C bed, and an 8-hour, 65 °C drying cycle. It prints in an open frame with a cooling fan at moderate speeds.

PCTG is billed as PETG-like. 3D-Fuel states it prints at 250–280 °C without an enclosure. Expect a hotter nozzle than PETG, and slow the part-cooling fan to protect layer bonding. One vendor recommends a fan of about 20–50%, and CNC Kitchen's best layer-adhesion number used 10%. Reports on warping conflict. One guide warns that PCTG shrinks more as it cools, and a service bureau says it needs the same controlled process as ASA for production work. For large, flat parts, I'd budget for brims, a warm chamber, and a test print before committing.

ASA is the hard one. Prusa lists 260 °C nozzle, 110 °C bed, an enclosure requirement, and a styrene warning. They also recommend good ventilation or an enclosure with active filtration. Bambu's range is a bit more forgiving at 240–270 °C nozzle and 80–100 °C bed, with an 80 °C, 8-hour drying cycle. See [how to dry filament](/posts/how-to-dry-filament-dryer-box-vs-dehydrator-vs-heated-bed/) for the options. Small ASA parts can print open-air. Large ones warp and crack between layers without chamber heat.

None of the three needs a hardened nozzle in plain form. Carbon-fiber blends of any of them do. [Hardened steel nozzle guide](/posts/hardened-steel-nozzle-abrasive-filaments/).

## What do they cost per kg?

Prices move constantly, so treat these as a snapshot from mid-November 2026.

- PETG is the cheapest, with roundups putting Sunlu at $14–18 and Overture at $16–20 per kg.
- ASA runs wide. Bambu's list price is $29.99 for 1 kg (it is often discounted), while a price tracker shows an Elegoo ASA 1 kg spool at $16.99.
- PCTG is the premium. 3D-Fuel's US-made Pro PCTG lists at $29.95 per 1 kg spool in common colors, and one roundup puts US makers' stores at $28.95–$34.99 per kg.

The PCTG premium over PETG is roughly $10–15 per kg. For a bracket that uses 50 g, that is under a dollar. Cost shouldn't decide this choice. Failure modes should.

## Who should pick which?

**Pick PETG** for indoor brackets, enclosures, jigs, and fixtures that see light loads, mild heat under about 60 °C, and no impacts. It is also the cheapest choice. I covered brands in [best PETG filament brands for functional parts](/posts/best-petg-filament-brands-functional-parts/). Try [Overture PETG](https://www.amazon.com/s?k=Overture+PETG+filament+1.75mm&tag=mizubikes-web-20) for a low-cost starting point.

**Pick PCTG** for parts that get dropped, snapped on, or flexed. Think snap fits, clips, tool holders, protective covers, and parts wiped with IPA or exposed to oils. It is not a hot-environment material and not for sustained load. Options include [Fiberlogy PCTG](https://www.amazon.com/s?k=Fiberlogy+PCTG+filament&tag=mizubikes-web-20) and [3D-Fuel Pro PCTG](https://www.amazon.com/s?k=3D-Fuel+Pro+PCTG+filament&tag=mizubikes-web-20).

**Pick ASA** for anything outdoors for years, in a hot car, or near a heat source. Examples are sensor housings, mounts, and trim. You need an enclosure and ventilation, and you should avoid solvent exposure. [Bambu Lab ASA](https://www.amazon.com/s?k=Bambu+Lab+ASA+filament&tag=mizubikes-web-20) and [Elegoo ASA](https://www.amazon.com/s?k=Elegoo+ASA+filament+1.75mm&tag=mizubikes-web-20) are common choices. Pick on the TDS and diameter tolerance, not the color chart.

If you have no enclosure and need outdoor use, PCTG is a reasonable compromise for shaded or seasonal parts. For permanent full-sun service, it isn't.

## Sources

- [Fiberlogy PCTG technical specifications](https://fiberlogy.com/en/product/pctg-filament-s2/)
- [Bambu PETG HF data sheet values (Crea3D mirror of TDS)](https://www.crea3d.com/en/filaments/1537-bambu-petg-hf.html)
- [Bambu ASA data sheet values (Crea3D mirror of TDS)](https://www.crea3d.com/en/filaments/1306-bambu-asa.html)
- [CNC Kitchen: Essentium PCTG review](https://www.cnckitchen.com/blog/essentium-pctg-review)
- [Prusament ASA product page](https://prusament.com/materials/prusament-asa/)
- [Prusament: chemical resistance of 3D printing materials](https://prusament.com/chemical-resistance-of-3d-printing-materials/)
- [3D-Fuel PCTG guide](https://www.3dfuel.com/pages/pctg)
