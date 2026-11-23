---
title: "Heat Set Inserts vs Printed Threads vs Captive Nuts"
date: 2026-11-22
description: "Heat set inserts vs printed threads vs captive nuts: torque and pull-out data, M3 hole sizes, install temps, and which fastener fits each functional part."
slug: heat-set-inserts-vs-printed-threads-vs-captive-nuts
categories: ["Guides"]
tags: ["heat set inserts", "fasteners", "design for 3d printing", "functional parts"]
cover:
  image: "/images/Parts-printed-in-printer.png"
  alt: "Close-up of 3D printed parts on a workbench"
  caption: ""
  relative: false
draft: false
---

*MizuMakes may earn a commission from links in this post.*

For most functional parts, heat set inserts vs printed threads vs captive nuts comes down to a simple rule. Use brass heat-set inserts for screws you will open more than a couple of times. Use captive nuts when you can design a pocket and want a full steel thread with no heating step. Use printed threads only for large, low-load features like lids, caps, and knobs.

The details matter more than the rule, though. Hole size, wall thickness, and print orientation decide whether an insert holds 150 kg or spins in place. Here is what the test data and design guides say.

## Heat set inserts vs printed threads vs captive nuts: the short version

The best head-to-head FDM data I found is an older CNC Kitchen test in PETG. It measured torque-out, which is the tightening torque at which the part starts to fail. Direct screwing and a Helicoil both gave up at 1 Nm, embedded nuts reached 2 Nm (where the PETG failed in compression), and the heat-set insert won clearly at 3 Nm.

To put that in context, even 1 Nm on an M3 bolt is already more than 1500 N of pretension. So the printed-thread result isn't useless for a one-off joint. It just leaves little margin.

| Method | Torque-out in PETG test | Best fit | Main weakness |
|---|---|---|---|
| Screw into printed or tapped plastic | ~1 Nm | One-time assembly, light loads | Plastic threads wear and creep |
| Captive (embedded) nut | ~2 Nm, limited by plastic crushing | Max clamp load, deep pockets | Needs pocket and access, or a mid-print pause |
| Heat-set brass insert | ~3 Nm | Repeated disassembly, one-sided access | Needs a sized hole and a soldering iron |

These numbers come from one printer, one material, and one test setup. Treat them as a ranking, not as design allowables.

## How strong are heat-set inserts, really?

Very strong when the hole is right. In CNC Kitchen's 2026 re-test, M3 inserts pulled out at around 1400 newtons on average, almost 150 kilograms. The samples were PLA on a CORE One L, and the author notes results shift with printer and material.

Brand matters too. In an earlier comparison, Ruthex held 181 kg, a generic eBay insert 157 kg, and a cheap one only 39 kg. The cheap one had only vertical knurling, which is fine for torque but poor for pull-out. Torque-out was roughly the same across all three.

There is a counterpoint. A screw driven straight into solid plastic held about 142 kg in one CNC Kitchen test, more than the cheap insert and close to the mid-grade one. So the case for inserts is not one-shot pull-out. It is repeated assembly, higher torque, and a metal thread that doesn't wear. Heat-set inserts remain the pick for connections you open over and over.

A caution on infill. A PLA study found that basic heat-set inserts depend on surface adhesion and are less affected by infill rate. Another guide says pull-out depends primarily on the number of solid walls around the hole. That fits the broader walls-over-infill logic in [3D print strength: walls vs infill vs orientation](/posts/3d-print-strength-walls-infill-orientation/). Add perimeters around the boss, not infill.

## When are printed threads acceptable?

Printed threads cost nothing and need no hardware, but they have two problems. Plastic threads wear faster than a metal insert and creep under sustained load. Every thread flank is also a stack of layer lines, so the layer bond becomes the load path.

Size is the other limit. One FDM study notes that below M6, thread tolerances increase and thread strength drops significantly. A lab study on SLS nylon (a much more isotropic process than FDM) found printed M8 threads failing at an average of 3.41 kN versus 3.83 kN with heat-set inserts. The authors concluded that printed threads are limited to larger sizes and lower loads.

So model threads in the part for jar lids, adjuster knobs, large clamping screws, and jigs. Don't model them for M3 or M4 fasteners that hold a bracket on. If you want a printed thread to survive, use a coarse pitch and large diameter, and test-print the fit on your printer first.

## Are captive nuts stronger than heat-set inserts?

Often yes, on raw holding force, because a nut bears on a broad face instead of relying on knurls gripping melted plastic. In a student test at MIT's fab class, pulling the embedded M3 nut out of the block took the most force, with the M3 heat-set insert a very close second. A design guide makes a similar point: an embedded nut is locked in by surrounding material on all sides. Another source frames it as a tradeoff: captive nuts give familiar hardware, broad bearing, and zero-heat installation, at the cost of pocket volume and access.

The catch is load direction relative to layers, and this is my own reasoning from how FDM parts fail. If the nut pulls up against a few bridged roof layers, you are loading layer adhesion in tension, which is the weak axis. If you orient the part so the nut bears against a vertical wall of continuous perimeters, the load runs in-plane and the joint is much better. Pick the pocket orientation with that in mind.

For the pocket, nominal M3 nut dimensions are 5.5 mm across flats and 2.4 mm thick. Add clearance for your printer, and print a test strip first. For a closed pocket, you can pause the print and drop the nut in, but that introduces defect risk. A side-loading slot avoids this.

Square nuts are often the better choice for those slots. A DIN 562 M3 square nut is 5.5 mm across and only 1.8 mm thick, so the slot stays shallow. Its flat sides also keep it from spinning, and it slides in along the slot without having to line up a hex point. That's why many printer designs, including Prusa's, use them. A [100-pack of M3 DIN 562 stainless square nuts](https://www.amazon.com/dp/B07G9TTZDB?tag=mizubikes-web-20) is cheap enough to keep on hand. Size the slot about 0.2 to 0.3 mm over the nut's width and thickness, then test-fit on your printer.

## How do I size the hole and wall for an M3 insert?

Start from the manufacturer drawing, then correct for FDM. Ruthex lists a 4.0 mm hole, 5.7 mm length, and 1.6 mm minimum radial wall for the RX-M3x5.7. The same chart gives M4 at 5.6 mm hole with a 2.1 mm wall, and M5 at 6.4 mm with a 2.6 mm wall.

Printed holes come out small. CNC Kitchen measured printed holes about 0.25 mm under the designed size, so its M3 insert needs 4.2 mm in CAD to land at a 4.0 mm hole. Its data show the major strength drop between 4.1 and 4.2 mm in the as-printed samples. Either way, run a diameter ladder on your own machine. Holes on a vertical face can print a different size from upright holes, so test in the orientation you will use.

A few more rules:

- **Depth:** make blind holes roughly 1 mm deeper than the insert is long, so displaced plastic has somewhere to go. For a 5.7 mm M3 insert, that's about 6.7 mm.
- **Temperature:** CNC Kitchen recommends 10 to 20 °C above the filament's printing temperature, around 225 °C for PLA and 245 °C for PETG. Too hot with an oversized hole risks the entire wall pulling out, per a Georgia Tech guide.
- **Boss:** one guide suggests a boss about twice the insert width, so 8 to 9 mm for a 4.6 mm M3 insert.
- **Cooling:** let the insert cool before tightening a screw into it.

On cost, inserts are cheap. 3DJake lists Ruthex M3x5.7, 100 pieces, at $8.36 before shipping, and marketplace resellers charge more. On Amazon, the same [ruthex M3x5.7 inserts, 100 pieces](https://www.amazon.com/dp/B08BCRZZS3?tag=mizubikes-web-20) are listed, though prices vary by seller. If you'll use more than M3, the [ruthex M2/M3/M4/M5 assortment bundled with seven heat-set tips](https://www.amazon.com/dp/B0FCXXW62N?tag=mizubikes-web-20) covers the common sizes plus the iron tips in one order. You will also want a [temperature-controlled soldering iron](https://www.amazon.com/s?k=temperature+controlled+soldering+iron&tag=mizubikes-web-20) rather than a fixed-wattage pencil, because the temperature window is narrow. For captive nuts, a [stainless M3 hex nut assortment](https://www.amazon.com/s?k=M3+stainless+hex+nut+assortment&tag=mizubikes-web-20) covers most pockets, and [M3 DIN 562 square nuts](https://www.amazon.com/dp/B07G9TTZDB?tag=mizubikes-web-20) suit side-loading slots.

## Which should I use for brackets, enclosures, and hot parts?

**Enclosures and electronics mounts:** heat-set inserts. You get a flush, one-sided thread and can reopen the lid indefinitely. One insert guide says they win where there's no room for a nut pocket, which covers most enclosures, brackets, and printer upgrade parts.

**Load-bearing brackets with a through-bolt:** captive nut, oriented so the nut bears on perimeters, not roof layers. Steel on steel, no heat, and a replaceable nut.

**Jigs, fixtures, lids, and knobs:** printed threads are fine at larger sizes. Fixtures that see occasional light loads don't justify extra hardware.

**Hot or sustained-load parts:** this is where inserts can fail quietly. The insert sits in a polymer boss, so the boss's heat deflection and creep behavior set the limit, not the brass. In PLA near its glass transition, an insert under steady tension will slowly pull through. Pick a material suited to the temperature, as covered in [PLA vs PETG](/posts/pla-vs-petg/) and [HT-PLA vs PETG with annealing](/posts/ht-pla-vs-petg-annealing-heat-resistance/). Use a captive nut with a broad bearing face for sustained clamp load.

**When not to use inserts:** thin walls below the minimum, parts printed from very soft materials like TPU, and joints that will take one assembly only (self-tapping screws are fine there).

The common thread is that fastener choice is a boss design question. Add walls, orient the load in-plane with the layers, and verify the hole size on your own printer before you commit a batch.

## Sources

- [CNC Kitchen: Are Our Heat-Set Insert Datasheets Wrong?](https://www.cnckitchen.com/blog/are-our-heat-set-insert-datasheets-wrong)
- [CNC Kitchen: Helicoils vs Threaded Inserts vs Embedded Nuts](https://www.cnckitchen.com/blog/helicoils-threaded-insets-and-embedded-nuts-in-3d-prints-strength-amp-strength-assessment)
- [CNC Kitchen: Threaded Inserts, Cheap vs Expensive](https://www.cnckitchen.com/blog/threaded-inserts-for-3d-prints-cheap-vs-expensive)
- [CNC Kitchen: Tips & Tricks for Heat-Set Inserts](https://www.cnckitchen.com/blog/tips-and-tricks-for-heat-set-inserts)
- [MDPI Polymers: Load-Bearing Assessment of Threads in 3D-Printed Polymer Elements](https://www.mdpi.com/2073-4360/18/1/112)
- [MIT Fab Academy notes: embedded nut vs heat-set insert pull test](https://fab.cba.mit.edu/classes/863.25/people/MattiGruener/assignments/week4)
- [3DJake: ruthex M3 inserts, 100 pieces](https://www.3djake.com/ruthex/threaded-insert-m3-100-pieces)
- [Prusa forum: M3 DIN 562 square nuts](https://forum.prusa3d.com/forum/original-prusa-i3-mk3s-mk3-general-discussion-announcements-and-releases/m3-din-562-square-nuts/)
