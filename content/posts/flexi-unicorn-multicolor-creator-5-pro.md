---
title: "Printing a 4-Color Flexi Unicorn on the Flashforge Creator 5 Pro"
date: 2026-11-14
description: "A print-in-place flexi unicorn in four colors on the Flashforge Creator 5 Pro: painting it in Flash Studio, slicing two per plate, and what the toolchanger did well."
slug: flexi-unicorn-multicolor-creator-5-pro
categories: ["Projects"]
tags: ["Creator 5 Pro", "Flashforge", "multi-color", "print-in-place", "Flash Studio"]
cover:
  image: "/images/creator-5-pro-unicorn-print.webp"
  alt: "Four-color print-in-place flexi unicorn printed on a Flashforge Creator 5 Pro"
  caption: ""
  relative: false
draft: false
---

The first real multi-color job on my new [Flashforge Creator 5 Pro](/posts/why-i-chose-flashforge-creator-5-pro/) was a flexi unicorn: a print-in-place toy with a body made of linked segments that wiggle once it comes off the bed. It's a good first test for a toolchanger. It uses four colors with lots of small color regions, and the articulated joints only work if the printer holds its clearances. Here's how it went.

## The model

I used the [Flexi Unicorn on VoxelShare](https://desktop.voxelshare.com/en/models/11599990-flexi-unicorn). It downloads as a single model. The segments, joints, and head print in place as one piece with no assembly and no supports.

I loaded four colors of PLA, one per toolhead, painted the model in Flash Studio (Flashforge's slicer), and printed it.

## Painting it in Flash Studio

![Painting the flexi unicorn in Flash Studio's color painting panel](/images/creator-5-pro-color-painting.webp)
*The color painting panel in Flash Studio. Each numbered swatch is a filament, which maps to one of the four toolheads.*

The body is the base color, white, so anything left unpainted prints white. With the color painting tool open, I picked a filament swatch and painted each detail: the mane, the horn, the hooves, the tail, and the eyes.

The panel gives you a few ways to do it:

- **Fill tools** work well on separate features like the horn, hooves, and tail, because the color stops at the edge of the shape.
- **The circle brush** handles areas that blend into the body, like the mane, and small details like the eyes.
- **Section view** cuts away part of the model so you can reach spots that are hard to see, like the undersides of the hooves.

Zoom in close on the edges. The color boundary follows the mesh triangles, so a quick stroke near an edge prints as a jagged line. The full painting walkthrough, with every control on that panel, is in my [Creator 5 Pro multi-color guide](/posts/creator-5-pro-multicolor-printing-guide/).

## Slicing two at once

![Two painted flexi unicorns sliced on the Creator 5 Pro build plate](/images/creator-5-pro-unicorn-sliced.webp)
*Two unicorns on one plate in the slicer preview*

I put two on the plate. With a toolchanger, the extra copy costs very little in waste, because each color change is a toolhead swap plus a small prime, not a full filament purge. On a single-nozzle AMS-style printer, every color change on every layer purges filament, and doubling the parts roughly doubles the color changes.

The slicer preview is the best place to catch painting mistakes, like a stray patch of pink on the body or a hoof that missed its fill. It's much easier to fix here than after a print.

## The result

![The finished four-color flexi unicorn in hand](/images/creator-5-pro-unicorn-print.webp)

It came off the plate in white, pink, purple, and navy PLA, with the body segments linked and flexing as designed. The color boundaries on the mane and hooves came out crisp.

One thing you'll notice: the colors on the print don't match the slicer preview exactly. The horn printed purple and the tail navy. The slicer colors are just for the preview. What prints is whatever filament is loaded in each toolhead. So you can paint with whatever colors read clearly on screen and decide the real colors when you load the spools.

## What I'd tell someone trying this

- **Run the toolhead offset calibration first.** Print-in-place joints and clean color boundaries both depend on all four toolheads being aligned. My [multi-color guide](/posts/creator-5-pro-multicolor-printing-guide/) covers when to rerun it.
- **Pick a model with separate features for your first try.** Horns, hooves, and tails fill cleanly. Blended areas, like a mane that fades into the head, take more brush work.
- **Keep the prime tower on.** It's what keeps the color changes clean.
- **Dry your filament.** Wet filament strings, and on a multi-color print every string is a different color. My [filament drying guide](/posts/how-to-dry-filament-dryer-box-vs-dehydrator-vs-heated-bed/) covers temperatures and times.

Flexi toys are a fun way to learn the multi-color workflow, but the same painting and slicing steps carry straight over to functional parts, like a TPU grip painted onto a rigid handle or a contrasting label on a jig. That's where I'm headed next with this printer.

If you're thinking about getting one, the Creator 5 Pro is [$749 for Black Friday](/posts/black-friday-3d-printer-filament-deals-2026/), $200 off its regular price.
