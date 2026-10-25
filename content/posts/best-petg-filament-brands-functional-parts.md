---
title: "Best PETG Filament Brands for Functional Parts, by the Numbers"
date: 2026-10-24
description: "Prusament, Bambu Lab, Polymaker, eSUN and Overture PETG compared on data-sheet HDT, layer strength, tolerance and price for load-bearing parts."
slug: best-petg-filament-brands-functional-parts
categories: ["Guides"]
tags: ["PETG", "filament", "functional parts", "material selection"]
cover:
  image: "/images/best-petg-filament-brands-functional-parts-cover.webp"
  alt: "Spools of 3D printer filament stacked on a workshop shelf"
  caption: "Photo: Pexels / Pixabay"
  relative: false
draft: false
---

*MizuMakes may earn a commission from links in this post.*

Picking a PETG brand for a bracket, jig, or enclosure is mostly a question of three numbers: how much of the in-plane strength survives across layers, how close the heat deflection temperature (HDT) is to your operating temperature, and how consistent the diameter is. Color selection and spool art don't matter much.

This guide compares the data sheets of the PETG brands people actually buy. If you're still deciding between PETG and PLA, start with [PLA vs PETG](/posts/pla-vs-petg/).

## Read the data sheet with some suspicion

TDS values come from ideal specimens, and every vendor uses its own method. Printed parts land lower, especially across layers (Z).

The eSUN PETG+HS data sheet, for example, says its properties come from injection-molded splines, not printed coupons. <cite index="74-4">The physical, mechanical, thermal, and electrical values there are based on injection molding spline tests.</cite> That makes them a poor guide to printed layer strength.

So compare like with like. Look for X-Y versus Z tensile numbers, and treat any single headline "strength" figure as marketing until you can see the specimen orientation.

## The numbers side by side

Prices are US list prices I found and move around with sales. HDT is at 0.45 MPa unless noted.

| Filament | HDT | Tensile X-Y / Z (MPa) | Diameter tolerance | US price (1 kg) |
| --- | --- | --- | --- | --- |
| Prusament PETG | <cite index="3-8">68 °C (same at 1.8 MPa)</cite> | <cite index="3-8">47 horizontal / 50 vertical xz</cite> | <cite index="3-8">±0.02 mm</cite> | <cite index="51-3">$29.99</cite> |
| Bambu Lab PETG Basic (V3.0) | <cite index="47-8">71 °C (68 °C at 1.8 MPa)</cite> | <cite index="47-8">51 / 35</cite> | <cite index="82-4">±0.03 mm</cite> | <cite index="82-5">$13.99 refill; $16.99 with spool</cite> |
| Polymaker PETG (new formula) | <cite index="29-9">69 °C (65 °C at 1.8 MPa)</cite> | <cite index="60-5">47.96 / 45.71</cite> | not found | <cite index="29-5">$19.99</cite> |
| eSUN PETG-Basic | <cite index="71-4">73 °C</cite> | <cite index="71-4">68.41 / 35.84</cite> | not found | not found |
| Overture PETG | Vicat <cite index="38-4">85.1 °C</cite>; no HDT found | not published where I looked | <cite index="32-5">±0.02 mm claimed on Amazon</cite> | <cite index="32-2">$17.99 on Amazon</cite> |

Two things stand out. HDT barely varies across brands, and the table gives you no reason to expect a part to survive past the high 60s °C. Layer strength is where the brands separate.

## Prusament PETG: tight tolerance, documented layer bond

Prusa publishes more than most. The data sheet lists <cite index="3-8">interlayer adhesion of 18 ± 4 MPa</cite> next to a ±0.02 mm diameter tolerance. Prusa's print recommendations are <cite index="3-8">250 ± 10 °C nozzle, 80 ± 10 °C bed, and a 50% fan</cite>.

Prusa's own test numbers show how much the notch matters. <cite index="3-8">Notched Charpy impact is 6 ± 1 kJ/m² horizontal and 3 ± 1 vertical.</cite> A sharp internal corner in a PETG bracket will behave far more brittlely than the unnotched "no break" result suggests, so add fillets.

The cost is price. At <cite index="51-3">$29.99 list</cite>, it's roughly double Bambu's list price. I'd pay it for parts where fit matters, such as sliding fits, bearing seats, and press-fit inserts, because the tolerance is the tightest of the group. For a shop-floor jig, it's overkill.

## Bambu Lab PETG Basic: strong on paper, cheap, and dry-sensitive

The V3.0 sheet is a notable upgrade. Bambu says the formula was <cite index="47-5">upgraded to deliver PLA-level strength while keeping its toughness</cite>. The sheet shows <cite index="47-8">51 ± 1 MPa X-Y tensile against 35 ± 6 MPa in Z</cite>, so across-layer strength is roughly 70% of in-plane. It lists <cite index="47-8">0.45% saturated water absorption</cite>, which is the number to remember when deciding how seriously to dry it.

The older PETG HF is a different story. One third-party data aggregator lists HF at <cite index="17-13">34 MPa X-Y and 23 MPa Z tensile</cite>. A recent review also advises against paying a premium for <cite index="19-6">remaining HF stock</cite>. If you're buying for load-bearing parts, Basic is the one to look at.

Bambu's own guidance is to dry before use. For HF, the data sheet specifies <cite index="18-9">65 °C for 8 hours in a blast oven</cite>, and I'd apply the same to Basic. Wet PETG strings and bonds poorly between layers, which is the exact axis you're worried about. Bambu PETG Basic is the pick if you run an AMS and want a cheap general-purpose spool: [Bambu Lab PETG Basic](https://www.amazon.com/s?k=Bambu+Lab+PETG+Basic+1.75mm+1kg&tag=mizubikes-web-20).

## Polymaker PETG: the best published Z-axis number

Polymaker's new formula is the one to look at if layer adhesion drives your design. Its shop listing shows <cite index="60-5">47.96 MPa X-Y and 45.71 MPa Z tensile</cite>, which Polymaker itself frames as <cite index="62-7">95% of in-plane strength</cite>. Bending strength tells a less flattering story: <cite index="60-5">80.08 MPa X-Y versus 57.65 MPa Z</cite>. Tensile coupons at 100% infill flatter a layer bond, so I'd still design for the bending number.

Two notes. The older PolyLite PETG line was reportedly <cite index="28-5">discontinued except for the translucent</cite>, so old data sheets with 75 °C+ HDT figures don't describe the current product. And Polymaker itself says the new filament is <cite index="64-6">fairly hygroscopic</cite>, so dry it. [Polymaker PETG](https://www.amazon.com/s?k=Polymaker+PETG+1.75mm+1kg&tag=mizubikes-web-20) runs about <cite index="28-6">$19 per kilogram</cite>.

## eSUN and Overture: value spools with caveats

eSUN's PETG-Basic page shows an <cite index="71-4">HDT of 73 °C</cite> and the best-looking X-Y tensile number in the table, but I couldn't confirm the specimen method. The Z value of 35.84 MPa is the more useful figure, and it matches Bambu's. [eSUN PETG](https://www.amazon.com/s?k=eSUN+PETG+1.75mm+1kg&tag=mizubikes-web-20) is a reasonable budget option, but I wouldn't design around the 68 MPa figure.

Overture is the cheapest well-known option, and the manufacturer lists <cite index="38-4">$14.99 against a $22.99 list price</cite>. It publishes a <cite index="38-4">Vicat softening temperature of 85.1 °C</cite>, but Vicat is not HDT and reads higher. I couldn't find a layer-strength figure. Diameter claims vary by listing: one Amazon page says <cite index="32-5">±0.02 mm</cite>, while another says <cite index="31-2">99% probability within ±0.03 mm</cite>. [Overture PETG](https://www.amazon.com/s?k=Overture+PETG+1.75mm+1kg&tag=mizubikes-web-20) fits fixtures and prototypes where nobody will test the part to failure.

## When to step up to a specialty PETG

Three Prusa variants cover most of what generic PETG can't:

- **PETG Carbon Fiber:** <cite index="10-4">HDT of 96 °C at 0.45 MPa and 80 °C at 1.8 MPa</cite>, with <cite index="10-4">flexural modulus of 2.3 GPa horizontal and 3.1 GPa vertical</cite>. It needs a hardened nozzle and <cite index="10-4">265 ± 10 °C</cite>. The 1.8 MPa HDT is the number that matters for loaded parts.
- **PETG V0:** <cite index="57-4">UL-certified, self-extinguishing PETG</cite> aimed at <cite index="57-6">housings and insulating parts in electronics</cite>. It lists at <cite index="57-3">$54.99</cite>, so use it where the flame rating is the requirement.
- **Heat-limited jobs:** If the part sees much beyond the high 60s °C, no PETG fixes that. Look at PET-CF, whose Bambu data sheet lists <cite index="40-6">HDT figures</cite> far above PETG's, or ASA. See [What is ASA Filament?](/posts/what-is-asa-filament/) for the outdoor and UV case.

## Print and design rules that matter more than the brand

Dry the spool at 65 °C for 6 to 8 hours before printing structural parts. Print at the hot end of the vendor's nozzle range (about 240 to 260 °C for most of these), and keep fan speed moderate. Polymaker's range is <cite index="59-12">20–60%</cite>, but heavy cooling sacrifices layer bond.

Orient the part so the load runs along the layers, not across them. Use more walls instead of more infill, since walls carry load in a PETG bracket. Where a part sees repeated assembly, use heat-set or press-in inserts so the fastener never loads layer lines.

Sustained load is the failure mode people overlook. Bambu's PETG Basic has a <cite index="47-8">glass transition of 69 °C</cite>, and creep accelerates well below that. A conservative design margin is to keep long-term loaded PETG parts a good 20 °C or more under Tg, which rules out the dashboard, a space-heater shelf, or a spot next to a power resistor.

Chemistry is another limit. One review of Bambu's data sheets notes <cite index="19-8">no resistance to acids or alkalis and some organic solvents</cite>, and no fire rating for generic PETG.

## Which one to buy

For most functional parts, I'd start with Bambu PETG Basic or Polymaker PETG, on the strength of their published Z-axis figures and price. Choose Prusament when tolerance and documented interlayer data matter more than cost. Step up to carbon-fiber PETG when stiffness or the 1.8 MPa HDT is the constraint, and leave PETG altogether when the operating temperature heads toward its glass transition.

If you're matching a filament to a printer with a heated chamber, the [Prusa CORE One+ write-up](/posts/prusa-core-one-plus-heated-chamber-features/) covers what that hardware adds.

## Sources

- https://prusament.com/wp-content/uploads/2022/10/PETG_Prusament_TDS_2022_10_EN.pdf
- https://prusament.com/wp-content/uploads/2022/10/PETG_Prusament_TDS_2021_10_EN.pdf
- https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-forum-prod/2024/10/e525c593-prusament-petg-technical-data-sheet.pdf
- https://www.prusa3d.com/file/3464789/prusament-petg-v0-technical-data-sheet.pdf
- https://www.prusa3d.com/product/prusament-petg-v0-natural-1kg/
- https://www.prusa3d.com/product/prusament-petg-jet-black-1kg/
- https://store.bblcdn.com/s1/default/cb94589bf7994fdcbfa833badefae9cd/Bambu_PETG_Basic_Technical_Data_Sheet.pdf
- https://store.bblcdn.com/3a230e260a3a47c2b0db0156e07eef91.pdf
- https://us.store.bambulab.com/products/petg-basic
- https://3dfilamentprofiles.com/filament/details/439
- https://wiki.bambulab.com/filament-acc/petcf-ppacf/07689de83afd4cc480f136c7697e6de3.pdf
- https://www.goodprints3d.com/blogs/reviews/bambu-lab-petg-hf-review-a-faster-petg-pick-for-makers-who-want-tougher-utility-prints-without-giving-up-modern-high-speed-workflows
- https://shop.polymaker.com/products/petg?variant=39574344761401
- https://polymaker.com/best-petg-filament-for-3d-printing-speed-strength-value/
- https://wiki.polymaker.com/polymaker-products/polymaker-filaments/prime-materials/petg
- https://wiki.polymaker.com/polymaker-products/polymaker-filaments/prime-materials/petg/polymaker-tm-petg-new
- https://filascope.com/filament/polymaker-petg-polymakertm-petg--lime--62f01216
- https://all3dp.com/1/petg-filament-3d-printing/
- https://www.esun3d.com/epetg-lite-product
- https://www.esun3d.com/uploads/eSUN_PETG+HS-Filament_TDS_V1.0.pdf
- https://overture3d.com/products/overture-high-speed-petg
- https://www.amazon.com/OVERTURE-Filament-Consumables-Dimensional-Accuracy/dp/B0991YSBDG
- https://www.walmart.com/ip/OVERTURE-PETG-Filament-1-75mm-3D-Printer-Filament-1kg-Spool-2-2lbs-Dimensional-Accuracy-99-Probability-0-03-mm-Fit-Most-FDM-Orange/772010720
