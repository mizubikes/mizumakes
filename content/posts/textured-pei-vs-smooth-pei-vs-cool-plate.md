---
title: "Textured PEI vs Smooth PEI vs Cool Plate: Which to Use"
date: 2026-11-16
description: "Textured PEI vs smooth PEI vs cool plate: which build plate suits PLA, PETG, TPU, ABS and nylon, with bed temps and glue rules from the makers."
slug: textured-pei-vs-smooth-pei-vs-cool-plate
categories: ["Guides"]
tags: ["build plates", "PEI", "bed adhesion", "Bambu Lab"]
cover:
  image: "/images/textured-pei-vs-smooth-pei-vs-cool-plate-cover.webp"
  alt: "Bambu Lab Textured PEI Plate, a gold spring steel build plate with a textured PEI coating"
  caption: "Bambu Lab Textured PEI Plate"
  relative: false
draft: false
---

*MizuMakes may earn a commission from links in this post.*

For most functional printing, textured PEI is the plate to own. It holds PLA and PETG without glue, and it lets go on its own once it cools. In the textured PEI vs smooth PEI debate, smooth only wins when you need a flat, glossy underside, and it costs you glue and some risk with PETG. The cool plate family (SuperTack) is a PLA-first specialty surface, not a general-purpose one.

The naming below follows Bambu Lab's lineup, but the physics carries over to Prusa and most other spring-steel systems.

## Textured PEI vs smooth PEI: what actually differs

Both surfaces are PEI, and PEI grips plastic when it is hot and lets go as it cools. The difference is contact area. A smooth sheet gives the first layer a flat surface to wet out against, so adhesion is high. Prusa's own documentation says its smooth sheet grips some filaments, like TPU and PETG, so hard that they can damage the sheet when removed. Powder-coated sheets suit PETG, CPE and TPU, which tend to over-adhere to smooth surfaces but release more easily from textured ones.

The tradeoff is the same one you see in any adhesion problem. Smooth PEI also helps small footprints and sharp corners. Prusa notes that prints with sharp corners or a small first-layer area are less likely to detach on it. Textured PEI gives up a little of that holding power in exchange for forgiving release.

The specs differ too. Bambu's textured plate uses a 0.075 mm PEI powder coating on magnetic stainless steel, rated up to 180 °C. Its smooth plate used a 0.125 mm PEI sheet on spring steel, rated up to 120 °C. Neither rating limits you, since no bed you'd run on these plates goes past 110 °C.

There's also a supply change. Bambu's US store now says the Smooth PEI Plate for X1/P1/A1/P2S/X2D/H2 series is no longer available, and the Engineering Plate is the recommended replacement. A smooth plate remains for the A1 mini, and Bambu's Dual-Texture PEI plate still pairs a textured side with a smooth one. If you own an older smooth plate, the guidance below still applies. If you're buying new, expect to be choosing between textured, dual-texture, SuperTack and Engineering.

## Which plate for which filament?

The table uses Bambu's published settings for its own plates. Treat the bed temperatures as starting points, because slicer profiles vary by filament brand.

| Filament | Textured PEI | Smooth PEI | Cool Plate SuperTack |
| --- | --- | --- | --- |
| PLA | 45–60 °C, no glue | 45–60 °C, no glue | Designed for PLA; firm hold at a bed as low as 40 °C |
| PETG | 60–80 °C, no glue | 60–80 °C, glue stick or liquid glue | Listed for PETG; check the profile temperature |
| ABS / ASA | 90–100 °C, glue stick | 90–100 °C, glue | Not intended |
| TPU | 35–45 °C, no glue on 85A/90A | 35–45 °C, glue | Do not print TPU on it |
| PC / PA | 90–110 °C, glue stick | 90–110 °C, glue stick | Not intended |

The pattern is consistent. Textured PEI is the only plate where PLA, PETG and TPU all work without glue, and where the only glue requirements are the high-temperature engineering materials.

## Why does PETG tear smooth PEI?

PETG is the filament that makes people regret the smooth plate. Prusa's surface-prep guide says PETG bonds extremely well to a clean, degreased smooth PEI sheet, and removal often peels off the PEI and permanently damages the sheet.

The fix is a release layer. Prusa recommends either another type of steel sheet or PVA glue as a separation layer. The glue stick there is not an adhesive. It is a sacrificial film that fails before your plate does. Bambu's smooth-plate instructions say the same thing, telling you to apply glue to prevent the sheet from tearing with any filament other than PLA.

For PETG brackets, jigs and enclosures, the simple answer is a textured plate with a cooled-down removal. Bambu says prints come off easily once the bed reaches room temperature, and recommends waiting until it is 35 °C or lower. If you're choosing a PETG spool, our [PETG brand comparison](/posts/best-petg-filament-brands-functional-parts/) covers the data-sheet numbers, and [PLA vs PETG](/posts/pla-vs-petg/) covers when each material is the right call.

## Is the cool plate (SuperTack) worth it?

SuperTack is the successor to Bambu's original Cool Plate. It's built for PLA at low bed temperatures, which has real engineering value. A cooler bed means less thermal expansion mismatch, less warping on large PLA footprints, and a faster heat-up. It also leaves a smooth, matte bottom face. Bambu says the coating gives the underside a smooth, matte texture that blends in with other surfaces.

The limits matter for functional work:

- Bambu warns that TPU will damage the build plate.
- Bambu does not recommend its own PLA Silk on it, because strong adhesion may damage printed models.
- Organic solvents are out. Bambu says acetone will damage the SuperTack surface, so wash with warm soapy water rather than reaching for solvents.
- It's a consumable. Bambu says the plate degrades over time.

PETG on SuperTack is where sources disagree. Bambu's store lists the plate as designed for PLA and PETG. Third-party guides give different bed temperatures, from 55–60 °C to 70 °C, and users on Bambu's forum report mixed PETG results. I'd treat it as a PLA plate that sometimes handles PETG, and keep a textured plate for anything structural in PETG.

On price, Bambu's US store lists SuperTack at a typical $34.99, with frequent discounts. The [Bambu Cool Plate SuperTack](https://www.amazon.com/s?k=Bambu+Cool+Plate+SuperTack&tag=mizubikes-web-20) only pays off if PLA is a large share of your printing.

## What about ABS, ASA, nylon and PC?

These materials fail on plates for different reasons. They shrink more as they cool, so adhesion has to fight warping stress, and bed temperatures run 90–110 °C. That is why Bambu's glue guidance for them is stricter even on textured PEI. A glue stick here does double duty, helping the first layer hold and protecting the coating when you pry the part off.

The plate is only one part of the fix. Warping in ABS and ASA is mostly a chamber and draft problem, so use a brim and a closed enclosure, and don't expect any plate to beat thermal contraction on a large flat part. Our [ASA overview](/posts/what-is-asa-filament/) covers when to move from PETG to ASA for outdoor parts.

The Engineering Plate is Bambu's answer for this group. It's polyester powder on manganese steel with a 120 °C surface rating, and Bambu states that glue must be applied before printing any material on it. Treat it as the nylon and PC plate and not your daily driver. You can find it by searching for the [Bambu Lab Engineering Plate](https://www.amazon.com/s?k=Bambu+Lab+Engineering+Plate&tag=mizubikes-web-20).

## Which plate for functional parts?

The plate sets the quality of the bottom face, and that face often matters on a functional part. A few design rules follow.

For parts that mate or seal on the bottom, such as a bracket that sits flush on a surface, a smooth or Engineering plate gives a flatter face. A textured plate imprints its pattern into layer one. I couldn't find a published texture depth, so test-fit a sample piece before committing a tolerance-critical part to a textured plate.

For load-bearing parts, orient so the load doesn't pull layers apart, and don't count the plate-contact layer as extra strength. The plate affects first-layer adhesion and surface finish. It doesn't improve Z-axis strength.

For TPU and small-footprint parts, the textured plate with a low bed temperature is the safest combination for release. Our [TPU printing guide](/posts/tpu-printing-guide-settings-direct-drive-brands/) covers speeds and extruder requirements.

For mixed workflows, a dual-sided plate is a reasonable compromise. Bambu's [Dual-Texture PEI plate](https://www.amazon.com/s?k=Bambu+Lab+Dual-Texture+PEI+Plate&tag=mizubikes-web-20) has a textured PEI side and a smooth PEI side in one plate, with the smooth side following the same glue rules as above.

## How much do the plates cost?

Prices vary by printer size, and discounts are common, so use these as ballparks. Bambu's US store lists the textured plate from $15.99, against a typical price of $19.99, for the smallest size. Larger sizes such as the one for the P2S and X2D list at $34.99 typical. The remaining smooth PEI listing, for the A1 mini, is $21.99. You can compare current listings for the [Bambu Lab Textured PEI Plate](https://www.amazon.com/s?k=Bambu+Lab+Textured+PEI+Plate&tag=mizubikes-web-20) against the SuperTack above.

At these prices, the sensible approach is to buy a spare textured plate and swap between them. It's cheaper than ruining a plate with a stuck PETG part.

## Keeping plates working

Adhesion problems are usually contamination, not the wrong plate. Bambu's guidance for its dual-texture plate is to clean regularly with detergent and water, and to treat sanding with fine-grit paper as a restoration step for textured surfaces. Avoid solvents on SuperTack, and don't peel prints off a hot plate. Prusa also notes that its steel sheets are consumables, with coatings that diminish over time.

## Bottom line

Buy textured PEI first. It covers PLA, PETG and TPU without glue, and ABS, ASA, nylon and PC with a glue stick. Add SuperTack if you print a lot of PLA and want a cool bed and a clean underside. Use a smooth or Engineering plate when the bottom face matters, or when you're printing nylon or PC, and always put glue under PETG and TPU on the smooth ones. Check your slicer's plate setting before each print, since the bed temperatures change with the plate.

## Sources

- [Bambu Lab US store: Textured PEI Plate](https://us.store.bambulab.com/products/bambu-textured-pei-plate)
- [Bambu Lab US store: Smooth PEI Plate](https://us.store.bambulab.com/products/bambu-smooth-pei-plate)
- [Bambu Lab US store: Engineering Plate](https://us.store.bambulab.com/products/bambu-engineering-plate)
- [Bambu Lab: Cool Plate SuperTack](https://asia.store.bambulab.com/products/bambu-cool-plate-supertack)
- [Prusa Help: Print surface preparation](https://help.prusa3d.com/article/print-surface-preparation_686951)
- [Prusa Help: Smooth steel sheet](https://help.prusa3d.com/article/smooth-steel-sheet_196550)
