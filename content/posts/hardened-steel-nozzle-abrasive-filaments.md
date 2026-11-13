---
title: "Hardened Steel Nozzle: Which Filaments Need One?"
date: 2026-11-11
description: "Hardened steel nozzle guide: which filaments are abrasive (CF, GF, glow, metal-fill), what it costs in heat transfer, and when to skip it."
slug: hardened-steel-nozzle-abrasive-filaments
categories: ["Guides"]
tags: ["nozzles", "abrasive filament", "carbon fiber", "hotend"]
cover:
  image: "/images/hardened-steel-nozzle-abrasive-filaments-cover.webp"
  alt: "Close-up of a 3D printer hotend and nozzle extruding plastic onto a print bed"
  caption: "Photo: mebner1 / Pixabay"
  relative: false
draft: false
---

*MizuMakes may earn a commission from links in this post.*

You need a hardened steel nozzle whenever the filament contains hard particles: carbon fiber, glass fiber, glow-in-the-dark pigment, or metal fill. For plain PLA, PETG, ABS, ASA, and TPU you don't, and the harder nozzle won't improve print quality. One Prusa forum answer puts it plainly: hardened nozzles are only needed for abrasives and add no print quality over brass.

The real decision is how much abrasive filament you plan to run, and what you give up in heat transfer when you fit one.

## Do I need a hardened steel nozzle, or is stock fine?

The mechanism is simple. Carbon and glass fibers and hard pigments act like fine abrasives as they pass through the nozzle. Glass fiber is harder than brass, and the orifice slowly grows. Typical symptoms of a worn nozzle are creeping over-extrusion, more stringing, and dimensions that drift. For a part with a press-fit or a 0.2 mm clearance, that drift matters more than the cosmetics.

How fast it happens depends on who you ask, which is a good reason to treat the numbers as rough. One vendor claims a brass nozzle can open from 0.4 to 0.5 mm in as little as 50 hours with abrasives. Another puts brass failure at 1 to 3 kilograms of carbon fiber or glow filament. Either way, hardened steel isn't immortal. Even a hardened nozzle wears eventually with carbon fiber, just far more slowly than brass.

Bambu's stock nozzles matter here. The P1S ships with a stainless steel nozzle, and the X1C ships with a 0.4 mm hardened one. The P1 series also uses steel extruder gears that Bambu acknowledges can wear quickly on abrasive filament. So on a P1S, the nozzle is only half the upgrade. Our [P1S long-term review](/posts/bambu-p1s-review-1000-hours/) covers that machine's other limits.

## Which filaments are abrasive enough to require one?

Anything with "CF" or "GF" in the name is the obvious group. Bambu's own wiki goes further. It lists PLA-CF/GF, PETG-CF/GF, ABS-CF/GF, PA-CF/GF, PAHT-CF/GF, PET-CF/GF, PLA Marble, PLA Sparkle, and PLA Glow, and advises against stainless or brass for all of them.

| Filament type | Abrasive? | Nozzle guidance |
|---|---|---|
| PLA, PETG, ABS, ASA, TPU (unfilled) | No | Stock nozzle is fine |
| PLA-CF, PETG-CF | Yes | Hardened steel; Bambu approves its own for 0.4 mm, third-party filament suggests 0.6 mm |
| PA-CF, PAHT-CF, PET-CF, PA-GF | Yes, heavily | Hardened steel, 0.6 mm preferred |
| Glow-in-the-dark | Yes | The pigment is strontium aluminate; hardened steel |
| Metal-fill | Yes | Hardened steel |
| Wood-fill | Mildly | Less abrasive than carbon fiber, but still wears brass faster than plain PLA |

Glow filament is the one that catches people out because it looks like ordinary PLA. Some users get away with brass for an occasional accent piece, but for functional work you'd rarely print a glow part anyway. Pick the nozzle for the filament you'll run most, not the one-off.

## What does a hardened steel nozzle cost you in print quality?

Heat transfer. Hardened steel conducts only about 21 W/mK, so you print slower or run hotter to compensate. Prusa's guidance is to raise hotend temperature by roughly 5 °C, and another guide suggests 5 to 10 °C. Prusa also notes that some standard materials, ABS for example, can't be printed as fast through hardened steel.

On fast machines this shows up as under-extrusion at high volumetric flow. One guide says that mild under-extrusion can appear on high-flow printers with fast profiles. The fix is to cap flow rate for the filament, add 5 to 10 °C, or buy a high-flow hardened nozzle. One retailer lists Bambu's H2/P2S/X2D standard-flow hardened hotend at $21.99 and the high-flow version at $52.99. For CF materials printed at modest speeds, standard flow is usually enough.

Size also matters more than metallurgy for reliability. Bambu warns that fiber or particle-filled filament easily clogs a 0.2 mm nozzle, and strongly recommends a 0.6 mm hardened nozzle for CF and GF. A 0.6 mm nozzle also gives you thicker lines, which suits brackets and fixtures where Z-axis bonding between wide layers matters more than surface detail.

## How much does a hardened steel nozzle cost?

Prices vary a lot by platform, and they change, so check before ordering.

- **Bambu P1 series:** Bambu's US store listed a 0.4 mm hardened hotend at $14.99 and a complete hotend assembly at $34.99. The Hardened Steel Upgrade Combo for the P1 series was $43.98. That's the one to look at if you also need the extruder gears. [Search the combo here](https://www.amazon.com/s?k=Bambu+Lab+Hardened+Steel+Upgrade+Combo&tag=mizubikes-web-20) or a [P1 hardened steel hotend](https://www.amazon.com/s?k=Bambu+Lab+P1+hardened+steel+hotend&tag=mizubikes-web-20).
- **Prusa Nextruder printers:** The Prusa ObXidian 0.4 mm is hardened steel with a corrosion-resistant coating, listed at $52.90. The standard-flow E3D ObXiDian 500 was listed at $69.99, and E3D claims at least five times the wear resistance of ObXidian. That claim is the manufacturer's own, so I'd treat it as directional. Here's an [ObXidian 0.4 mm search](https://www.amazon.com/s?k=Prusa+Nozzle+ObXidian+0.4mm&tag=mizubikes-web-20).

A coated or tungsten-carbide nozzle only pays off at volume. One comparison suggests plain hardened steel gives the best cost per kilogram for regular abrasive use of about a kilogram a month or more. For occasional use, it's the cheap, sensible default.

## What changes in print settings for carbon fiber filament?

The nozzle is the easy part. Here are two Bambu data sheets that show how different CF materials are.

**PLA-CF** is the forgiving one. The TDS gives 210 to 240 °C for the nozzle and drying at 55 °C for 8 hours. But look at the mechanical numbers. Tensile strength is 38 MPa in the XY plane but 26 MPa in Z, and Z elongation at break is only 3.6%. The glass transition is 63 °C and the heat deflection temperature is 54 to 55 °C. So carbon fiber stiffens PLA but doesn't fix the weak layer bond or the low heat limit. A PLA-CF bracket in a hot car still creeps and sags. Orient it so the load runs along the layers, not across them.

**PAHT-CF** is the real engineering option. Bambu's data sheet calls for an 80 °C, 8 to 12 hour dry, a 260 to 290 °C nozzle, 80 to 100 °C bed, speed at or below 100 mm/s, and a 45 to 60 °C chamber. The heat deflection temperature is 194 °C at 0.45 MPa and 170 °C at 1.8 MPa, with 0.88% saturated water absorption. That makes it viable for hot-environment fixtures, which PLA-CF never will be. These are ideal-specimen figures, so expect less in a printed part, especially across layers.

Drying is the practical snag. The AMS 2 Pro tops out at 65 °C, short of the 80 °C PAHT-CF needs, while the AMS HT reaches 85 °C. Our [AMS vs AMS 2 Pro vs AMS HT comparison](/posts/bambu-lab-ams-vs-ams-2-pro-vs-ams-ht/) and the [filament drying guide](/posts/how-to-dry-filament-dryer-box-vs-dehydrator-vs-heated-bed/) cover the options. Also note the chamber requirement: a nozzle can't solve warping, which is why a heated chamber like the one on the [Prusa CORE One+](/posts/prusa-core-one-plus-heated-chamber-features/) matters for nylon CF.

## When you should skip a hardened steel nozzle

If your parts are PLA, PETG, ASA, or TPU, stay on the stock nozzle. Brass or stainless transfers heat better and gives you less to tune. A common compromise is to keep one nozzle for everyday work and a dedicated hardened one for abrasives, swapping when the material changes. Some people just run hardened for everything, which works if you're willing to add a few degrees. Prusa's own forum community is split on this, so either approach is defensible.

Also reconsider whether you need carbon fiber at all. If you need heat resistance, ASA or PETG often does the job without abrasive wear (see our [PETG brand comparison](/posts/best-petg-filament-brands-functional-parts/)). CF is for stiffness, dimensional stability, or matte finish, and for those jobs it's usually worth the nozzle.

A short checklist before loading a spool:

1. Read the label for CF, GF, glow, marble, sparkle, metal, or wood.
2. Check the manufacturer's nozzle recommendation, since some say 0.6 mm minimum.
3. Fit hardened steel (and steel gears if your extruder needs them) before the first print, not after.
4. Add 5 to 10 °C to your usual temperature and watch for under-extrusion.
5. Measure a calibration part periodically, since orifice wear shows up as dimensional drift.

## Sources

- [Bambu Lab Wiki: filament guide material table](https://wiki.bambulab.com/en/general/filament-guide-material-table)
- [Bambu Lab US Store: P1 series hotend](https://us.store.bambulab.com/products/bambu-hotend-p1-series)
- [Bambu Lab US Store: Hardened Steel Upgrade Combo](https://us.store.bambulab.com/products/hardened-steel-upgrade-combo)
- [Prusa Knowledge Base: E3D V6 nozzles for abrasive materials](https://help.prusa3d.com/article/e3d-v6-nozzles_920168)
- [Prusa: ObXidian 0.4 mm nozzle](https://www.prusa3d.com/product/prusa-nozzle-obxidian-4/)
- [Bambu PLA-CF technical data sheet](https://solidprint3d.ie/wp-content/uploads/2024/03/Bambu-PLA-CF_Technical-Data-Sheet.pdf)
- [Bambu PAHT-CF technical data sheet](https://manuals.plus/m/b651fbe3e43fdde811a411f36a995db31e7f734ec8653d933521f94c8ae7b4d5)
