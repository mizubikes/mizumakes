---
title: "PLA-CF vs PETG-CF vs PA-CF for Functional Parts"
date: 2026-11-18
description: "PLA-CF vs PETG-CF vs PA-CF compared on Bambu TDS numbers: heat resistance, Z-axis strength, moisture, settings, and which suits your part."
slug: pla-cf-vs-petg-cf-vs-pa-cf
categories: ["Guides"]
tags: ["carbon fiber filament", "PAHT-CF", "nylon", "functional parts"]
cover:
  image: "/images/Parts-printed-in-printer.png"
  alt: "Assortment of black 3D printed functional parts on a workbench"
  caption: ""
  relative: false
draft: false
---

*MizuMakes may earn a commission from links in this post.*

For PLA-CF vs PETG-CF vs PA-CF, the short answer is to pick by temperature and moisture first, then stiffness. PLA-CF is the stiffest easy option, but it softens at about 55 °C. PETG-CF buys you a bit more heat margin and toughness. PA-CF (nylon with carbon fiber) is the only one of the three that belongs in a genuinely hot or load-bearing part, and it costs you an enclosure, a dryer, and a hardened nozzle.

One caveat before the numbers. I'm using Bambu Lab's data sheets because they publish the same test set for all three families. Other brands differ, and every TDS figure comes from ideal specimens. Printed parts land lower, and the Z axis (across layers) lands much lower.

## PLA-CF vs PETG-CF vs PA-CF: the numbers side by side

| Material (Bambu) | HDT 0.45 / 1.8 MPa | Tensile XY / Z | Saturated water uptake | Nozzle |
|---|---|---|---|---|
| PLA-CF | 55 / 54 °C | 38 / 26 MPa | 0.42% | 210–240 °C |
| PETG-CF | 74 / 68 °C | 35 / 29 MPa (see note) | not found | 240–270 °C |
| PA6-CF | 186 / 164 °C | 102 / 48 MPa | 2.35% | 260–290 °C |
| PAHT-CF (PA12-based) | 194 / 170 °C | 92 / 47 MPa | 0.88% | 260–290 °C |

The PETG-CF Z value moves between data sheet revisions. One revision lists 59 MPa in XY and 38 MPa in Z, while another lists the lower figures above. Treat PETG-CF as roughly 30–40 MPa across layers and test your own part.

Two patterns stand out. The Z-axis tensile strength of the nylons is about half of XY. PLA-CF and PETG-CF are weaker in absolute terms, but the penalty is similar in proportion.

## Is PLA-CF good enough for functional parts?

For rigid, room-temperature parts, yes. Bambu lists PLA-CF bending modulus at 3950 MPa against 2910 MPa for PETG-CF, so PLA-CF is the stiffer of the two. That suits jigs, camera and sensor brackets, drone frames, and fixtures that see load but not heat.

The limit is thermal. The glass transition is 63 °C and HDT is 54–55 °C. A bracket behind a windshield or next to a motor will creep long before it reaches that number, because sustained load plus a temperature within 15–20 °C of Tg is where plastics flow. Elongation is also low. Break elongation drops from 8.4% in XY to 3.6% in Z, so it fails with little warning.

It's the easy one to print. Bambu suggests drying at 55 °C for 8 hours, a bed of 35–45 °C, and speeds under 200 mm/s. Because chamber heat isn't needed, it works on open-frame machines. If you want more heat margin without leaving PLA, see my [HT-PLA vs PETG annealing comparison](/posts/ht-pla-vs-petg-annealing-heat-resistance/).

## PETG-CF vs PLA-CF: what do you actually gain?

You gain toughness and about 20 °C of HDT, and you give up stiffness. Bambu's own comparison shows Z-axis impact of 10.7 kJ/m² for PETG-CF against 7.8 for PLA-CF. The PETG-CF sheet lists 10.4% elongation and 41.2 kJ/m² impact strength, which is why it fits clips, drone parts, and anything that gets knocked around.

It is not a heat material, though. HDT is 74 °C at 0.45 MPa and 68 °C at 1.8 MPa. Use it where the part sees a warm room or a sunlit shelf, not an engine bay. For outdoor and chemical-exposure parts, I'd compare it against unfilled options in [PCTG vs ASA vs PETG](/posts/pctg-vs-asa-vs-petg/) before paying the carbon premium.

Print settings are PETG-like. Bambu lists 240–270 °C nozzle, 65–75 °C bed, and drying at 65 °C for 8 hours. Expect moisture to show up as stringing and a rough surface, so dry it. For unfilled PETG brand comparisons, see [Best PETG Filament Brands for Functional Parts](/posts/best-petg-filament-brands-functional-parts/).

## PA6-CF vs PAHT-CF: which nylon carbon fiber?

Both are nylon, but they behave differently once they absorb water. PA6-CF is the stiffest and strongest dry. Its dry XY bending modulus is 5460 MPa against 4230 MPa for PAHT-CF. The price of that stiffness is moisture. Saturated water absorption is 2.35% for PA6-CF versus 0.88% for PAHT-CF.

When wet, the gap closes. Wet XY bending modulus is 3560 MPa for PA6-CF and 3640 MPa for PAHT-CF. Bambu describes PAHT-CF as a PA12 and carbon fiber composite that keeps its properties when damp. Bambu says PA6-CF loses stiffness and strength after absorbing water, so it advises against it for thin, long parts that need dimensional stability. The flip side is that damp PA6-CF becomes tougher against drops and impacts.

My rule: if the part lives in a conditioned room and needs maximum stiffness, PA6-CF is the pick. Choose PAHT-CF for anything in a garage, workshop, or machine, or where dimensions matter. PAHT-CF also has better published layer performance. Bambu reports Z-axis impact of 13.3 kJ/m² versus 5.7 for older normal PA-CF. Bambu notes that the older PA-CF has been discontinued in favor of PAHT-CF.

## What does nylon CF need to print reliably?

More than the other two combined. For PAHT-CF, Bambu specifies drying at 80 °C for 8–12 hours, a 260–290 °C nozzle, an 80–100 °C bed, and a 45–60 °C chamber. It recommends a 0.6 mm nozzle, with 0.4 and 0.8 mm also listed. The product page lists speeds under 100 mm/s, which means you're trading print time for strength. Bambu says it is unsuitable for open-frame printers.

Drying is where people trip. The AMS 2 Pro tops out at 65 °C, so it cannot complete the 80 °C cycle. Dry in a dedicated dryer instead, or read my [AMS vs AMS 2 Pro vs AMS HT breakdown](/posts/bambu-lab-ams-vs-ams-2-pro-vs-ams-ht/) and my [filament drying comparison](/posts/how-to-dry-filament-dryer-box-vs-dehydrator-vs-heated-bed/). Keep the spool sealed or in a dry box while printing.

Annealing is optional. Bambu suggests 80–130 °C for 5–12 hours for PAHT-CF, but annealed parts can change dimensions, so test on a coupon before doing it to a tight-tolerance part.

## Do carbon fiber filaments need a hardened steel nozzle?

Yes, all three. Bambu says a stainless steel nozzle is not recommended for PLA-CF, and lists a hardened steel nozzle for PETG-CF. The details are in [Hardened Steel Nozzle: Which Filaments Need One?](/posts/hardened-steel-nozzle-abrasive-filaments/). Brass wears out quickly under chopped carbon fiber, and the resulting oversize bore quietly wrecks your dimensional accuracy.

## How should you design and orient carbon fiber parts?

Print so the load runs along the filament paths, not across layers. A bracket that is loaded in bending should have its layers parallel to the bending plane, not stacked perpendicular to it. Carbon fiber improves stiffness along the road direction, but the TDS Z-axis numbers above show how much of that you lose between layers.

A few practical habits follow from the data:

- Use more walls than infill. Perimeters carry most of the load in a printed part.
- Add fillets at corners and avoid sharp transitions where layers peel apart.
- Use heat-set or press-in inserts for threads, not printed threads. Carbon-filled plastics are stiff and notch-sensitive, so tapped threads are weak.
- Avoid snap fits in PLA-CF and PA6-CF. Their break elongation is only a few percent, and the PETG-CF and wet nylon are more forgiving.
- Leave extra clearance on mating features, then adjust from a test print. CF filaments shrink less than their base polymers, but that does not remove the need for calibration.

## What does carbon fiber filament cost?

Prices swing with sales, so check current listings. On the Bambu US store, PETG-CF lists at $34.99 for a 1 kg spool, and PLA-CF variants are also $34.99 for 1 kg. PAHT-CF starts at $49.99 per 0.5 kg, about $0.10 per gram. Roughly, nylon CF costs two to three times as much per kilo as the PLA and PETG versions. For basics on cost per gram, see [How Much Does 3D Printer Filament Cost?](/posts/how-much-does-3d-printer-filament-cost/).

If you want to price-check any of these, here are search links for [Bambu PLA-CF](https://www.amazon.com/s?k=Bambu+Lab+PLA-CF&tag=mizubikes-web-20), [Bambu PETG-CF](https://www.amazon.com/s?k=Bambu+Lab+PETG-CF&tag=mizubikes-web-20), and [Bambu PAHT-CF](https://www.amazon.com/s?k=Bambu+Lab+PAHT-CF&tag=mizubikes-web-20).

## Which one should you pick?

Pick PLA-CF for stiff indoor jigs, fixtures, and brackets that stay below about 45 °C. Pick PETG-CF when you want some impact tolerance and a few more degrees of margin. Pick PAHT-CF for heat, humidity, and sustained load. Pick PA6-CF only for dry, stiffness-critical parts.

There is one more option above all three. Bambu's PET-CF lists HDT of 205 °C at 0.45 MPa and 182 °C at 1.8 MPa, with low moisture absorption. Its Z-axis tensile strength is only 35 MPa, so it's stiff and hot but not tough across layers.

Skip all of them for parts that need UV exposure, flexibility, or thin snap features. Carbon fiber raises stiffness, not toughness. For those cases, ASA or unfilled PETG is usually the better engineering call.

## Sources

- [Bambu Lab PLA-CF technical data sheet](https://store.bblcdn.eu/s8/default/aefa8303ad8d40248b0d86dfdad46518/Bambu_PLA-CF_Technical_Data_Sheet_V3.pdf)
- [Bambu Lab PETG-CF technical data sheet](https://3dstore.ch/shop/ProdukteDetails/Bambu_PETG-CF-Technical_Data_Sheet.pdf)
- [Bambu Lab PAHT-CF technical data sheet V3.0](https://wiki.bambulab.com/filament-acc/asacf-pahtcf/65f1b18a6d6142d794a1a6a00f1496ef.pdf)
- [Bambu Lab PA6-CF specs and PA6-CF vs PAHT-CF table (MatterHackers)](https://www.matterhackers.com/store/l/bambu-lab-pa6-cf-filament/sk/MC64KFKY)
- [Bambu Lab US store: PETG-CF](https://us.store.bambulab.com/products/petg-cf)
- [Print3DIndex: Bambu PAHT-CF specs and drying notes](https://www.print3dindex.com/materials/bambu-lab-paht-cf)
