---
title: "TPU Printing Guide: Settings, Direct Drive, Brands"
date: 2026-11-13
description: "TPU printing guide with real settings: direct drive vs Bowden, retraction, speed, drying, and TDS-compared brands for functional parts."
slug: tpu-printing-guide-settings-direct-drive-brands
categories: ["Guides"]
tags: ["tpu", "flexible filament", "direct drive", "print settings"]
cover:
  image: "/images/tpu-printing-guide-settings-direct-drive-brands-cover.webp"
  alt: "Desktop 3D printer with a direct drive extruder printing a part"
  caption: "Photo: ZMorph3D / Pixabay"
  relative: false
draft: false
---

*MizuMakes may earn a commission from links in this post.*

The short answer for a TPU printing guide: use a direct drive extruder, print 95A TPU slowly (roughly 20–40 mm/s unless it is a high-flow grade), keep retraction near zero, and dry the spool before you start. Polymaker's own advice is to avoid a Bowden setup, because any large gap between extruder and hotend causes problems. Get those four things right and TPU is one of the more forgiving functional materials. Get one wrong and you get grinding, strings, or a jammed hotend.

Below are the settings, the mechanisms behind them, how to design for a material that stretches, and how the common brands compare on published numbers.

## What is TPU good for, and when should you not use it?

TPU is the answer when a part has to flex, absorb impact, resist abrasion, or seal. Think vibration mounts, bumpers, grommets, cable strain reliefs, gaskets, drive-belt-style pads, and protective sleeves. TPU resists abrasion, oils, and greases, and handles moderate temperatures of about -40 to 80 °C.

It is the wrong choice for anything that needs to hold position under sustained load. A flexible part creeps, and a clamp or locating feature made from it will drift. Compression set is the number to watch. BigRep's TPU 98A data lists 35% compression set at 23 °C and 42% at 70 °C. That is one industrial grade, not a universal figure, but it shows that even a firm TPU does not fully spring back after being squeezed. If a gasket has to stay sealed for years under constant compression, test it.

Heat is the other limit. Prusament's 95A lists an HDT of 78.6 °C at 1.80 MPa. For engine-bay or hot-enclosure parts, look at the numbers before committing, and keep stiff, hot parts in something like the materials covered in our [PETG brand comparison](/posts/best-petg-filament-brands-functional-parts/) or ASA.

## Do you need direct drive for TPU?

In practice, yes. TPU is soft and compressible, so the filament path matters. In a Bowden setup the long PTFE tube acts like a spring, compressing when you push or retract, which causes under-extrusion, stringing, and inconsistent flow. A direct drive extruder keeps that unsupported span short. Polymaker recommends a direct extruder with a gear-ratio mechanical advantage.

Bowden is not impossible with 95A or harder. One guide suggests sticking to 95A or harder and printing around 15–20 mm/s, with retraction minimized or off. Treat that as a workaround. Softer grades like 85A on Bowden are not worth the failed prints.

One more hardware note: unfilled TPU is not abrasive. SimplyPrint lists Bambu's TPU 95A HF as not abrasive. A brass nozzle is fine, and Prusa specifically recommends a 0.4 mm brass nozzle for its TPU. If you want to know when hardened steel actually matters, see [which filaments need a hardened steel nozzle](/posts/hardened-steel-nozzle-abrasive-filaments/).

## TPU printing guide: what settings actually work?

Start from the manufacturer's sheet, then slow down. Here is the baseline I would use for a standard 95A on a direct drive machine.

**Nozzle temperature:** 220–230 °C is the middle of most ranges. Bambu specifies 220–240 °C, Polymaker 210–230 °C, and Prusament 230 ± 10 °C. Don't chase stringing by running cold. One guide notes that lowering temperature too far hurts layer adhesion and causes delamination.

**Bed:** TPU sticks hard, so you rarely need much heat. Bambu's older 95A sheet calls for 30–35 °C with PVP glue as a release layer. Polymaker allows 25–60 °C. Prusament goes higher, at 65 ± 10 °C, on a PA nylon, PP, satin, textured, or smooth PEI sheet, and recommends a brim for very small or very large objects. Use a release layer on smooth PEI so you don't tear the surface when removing the part.

**Speed:** this is the setting that matters most. Polymaker lists 20–40 mm/s for standard PolyFlex TPU95. Prusament's sheet says up to 30 mm/s. Think in volumetric flow too. Bambu's own comparison puts standard TPU 95A at 3.6 mm³/s and the HF version at 12 mm³/s. Exceed what the filament can push and the extruder gear chews it.

**Cooling:** Prusament recommends 30–50% fan. That is enough to hold overhangs without chilling the layer bond.

**Retraction:** keep it small and slow. Standard PLA retraction of 5–6 mm at 40–60 mm/s can pull molten TPU into the cold zone, where it solidifies and jams. A common direct drive range is 0.5–1.5 mm at 20–30 mm/s. Note that the manufacturer sheets disagree: Polymaker lists 3 mm at 40 mm/s for direct drive. Run a retraction tower on your hotend rather than trusting either number. Disable Z-hop.

## How do you dry TPU?

TPU takes up moisture, and wet TPU shows up as pops, strings, and rough surfaces. Bambu's high-flow sheet gives 70 °C for 8 hours in a blast drying oven, or 80–90 °C for 12 hours on an X1-series heatbed. Polymaker also lists 70 °C for 8 hours. Some third-party guides say 50–55 °C for 4–6 hours, which is a gentler option if your dryer or spool is not rated for 70 °C. Bambu's spool material is rated to 90 °C, but a generic spool may not be, so check before you cook it. Details on equipment are in our [filament drying comparison](/posts/how-to-dry-filament-dryer-box-vs-dehydrator-vs-heated-bed/).

Prusament is the exception. Its data sheet reports 0.02% moisture absorption in 24 hours and 0.04% in 7 days. Prusa still says drying may be needed in high-humidity storage.

## How do you design a TPU part?

TPU stiffness depends heavily on geometry. Wall count and infill set the feel of the part: Bambu notes that lower infill increases flexibility. Use thick walls and high infill for a bumper that must stay firm, and thin walls with gyroid or low infill for a part that should compress.

Orientation is where I would not trust marketing. Some guides claim TPU bonds well layer to layer and gives good isotropic strength. The data for Bambu's firmer 68D grade, as transcribed by filamentdb, shows a different picture: tensile strength of 22.4 MPa in X-Y versus 11.2 MPa in Z. Elongation at break drops from 650% to 31% in Z, and notched Charpy impact falls from 124.3 to 9.6 kJ/m². That is one grade, so don't assume the same for a 95A, but it is a good reason to align the main tensile load with the layer plane and not across layers.

Tolerances: print holes slightly undersized and test, since a soft part grips whatever it surrounds. Skip threaded features that need real torque. Use heat-set inserts only in a rigid mating part, and clamp TPU between plates and fasteners instead.

## Which TPU brand should you buy?

Published numbers are measured on molded or ideal printed specimens, and the methods differ by brand, so treat the table as a rough guide, not a ranking.

| Filament | Hardness | TDS tensile / elongation | Nozzle | Speed guidance | Price (1 kg unless noted) |
|---|---|---|---|---|---|
| Bambu TPU 95A HF | 95A | 27.3 MPa / >650% | 220–240 °C | under 200 mm/s | $41.99 list |
| Bambu TPU for AMS | 68D | 22.4 MPa / >650% | 220–240 °C | up to 238 mm/s | $38.99 |
| Polymaker PolyFlex TPU95 | 95A | n/a / 551% | 210–230 °C | 20–40 mm/s | not verified |
| Polymaker TPU95-HF | 95A | 26.6 MPa / 496% | 200–230 °C | 30–100 mm/s | not verified |
| Prusament TPU 95A | 95A | n/a / n/a (HDT 78.6 °C) | 230 ± 10 °C | up to 30 mm/s | $34.99 per 500 g at launch |
| Overture TPU 95A | 95A | 30.1 MPa / 332% | 210–230 °C | max about 40 mm/s | $22.99 |

Sources for the table: Bambu's HF sheet, Bambu's AMS-grade comparison, its tensile figure, Polymaker's HF sheet, Overture's TDS, and a profile database for Overture's speed and temperature range. Bambu's US store lists TPU for AMS at $38.99, and TPU 95A HF at $41.99. Overture's own store lists its standard 1 kg TPU at $22.99. The Prusament price is only the launch figure; $34.99 for a 500 g spool may have changed.

**Bambu TPU 95A HF** is the pick if you want speed. The 12 mm³/s figure is more than three times the standard grade. The catch: Bambu says all AMS units are not compatible with it. If you need TPU through an AMS, the separate TPU for AMS is rated for 18 mm³/s, but it is a stiffer 68D material, so it won't give a soft 95A feel. See our [AMS vs AMS 2 Pro vs AMS HT breakdown](/posts/bambu-lab-ams-vs-ams-2-pro-vs-ams-ht/) if you are weighing multi-material setups. [Search Bambu TPU 95A HF on Amazon](https://www.amazon.com/s?k=Bambu+Lab+TPU+95A+HF&tag=mizubikes-web-20).

**Polymaker PolyFlex** has the most useful documentation. It lists both direct and indirect-drive retraction settings, and the HF version stretches the speed range to 100 mm/s. Polymaker also says the HF grade has UV resistance. [Search Polymaker PolyFlex TPU95 on Amazon](https://www.amazon.com/s?k=Polymaker+PolyFlex+TPU95&tag=mizubikes-web-20).

**Prusament TPU 95A** is the one for chemical and cold exposure. Its polymer is an ether-diol type, unlike the ester type in most TPU filaments. That trades some oil resistance for hydrolysis and microbial resistance; Wikipedia's comparison table rates ether-based TPU higher for hydrolysis, microbial, and low-temperature performance, and ester-based higher for chemical resistance. Prusa also states a diameter tolerance of 0.06 mm, which is looser than Bambu's ±0.03 mm, though Prusa argues most competitors don't hold their claimed numbers. [Search Prusament TPU 95A on Amazon](https://www.amazon.com/s?k=Prusament+TPU+95A&tag=mizubikes-web-20).

**Overture and SUNLU** are the budget picks. Overture's TDS shows 30.1 MPa tensile and 332% elongation, so it is firmer and stretches less than the others listed above. SUNLU's store shows TPU at $17.99 on sale against a $22.95 regular price, but I could not find a SUNLU data sheet with mechanical values, so I can't compare it on numbers. For general use like feet, bumpers, and spacers, both are reasonable. For parts where you need documented properties, pay for the brand that publishes them. [Search Overture TPU 95A on Amazon](https://www.amazon.com/s?k=Overture+TPU+95A+Filament&tag=mizubikes-web-20) or [SUNLU TPU 95A](https://www.amazon.com/s?k=SUNLU+TPU+95A+Filament&tag=mizubikes-web-20).

## What goes wrong most often with TPU?

Grinding or a clogged feed path usually means speed or flow is too high, or the idler tension is too tight. Strings and bubbles mean wet filament, so dry it before you touch retraction. Soft, blobby corners mean the extruder is pushing filament that has nowhere to go; lower speed and use the filament's real volumetric limit as your cap. Warping is generally mild, but Prusa notes large TPU prints tend to warp, so add a brim on big flat parts.

After that, test the part under the real load. Stretch it, compress it for a week, and heat it if that applies. Data sheet numbers will tell you which brand to try. Only your own part will tell you whether it works.

## Sources

- [Bambu Lab US store: TPU 95A HF](https://us.store.bambulab.com/products/tpu-95a-hf)
- [Bambu TPU 95A HF technical data sheet (V1.0)](https://store.bblcdn.eu/s8/default/16df21baf482453999b3dbb61cc110e7/Bambu_TPU_95A_HF_Technical_Data_Sheet.pdf)
- [Polymaker wiki: PolyFlex TPU95 data sheet](https://wiki.polymaker.com/polymaker-products/more-about-our-products/documents/technical-data-sheets/tpu/polyflex-tm-tpu95)
- [Prusament TPU 95A technical datasheet](https://3d.nice-cdn.com/upload/file/prusament-tpu-95a-technical-data-sheet[0].pdf)
- [Overture TPU technical data sheet](https://midlands3d.com/wp-content/uploads/2025/06/TPU-95A-Technical-Data-Sheet.pdf)
- [filamentdb: Bambu TPU 68D mechanical properties (X-Y vs Z)](https://filamentdb.app/filament/bambu-lab/tpu-for-ams-68d)
