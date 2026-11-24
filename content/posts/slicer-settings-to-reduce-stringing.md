---
title: "Slicer Settings to Reduce Stringing: Ranked by Impact"
date: 2026-11-23
description: "Slicer settings to reduce stringing, ranked by impact: drying, nozzle temperature, retraction, wipe and travel, with starting numbers."
slug: slicer-settings-to-reduce-stringing
categories: ["Guides"]
tags: ["stringing", "retraction", "slicer settings", "PETG", "troubleshooting"]
cover:
  image: "/images/slicer-settings-to-reduce-stringing-cover.webp"
  alt: "Close-up of a 3D printer nozzle depositing filament on a print"
  caption: "Photo: ZMorph3D / Pixabay"
  relative: false
draft: false
---

*MizuMakes may earn a commission from links in this post.*

The slicer settings to reduce stringing that matter most are, in order: dry the filament, lower the nozzle temperature by 5-10 °C, then tune retraction to roughly 1 mm on a direct-drive extruder. Wipe, travel, and Z-hop settings come after that. Most people start at retraction because it's the setting they can see in the slicer. The cause is usually upstream of it.

For functional parts, this matters beyond looks. Strings between mounting bosses or inside a snap-fit pocket have to be cleaned off before the part assembles. The same fixes also touch layer adhesion, which is the weak axis of any FDM part, so the goal is the smallest change that works.

## What actually causes stringing?

Stringing is molten plastic leaking from the nozzle during a travel move. Three things drive the leak: moisture, melt viscosity, and pressure in the melt zone.

Moisture first. Water in the filament turns to vapor and expands as it heats in the nozzle, pushing the melt outward. Bambu's retraction documentation says damp filament is more prone to stringing and oozing, and adjusting retraction usually can't fully solve it.

Viscosity second. Higher temperature means lower viscosity, which means more ooze during travel. Pressure third. Retraction pulls filament back to relieve that pressure before the nozzle moves. Bambu's wiki describes it as reducing the pressure of molten filament in the hot end.

That gives the fix order. If you retract more to compensate for a wet spool, you're treating a symptom, and you may clog the nozzle.

## Step 1: Dry the filament before touching the slicer

PETG is the usual offender. Polymaker's PETG page calls it very hygroscopic, with wet material causing stringing and poor surface quality. Its guidance is to dry first, and only then lower the nozzle temperature and fine-tune retraction and travel settings.

Drying numbers depend on the exact product, so use the maker's figure. Polymaker lists 60 °C for 6 hours for its standard PETG, and 65 °C for 6 hours for PolyMax PETG. Bambu's own PETG guidance, as reported by a third-party retailer, is 65 °C for 8 hours in a blast drying oven or in an AMS 2 Pro/AMS HT. Don't treat 60, 65, and 70 °C as interchangeable. Our [filament drying comparison](/posts/how-to-dry-filament-dryer-box-vs-dehydrator-vs-heated-bed/) covers dryer box versus dehydrator versus heated bed.

If you don't own a dedicated dryer, a [filament dryer like the Polymaker PolyDryer](https://www.amazon.com/s?k=Polymaker+PolyDryer&tag=mizubikes-web-20) is the straightforward fix. Spools of [Polymaker PETG](https://www.amazon.com/s?k=Polymaker+PETG+filament&tag=mizubikes-web-20) are a reasonable baseline to test against. For other brands, our [PETG brand comparison](/posts/best-petg-filament-brands-functional-parts/) lists TDS numbers.

A wet spool tends to announce itself with popping, a rough surface, and fine hair across the whole print. Thicker strands between separate features point to temperature or retraction instead.

## Step 2: Lower nozzle temperature, but watch layer bonding

Temperature is the cheapest lever. Bambu's troubleshooting page says to reduce the nozzle temperature when it's high enough to make the melt too runny. Its sticking-nozzle article suggests dropping it by 5-10 °C. Go in 5 °C steps and reprint the same test each time.

There's a tradeoff on load-bearing parts. One PETG guide notes that cooler temperatures may weaken layer adhesion. Polymaker's advice is to find the lowest temperature that still gives smooth walls, reliable extrusion, and strong layer adhesion. If a part will see tension across layers, stop lowering the temperature when you see layer gaps or matte, under-melted walls. Orientation and wall count matter more than a few degrees, as covered in [walls vs infill vs orientation](/posts/3d-print-strength-walls-infill-orientation/).

Speed interacts with temperature too. Bambu's wiki notes that at very low print speeds the filament spends longer in the nozzle, melts more thoroughly and flows freely, so you may see stringing unless you lower the temperature to match. If you slowed a profile down for quality, drop the temperature with it.

## Step 3: What retraction settings reduce stringing?

Retraction depends on your extruder. Bowden machines need a longer pull because the tube adds slack. Prusa's own documentation says the Bowden MINI presets use a much longer retraction length, 3.2 mm by default. Direct-drive Prusa profiles sit much lower, at 0.7-0.8 mm.

Starting points from manufacturers:

| Source | Direct drive | Bowden / indirect | Nozzle range |
| --- | --- | --- | --- |
| Polymaker PETG | 1 mm at 20 mm/s | 3 mm at 40 mm/s | 240-260 °C |
| Polymaker PolyMax PETG | 1 mm at 20 mm/s | 3 mm at 40 mm/s | 230-260 °C |
| Bambu wiki (troubleshooting bump) | 1.2-1.6 mm at 40-60 mm/s | n/a | n/a |
| Prusa profiles (PLA/PETG) | about 0.8 mm | 3.2 mm (MINI) | n/a |

The numbers disagree because extruder geometry and melt-zone length differ between machines. Treat them as a starting range. Change retraction in small increments: one guide suggests 0.2 mm steps on direct drive and 1 mm steps on Bowden, and stopping the moment strings vanish.

More isn't better. Bambu's wiki warns that too much retraction length can easily clog the nozzle. One summary of Bambu's guidance puts the ceiling at no more than 2 mm. The mechanism is that retracting too far pulls soft filament into the cooler zone above the melt zone, where it can jam on re-entry. Prusa's changelog-style advice on speed is similar: a higher retraction speed improves stringing, but too high may skip steps in the motor.

TPU is an exception. Bambu's TPU guide suggests raising retraction by only 0.2 mm if leaking is severe, and warns that excess retraction can cause delayed extrusion and holes in the surface. More on that in the [TPU printing guide](/posts/tpu-printing-guide-settings-direct-drive-brands/).

## Step 4: Wipe, travel, and Z-hop settings

Once moisture, temperature, and retraction are sane, the remaining settings clean up what's left.

**Wipe while retracting.** This moves the nozzle along the last extrusion path during retraction to clean off leaked material. OrcaSlicer's community reference lists it as disabled by default, so it's worth checking whether your profile enables it. Bambu Studio exposes it under filament setting overrides.

**Travel distance.** Fewer long jumps means fewer chances to string. Bambu advises that for plates with multiple models you should reduce the spacing between the models and increase retraction length or speed. Prusa's documentation notes that a higher minimum-travel threshold gives shorter print times but more oozing and stringing. For a fixture with many separate posts, print one at a time or arrange them tightly.

**Z-hop type.** Bambu's retraction page says slope, spiral, and auto lift can effectively reduce oozing and stringing. A straight vertical lift can leave fine lines at layer transitions, so try a non-vertical type before turning Z-hop off entirely.

**Avoid crossing walls.** Routing travels inside the part keeps strings out of sight. One caveat: an OrcaSlicer issue reported that on some layers one side lost its retraction wipe when this was enabled, and a fix pull request followed. If you see one-sided stringing, toggle it and compare.

## How do I test one change at a time?

The common failure mode is changing temperature, retraction, and Z-hop together, then not knowing which one worked. One guide puts it plainly: people change all three at once and can't tell which helped.

OrcaSlicer ships a built-in retraction test, and the wiki points users to the Retraction Test to find optimal settings for your filament. Print a two-tower stringing test or retraction tower. Change one variable, reprint, and record the result per filament and brand, not per spool.

## What if stringing still won't go away?

Check these before you keep tuning:

- **Wrong profile.** Using a profile for another brand or material often brings stringing back, because the default temperature and retraction differ by filament.
- **Worn or mismatched nozzle.** One Bambu-focused guide lists a worn nozzle, or one with a different diameter from the one chosen in the slicer as a cause. Abrasive filaments wear brass quickly, so see [which filaments need a hardened nozzle](/posts/hardened-steel-nozzle-abrasive-filaments/).
- **Over-extrusion.** Flow ratio set too high can also contribute to ooze.
- **Silk or low-density filaments.** These need their own settings, since a standard profile won't fit them.

Also accept that PETG won't ever string like PLA. Some strands are normal, and a quick pass with a heat gun or deburring tool is faster than chasing zero. Fix the settings until the part is clean enough to assemble, then stop.

## The short version

Dry the spool per the manufacturer's numbers, lower the nozzle temperature in 5 °C steps until layer bonding starts to suffer, then set retraction near 1 mm direct drive or 3-5 mm Bowden and adjust in small steps. Turn on wipe, use a slope or spiral Z-hop, and keep travel moves short. That order solves the large majority of stringing before you spend filament on test towers.

## Sources

- [Bambu Lab Wiki: Common print quality problems](https://wiki.bambulab.com/en/knowledge-sharing/common-print-quality-problem)
- [Bambu Lab Wiki: Bambu Studio retraction parameters](https://wiki.bambulab.com/en/software/bambu-studio/parameter/retraction)
- [Polymaker PETG product page and print settings](https://shop.polymaker.com/en-eu/products/petg)
- [Polymaker PolyMax PETG product page](https://shop.polymaker.com/products/polymax-petg)
- [Prusa Knowledge Base: Stringing and oozing](https://help.prusa3d.com/article/stringing-and-oozing_1805)
- [OrcaSlicer Wiki: Retraction](https://www.orcaslicer.com/wiki/printer_settings/extruder/printer_extruder_retraction)
