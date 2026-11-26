---
title: "Best Slicer Settings to Reduce Stringing: Tuning Order"
date: 2026-11-25
description: "The best slicer settings to reduce stringing, in the order to change them: dry the spool, then temperature, retraction, travel, and wipe, with starting numbers."
slug: best-slicer-settings-to-reduce-stringing
categories: ["Guides"]
tags: ["stringing", "slicer settings", "retraction", "troubleshooting"]
cover:
  image: "/images/best-slicer-settings-to-reduce-stringing-cover.webp"
  alt: "Close-up of a 3D printer nozzle extruding molten plastic onto a print"
  caption: "Photo: ZMorph3D / Pixabay"
  relative: false
draft: false
---

*MizuMakes may earn a commission from links in this post.*

The best slicer settings to reduce stringing are, in order: dry the filament, lower nozzle temperature in 5 °C steps, set retraction to a modest calibrated value, and then cut down on travel moves over open air. Most people reverse that order and crank retraction first. That usually trades hairs for clogs and weak spots in the walls.

For functional parts, stringing is mostly cosmetic until it isn't. Strings across a bearing bore, a sealing face, or a snap-fit clearance matter. So does the under-extrusion that over-aggressive retraction leaves behind. Here is a tuning order that treats it as a process-control problem.

## What actually causes stringing?

Stringing is molten plastic leaking out of the nozzle while the head travels between features. Bambu Lab's slicer documentation describes the mechanism as heat plus internal nozzle pressure pushing melt out even when you aren't commanding extrusion. Retraction pulls filament back before the move, which lowers the melt pressure and reduces the chance of a string on the travel path.

Three things feed the leak: viscosity (temperature), pressure (retraction and flow), and time (travel distance and speed). Moisture is a fourth, and it is the one that slicer settings can't fix. Bambu's wiki says damp filament is more prone to stringing and usually can't be fully solved by adjusting retraction.

## Step 1: Dry the spool before touching the slicer

If the strings are fine, hairy, and accompanied by popping or rough surfaces, dry first. Re-tuning a profile around wet filament gives you settings that only work until the spool changes.

Drying numbers vary by manufacturer. For PLA, Bambu Lab gives 50 °C for 8 hours in a forced-air oven, Polymaker 55 °C for 6 hours, and Prusa 45 °C for 6 hours. For PETG, one chart compiled from Bambu's data lists 60–65 °C for 8 hours in a convection oven, against 55 °C for 6 hours for Prusament. TPU is the most demanding: Bambu says to always dry it before printing. The full method comparison is in my [filament drying guide](/posts/how-to-dry-filament-dryer-box-vs-dehydrator-vs-heated-bed/). A [filament dryer](https://www.amazon.com/s?k=filament+dryer&tag=mizubikes-web-20) with a sealed print-side feed matters more than any single slicer tweak for hygroscopic materials.

## Step 2: Lower the nozzle temperature in 5 °C steps

Temperature is the cleanest lever because it changes viscosity without touching extrusion mechanics. Bambu's troubleshooting page says that a nozzle that is too hot makes the melt too thin, so you should reduce the temperature. Prusa's stringing guidance, as summarized by one reference, suggests dropping 5–10 °C and checking whether the strings thin out.

Don't drop so far that you hurt layer adhesion, which is already the weak axis in printed parts. Stop when the strings are gone or when you see gaps in walls. Check the manufacturer's range first. Prusament PETG's data sheet lists 250 ± 10 °C for the extruder, while the flame-retardant V0 version is rated 230 ± 10 °C. Third-party testing summaries suggest 230–240 °C on a P1S, down from the 245–250 °C default. That is community reporting rather than a spec, so treat it as a place to begin a temperature tower, not a target.

If you are choosing PETG for a functional part, the [PETG brand comparison](/posts/best-petg-filament-brands-functional-parts/) covers how published ranges differ by manufacturer.

## What retraction settings reduce stringing?

Retraction gets the most attention and is the easiest to overdo. Starting points depend on the extruder path.

On direct drive, Prusa's own profiles sit at 0.7–0.8 mm. Prusa's Bowden MINI is the opposite case, where the presets use a much longer default of 3.2 mm. Bambu's guidance is that too large a retraction length easily causes clogs, and it generally shouldn't exceed 2 mm. Prusa's support staff make a similar point, advising a maximum of 2 mm in PrusaSlicer.

For retraction speed, community guidance clusters around 30–40 mm/s on direct drive. Too slow leaves the melt oozing during the pull. Prusa notes that a higher speed improves stringing, but too high may skip steps in the motor. Treat the 30–40 figure as a starting band, not a data-sheet number.

The over-retraction failure mode matters for load-bearing parts. Pull too far and you drag melt into the cold zone, which causes jams and voids at restart points. Those voids sit in your perimeters, which are the walls carrying load. If you see gaps right after travel moves, you have gone too far.

## Use the retraction test instead of guessing

Orca's wiki puts retraction last in the calibration order: after flow and pressure advance, so the printer is already extruding properly. The built-in test varies length with height on two towers. One reference suggests 0 to 2 mm in 0.1 mm steps for direct drive, and roughly 1 to 6 mm in 0.2 mm steps for Bowden. Pick the shortest length where strings disappear and save it to the filament profile.

The order matters because retraction can't compensate for the other variables. If stringing persists, revisit temperature and flow first, since retraction can't fix a problem that's really moisture or heat.

## Travel, wipe, and seam settings that cut strings

Once temperature and retraction are reasonable, reduce the opportunities for a string to form.

Avoid crossing walls is the main one. Bambu's wiki lists it as a fix for stringing: enabling "Avoid crossing walls" reduces the probability of stringing. The cost is longer routed travel, so it adds a little print time.

Plate layout counts too. When parts are spread far apart, Bambu says to reduce spacing between models and, if needed, raise retraction length or speed slightly. Printing by object keeps the head close to the part it's working on, and Bambu's TPU guide specifically warns against excessive travel moves, including layer-by-layer printing across many models.

Travel speed helps on printers that are slow by default. One compiled guide recommends 150–250 mm/s for travel moves, but that is not a vendor spec. Bambu presets already travel fast, so on those machines there is nothing to gain. Stringing there is more often a temperature or moisture issue.

Wipe while retracting drags the nozzle across the path just printed to clean off residual ooze. Several tuning guides recommend it for PETG. On Bambu and Orca, Z-hop type also matters, since Bambu says slope, spiral, and auto lift can effectively reduce oozing and stringing. A plain vertical hop is the worse choice here.

Minimum travel before retraction is a trade-off. Prusa warns that raising it shortens print time but increases oozing and stringing. Keep the default unless you have a reason.

## Material-specific notes

PLA is the easy case: dry, drop temperature by 5–10 °C, leave retraction near stock. Bambu's own PLA profile is a decent baseline. One third-party guide puts stock Bambu retraction around 0.8 mm on most profiles.

PETG strings by nature. It is hygroscopic, with Prusa's data sheet listing 0.10% moisture absorption in 7 days for standard Prusament PETG. Some residual stringing is normal. Its low warping and good layer adhesion are why it's used for brackets and enclosures, so a few wisps that clean off with a deburring tool are a reasonable trade. My [PLA vs PETG comparison](/posts/pla-vs-petg/) covers when to pick it.

TPU wants a different approach. Orca's reference page, a third-party summary, suggests little to no retraction, 0.2–0.5 mm at most, because soft filament compresses rather than pulling back. Dry it, print by object, and use the settings in the [TPU printing guide](/posts/tpu-printing-guide-settings-direct-drive-brands/).

## When stringing isn't a slicer problem

If you've dried the spool, lowered temperature, calibrated retraction, and strings remain, look at hardware and filament. Candidates include a worn or mismatched nozzle (check the slicer diameter matches), a loose or dirty wiper, or low-density filaments. For the last, Bambu says to reduce print temperature and set flow ratio between 0.5 and 0.7. A heat-creep-prone hotend with a long retraction value will also look like stringing but is really partial jamming.

For parts where cosmetics don't matter, such as jigs, fixtures, and hidden brackets, I'd stop at the first clean test tower and move on. Tuning for zero strings costs strength and time. Where it does matter (clearance fits, sealing surfaces, snap-fit features), pair these settings with the wall and orientation choices in the [strength guide](/posts/3d-print-strength-walls-infill-orientation/).

## Sources

- [Bambu Lab Wiki: Stringing and oozing](https://wiki.bambulab.com/en/filament-acc/filament/print-quality/stringing-oozing)
- [Bambu Lab Wiki: Retraction parameters](https://wiki.bambulab.com/en/software/bambu-studio/parameter/retraction)
- [Prusa Knowledge Base: Stringing and oozing](https://help.prusa3d.com/article/stringing-and-oozing_1805)
- [OrcaSlicer Wiki: Calibration](https://github.com/OrcaSlicer/OrcaSlicer/wiki/Calibration)
- [Prusament PETG technical data sheet](https://www.prusa3d.com/file/2765253/prusament-petg-technical-data-sheet.pdf)
- [Bambu Lab Wiki: TPU printing guide](https://wiki.bambulab.com/en/knowledge-sharing/tpu-printing-guide)
