---
title: "3D Print Strength: Walls vs Infill vs Orientation"
date: 2026-11-20
description: "3D print strength comes from orientation, wall count, then infill. Learn wall counts, infill percentages, and layer-direction rules backed by real TDS numbers."
slug: 3d-print-strength-walls-infill-orientation
categories: ["Guides"]
tags: ["print strength", "infill", "wall count", "print orientation", "functional parts"]
cover:
  image: "/images/Parts-printed-in-printer.png"
  alt: "Several 3D printed functional parts and brackets on a workbench"
  caption: ""
  relative: false
draft: false
---

*MizuMakes may earn a commission from links in this post.*

For 3D print strength, set the order of priority as orientation first, wall count second, and infill third. Most people do it backwards and pile on infill. Layers bond to each other more weakly than plastic bonds within a layer, so the direction of your load matters more than anything you set in the slicer. After that, walls carry most of the load, and infill mostly supports the top surfaces and adds some bulk stiffness.

Below is how I'd choose those three variables for a real bracket, clip, or fixture, with data sheet numbers where they exist.

## What Controls 3D Print Strength: Walls, Infill, or Orientation?

Orientation sets the ceiling. Walls decide how much of that ceiling you reach. Infill is the last, cheapest-to-skip lever.

Prusa's documentation says a model's strength is mostly defined by the number of perimeters, not the infill. The physics is simple. In bending or tension, stress is highest at the outer surface, so the shell is where the material does the work. Infill sits in the neutral zone, where it contributes little.

The best-known test is CNC Kitchen's hook comparison. A baseline hook with two perimeters and 10% infill was compared against two control hooks of equal weight: one with 42% infill and one with five perimeters. The five-perimeter hook was nearly 22% stronger than the high-infill one. Treat that as one test on one printer and filament, not a universal constant. It does match what Prusa's documentation says.

## How Much Weaker Is the Z Axis? Orientation by the Numbers

FDM parts are anisotropic. One guide puts Z strength at only 30% to 70% of XY strength, depending on material, print parameters, and chamber temperature. Bambu Lab publishes both directions on its data sheets, which makes the gap easy to see:

| Bambu Lab filament | Tensile XY / Z (MPa) | Bending XY / Z (MPa) | Impact XY / Z (kJ/m²) |
|---|---|---|---|
| PETG Basic (TDS V3.0) | 51 / 35 | 75 / 56 | 34.2 / 10.5 |
| PETG HF | 34 / 23 | 64 / 48 | 31.5 / 10.6 |

Sources: Bambu's PETG Basic data sheet and its PETG HF data sheet. Both land at roughly two-thirds of XY tensile strength in Z. Impact in Z is about a third of XY for the Basic grade, which is the number that matters for snap-off failures. PETG HF's XY impact value is a different measurement. Its data sheet lists 31.5 kJ/m² unnotched and 6.2 kJ/m² notched.

Two cautions. First, these are specimens printed under ideal conditions on a tuned machine. Your part, with corners, bosses, and a cooler room, will land lower, and the Z-axis number drops fastest. Second, studies vary a lot. One materials article says FDM parts can be 4 to 5 times weaker in Z tension than in the XY plane. Design with a generous margin on any load that crosses layers.

### What to do with that

Orient the part so the main stress runs along the layers, not across them. Laying brackets flat helps reduce delamination and improves tensile and flexural performance. A few cases I'd think through before slicing:

- **L-bracket or hook:** Print it on its side so the bend is formed by continuous lines in a layer. Standing it upright makes the inside corner a layer-separation line.
- **Pins, shafts, and tall tabs loaded sideways:** These break across layers when printed vertically. Lay them down.
- **Compression along the build axis:** This is the one load that tolerates upright printing, since layers are pressed together rather than pulled apart.
- **Cantilevered snap fits:** The flexing arm should have its layers running along its length. Printed upright, the arm will crack at the root.

The tradeoff is that the best orientation for strength sometimes needs supports or gives a worse surface finish. That's usually an easy trade for a part that carries load.

## How Many Walls Should a Functional Part Have?

Slicer defaults are 2 walls and 15% infill on Bambu Studio. Bambu's own guidance says that's enough for most non-structural parts. For anything carrying load, I'd start at 4 walls. Some references put the sweet spot at four to six walls, with more impact than pushing infill past 25-30%.

That's a vendor blog's number, so verify it on your own part. Returns do diminish. A PLA study reported modulus of 626 MPa, 720 MPa, and 804 MPa for 1, 2, and 3 perimeters on one printer and profile. Each added wall helped, with smaller gains each time.

The cost is cheap. On one test cube, going from 2 to 4 walls added 4.5 g, while going from 20% to 30% infill added 6.4 g. That makes walls the better buy per gram for bending loads.

There's a ceiling. For ABS, ASA, and PC, Bambu recommends keeping walls to 6 or fewer and infill at 50% or below. Past that, the extra material increases the risk of warping from cooling contraction. This is another reason a solid block is usually the wrong answer. If you're printing in those materials, a decent enclosure matters more than the wall count; see my [enclosure comparison for ABS and ASA](/posts/best-3d-printer-enclosure-abs-asa/).

## Is 100% Infill Ever Worth It?

Rarely. Going from 20% to 100% costs a lot of time and filament for modest stiffness gains in bending, and thick solid sections shrink and warp more. One study that compared design cases found that adding an exterior perimeter moved the stress concentration from the outer edges toward the center of the specimen. That is more evidence for spending material on the shell first.

There is one smart exception: local reinforcement. CNC Kitchen's SmartInfill approach uses a mesh modifier to print only the high-stress region at 100% infill and the rest at 10%. The result was 33% stronger than the best control hook. In Bambu Studio you can reproduce this with a modifier shape and a higher sparse infill density over the loaded area. Put it around screw bosses, clamp points, and the root of any cantilever.

## Which Infill Pattern Is Strongest?

Pattern matters less than people expect. In a controlled tensile study summarized by one guide, the pattern changed maximum tensile strength by less than 5%. Choose by load direction and print time instead.

Gyroid and cubic are good defaults. Prusa says gyroid has similar strength in every direction, no line crossings within a layer, and prints fairly quickly. Cubic is also a reasonable pick when strength under multi-directional load matters. Grid and lines are fine for simple, one-axis loads. Concentric infill only makes sense near 100%. At lower densities, it's the weakest pattern because it lacks horizontal strength.

![Slicer preview of a flat plate: gyroid infill in the middle, with solid perimeters around the outer edge and around each screw hole](/images/gyroid-infill-walls-around-bosses-slicer.webp)
*Gyroid infill in a slicer preview. Perimeters ring the outer edge and every screw hole, so the edges and bosses are solid plastic while the middle stays light.*

For density, one Bambu Studio walkthrough suggests 20-25% for strength parts. That's a sensible starting point. Above about 40%, adding walls is the cheaper way to gain strength.

## Layer Height and Line Width: The Quiet Strength Settings

Layer height changes how much bonding area each layer has. Prusa says layer height should stay below 80% of the nozzle diameter, which caps a 0.4 mm nozzle at roughly 0.32 mm. A meta-analysis found that thicker layers might reduce tensile strength by up to 20%. A 0.16-0.20 mm layer is a good compromise for load-bearing parts on a 0.4 mm nozzle. Prusa's watertight-print guide notes that CNC Kitchen found the most durable prints at 0.15 mm, though 0.2 mm does fine.

Nozzle temperature and cooling also set layer bonding, and they're material-specific. Wet filament weakens it too, so dry your spools; I cover that in the [filament drying comparison](/posts/how-to-dry-filament-dryer-box-vs-dehydrator-vs-heated-bed/). For the material side of the choice, see [PLA vs PETG strength and heat resistance](/posts/pla-vs-petg/). If you need more stiffness, [PLA-CF, PETG-CF, and PA-CF](/posts/pla-cf-vs-petg-cf-vs-pa-cf/) have their own tradeoffs. Carbon-fiber filament usually raises XY stiffness more than Z strength, so orientation matters even more with it.

Wall thickness should also match your nozzle. A Printables test model suggests the dimension just below the first appearance of gap fill is the strongest and fastest to print. That means designing walls in multiples of your extrusion width, so the slicer doesn't leave voids.

## How Do I Design Screw Holes and Bosses That Don't Split?

Bolted joints are where printed parts usually fail, not the open areas. Printed threads strip, and screws driven straight into plastic hold less each time you reassemble. Brass heat-set inserts fix this, but the boss geometry has to cooperate. A set of M3 inserts is cheap, and I'd search [M3 heat set inserts](https://www.amazon.com/s?k=M3+heat+set+inserts&tag=mizubikes-web-20) in a bundle with a few drill-matched sizes.

Guidance on boss wall thickness varies by source. One recommends at least 1.6 mm of plastic all around the hole, closer to twice the insert's outer diameter for real loads. Another cites 2 to 3 times the insert diameter from injection molding practice. I'd go with the bigger number for anything that sees torque.

For an M3 insert, the printed hole wants to be roughly 4.0 to 4.2 mm. One test found inserts started fitting around 4.1 mm in horizontally printed holes and 4.2 mm in vertical ones. Print a test coupon on your own machine before committing to a design. Add a relief well about 1-2 mm deeper than the insert so displaced plastic has somewhere to go. Make sure the boss walls are solid by setting enough perimeters. One guide says four perimeters give 1.8 mm of solid plastic around each hole, a good minimum for M2 to M4, with five or six for M5 or load-bearing parts.

Material matters here too. PLA creeps under sustained load, particularly near heat. Insert bosses in PLA can loosen over time, so use PETG, ASA, or nylon for anything that stays under clamp load. The [HT-PLA vs PETG heat comparison](/posts/ht-pla-vs-petg-annealing-heat-resistance/) covers the temperature side of that.

## Quick Settings Starting Points

For a bracket in PETG on a 0.4 mm nozzle, I'd start here and adjust from testing:

- **Orientation:** Load runs along the layers, never pulling them apart.
- **Layer height:** 0.16-0.20 mm.
- **Walls:** 4, increasing to 5-6 for high-load parts (6 max for ABS/ASA/PC).
- **Infill:** Gyroid or cubic at 20-30%, with a local 100% modifier at bolt bosses.
- **Top/bottom shells:** Enough layers to bridge the infill, plus extra for parts that bend.
- **Fillets:** Radius every inside corner, since sharp corners concentrate stress in any material.

If you want filament with good published numbers, [Bambu PETG HF](https://www.amazon.com/s?k=Bambu+Lab+PETG+HF&tag=mizubikes-web-20) and [PETG Basic](https://www.amazon.com/s?k=Bambu+Lab+PETG+Basic&tag=mizubikes-web-20) both publish XY and Z data. Few brands do. I compare more PETG data sheets in [best PETG filament brands for functional parts](/posts/best-petg-filament-brands-functional-parts/).

## When Settings Won't Save the Part

No infill pattern fixes weak interlayer bonding. If a part must resist a load across the layers, such as a hook pulling upward from a vertical print, redesign it. Print it in two pieces and bolt them together, or print the loaded section flat. If the part has to survive sustained load at high temperature, switch materials before you add walls. A PLA part with 8 walls still softens at the same temperature.

Finally, test before trusting. Print the real part, load it beyond the design load, and see where it breaks. Then fix the geometry or orientation at that spot.

## Sources

- [Bambu Lab PETG Basic technical data sheet (V3.0)](https://store.bblcdn.com/s1/default/cb94589bf7994fdcbfa833badefae9cd/Bambu_PETG_Basic_Technical_Data_Sheet.pdf)
- [Bambu Lab PETG HF technical data sheet](https://store.bblcdn.com/ce12d65176a94f1086e6aefa238e62e2.pdf)
- [Prusa Knowledge Base: Layers and perimeters](https://help.prusa3d.com/article/layers-and-perimeters_1748)
- [Bambu Lab Wiki: ABS / ASA / PC usage guide](https://wiki.bambulab.com/en/filament/abs_asa_pc)
- [3ders: CNC Kitchen SmartInfill hook test](https://www.3ders.org/articles/20190208-stefan-at-cnc-kitchen-experimenting-with-smart-infill-for-stronger-3d-prints.html)
- [WEERG: FDM orientation and strength](https://www.weerg.com/guides/orientation-in-fdm-3d-printing)
- [Emrld Labs: heat-set insert hole sizing and boss design](https://emrldlabs.com/blog/heat-set-threaded-inserts-hole-sizing-install-strength/)
