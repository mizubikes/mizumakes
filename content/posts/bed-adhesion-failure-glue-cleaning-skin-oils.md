---
title: "How Bad Bed Adhesion Ruins Prints, and How to Fix It"
date: 2026-11-26
description: "One part letting go of the plate can turn a print into spaghetti. Why small parts lose adhesion, and how glue, plate cleaning, and clean hands fix it."
slug: bed-adhesion-failure-glue-cleaning-skin-oils
categories: ["Guides"]
tags: ["bed adhesion", "build plate", "textured PEI", "troubleshooting", "print-in-place"]
cover:
  image: "/images/bed-adhesion-failure-flexi-dog-cover.webp"
  alt: "Two yellow and pink flexi dog prints on a workbench: the left one failed into a mess of spaghetti, the right one printed cleanly"
  caption: "Same flexi dog model. Left: a section lost its grip on the plate. Right: a clean print."
  relative: false
draft: false
---

*MizuMakes may earn a commission from links in this post.*

The two flexi dogs above are the same model. The one on the right came off the plate clean, with every joint moving. The one on the left lost bed adhesion partway through, and from that point on the printer was laying plastic into the air. You can see the result: a body buried in tangled strands, loose segments, and spaghetti everywhere.

Nothing was wrong with the model or the slicer settings. The plate just didn't hold. Here's why that happens, why print-in-place toys are especially vulnerable, and the three things I now do to stop it: glue on the plate, cleaning the plate, and keeping my hands off the print surface as much as possible.

## What actually went wrong

![Underside of the failed flexi dog: yellow body and legs intact, with a pink tail segment turned into a tangle of spaghetti](/images/bed-adhesion-failure-tail-spaghetti.webp)
*The underside of the failed dog. The textured-PEI pattern is printed cleanly into the body and legs, but the pink tail segment came loose and turned into spaghetti.*

Flip the failed dog over and the problem is easy to read. The body and legs have the full textured-plate pattern on their undersides, so those parts stayed put. The tail segment didn't. Once a part comes loose, the nozzle keeps printing where the part used to be. The plastic has nothing to land on, so it piles up as strings. Those strings then drag into neighboring parts, which is how one small failure takes out the whole print.

## Why flexi and print-in-place toys fail first

A flexi toy isn't one part on the plate. It's a dozen small islands: each leg, each tail segment, and the joints between them. Each island has to hold on by itself.

Bambu Lab puts the physics plainly: the force between the print and the build plate is roughly proportional to their contact area. A small tail link has a tiny footprint, so it has very little grip. That small grip still has to resist the nozzle dragging across it, the part cooling and shrinking, and the toolhead moving around it. Tall, thin parts make it worse because the nozzle has more leverage to knock them over.

So on a print like this, adhesion isn't a first-layer issue you can forget about once layer one looks good. The smallest island sets the limit for the whole plate.

## Fix 1: Clean the plate with soap and water

Most adhesion problems on a PEI plate come down to contamination: skin oils, leftover residue, and dust. Bambu's cleaning guide for the textured PEI plate says to use warm water and dish soap, not alcohol, because "alcohol might just spread the oils on the print surface instead of removing it." Scrub with a sponge or a soft brush so the soap gets down into the texture, rinse, and dry with a paper towel.

Prusa takes a slightly different approach for smooth PEI. It recommends 90%+ isopropyl alcohol as the everyday degreaser, with dish soap every so often to remove the oils IPA leaves behind. Prusa also says not to use acetone at all on textured sheets. For a textured plate, I'd follow Bambu: soap and water.

If a plate still won't hold after a good wash, Bambu suggests lightly scuffing the textured surface with fine sandpaper or steel wool to expose fresh PEI. Then wash off every bit of the dust.

## Fix 2: Use glue on the plate

A thin layer of glue stick gives small parts much more grip. Prusa recommends a basic PVA glue stick and notes that glue also creates a protective separation layer, which helps with materials like PETG that can bond too hard to PEI. The glue washes off with dish soap and water, so it doesn't permanently change the plate. Use a plain PVA stick, not a "permanent" glue, and as Prusa puts it, "Don't put Superglue on your sheet!"

Apply a thin, even coat over the area the parts will sit on, and let it dry before printing. A common pick is a [washable PVA glue stick](https://www.amazon.com/s?k=Elmers+disappearing+purple+glue+stick&tag=mizubikes-web-20). The purple kind dries clear, so you can see where you've already covered.

## Fix 3: Keep your hands off the print surface

This is the habit that undoes all the cleaning. Bambu says it directly: "The natural oils from your hands can transfer to the printing surface, impacting the sheet's adhesion properties." It also says to handle the plate from the sides.

In practice, that means:

- Pick up the plate by its edges or the tab, never by the center.
- Pop prints off by flexing the plate, not by pressing on the surface with your palm.
- After washing, don't run a finger across the surface to "check" it.
- If you do touch it, wash it again before the next important print.

## Other settings that help small parts hold

If you've cleaned, glued, and kept your hands off, and small islands still lift, these are the next things to try. All are from Bambu's own troubleshooting page:

- **Add a brim** to small parts. A brim adds contact area, which is exactly what tiny tail links are missing.
- **Raise the bed temperature a few degrees.** Higher bed temperatures generally mean stronger adhesion. Don't go too far with PLA and PETG, though, or you'll get elephant's foot and clog risk.
- **Use a slightly thicker first layer** (Bambu suggests 0.25 mm layer height and 0.5 mm line width) if problems persist.

It also helps to match the plate to the filament. My [textured PEI vs smooth PEI vs cool plate comparison](/posts/textured-pei-vs-smooth-pei-vs-cool-plate/) covers which surface suits which material. Wet filament causes its own first-layer trouble, so see [how to dry filament](/posts/how-to-dry-filament-dryer-box-vs-dehydrator-vs-heated-bed/) if your spool has been sitting out.

## Quick checklist before a print-in-place job

1. Wash the plate with dish soap and warm water, rinse, and dry it.
2. Handle it only by the edges from then on.
3. Add a thin layer of PVA glue stick where the small parts will sit.
4. Add a brim to any small or thin islands.
5. Watch the first few layers, and stop the print the moment a part shifts.

Flexi toys are a great way to find adhesion problems, because they have so many small footprints. Get them to print cleanly and your functional parts will stick too. For another multi-color flexi print, see the [4-color flexi unicorn on the Creator 5 Pro](/posts/flexi-unicorn-multicolor-creator-5-pro/).

## Sources

- [Bambu Lab Wiki: Textured PEI plate cleaning guide](https://wiki.bambulab.com/en/filament-acc/acc/pei-plate-clean-guide)
- [Bambu Lab Wiki: Textured PEI plate not working as expected](https://wiki.bambulab.com/en/general/textured-PEI-plate-not-working-as-expected)
- [Prusa Knowledge Base: PEI print surface preparation](https://help.prusa3d.com/article/6Gtws6Yqjg-pei-print-surface-preparation)
