Title: GIMP 2.9.6 Released
Date: 2017-08-22
Category: News
Authors: Alexandre Prokoudine
Slug: gimp-2-9-6-released
Summary: After more than a year of hard work we are excited to release GIMP 2.9.6
featuring many improvements, some new features, translation updates for 22
languages, and 204 bug fixes.

After more than a year of hard work we are excited to release GIMP 2.9.6
featuring many improvements, some new features, translation updates for 22
languages, and 204 bug fixes.

As usual, for a complete list of changes please see
[NEWS](https://git.gnome.org/browse/gimp/tree/NEWS). Here we'd like to focus
on the most important changes.

## Performance

GIMP now has support for experimental multi-threading in GEGL and will try to
use as many cores as are available on your computer.

We know GIMP can explode when using more than one core, but we keep it that way
so that we get as many bug reports as possible for this officially unstable
development version. This is because we really, really want to ship GIMP 2.10
with usable parallel processing.

On the other hand, you can always set the amount of cores to 1 if you couldn't
be bothered to report bugs. For that, please tweak the amount of threads on the
*System Resources* page of the *Preferences* dialog.

## GUI, Usability, and Configurability

Benoit Touchette improved mask creation workflow for users who use a ton of
masks in their projects. Now GIMP remembers the last type of mask
initialization, and you can use key modifiers + mouse click on layer previews
to create, apply, or remove masks. There’s a new button in the *Layers*
dockable dialog for that as well.

To make that feature possible, Michael Natterer introduced saving of last
dialogs' settings across sessions and made these defaults configurable via the
new *Interface / Dialog Defaults* page in the *Preferences* dialog.

[screenshot]

Additionally, the *Preferences* dialog got a vertical scrollbar where
applicable to keep its height more sensible, and settings on individual pages
of the dialog can be reset separately now.

The *Quit* dialog got a few updates: automatically exiting when all the images
in the list have been saved, and a *Save As* button for every opened image
(clicking an image in the list will raise it easy checks).

## On-canvas Interaction Changes

Michael Natterer did a huge under-the-hood work that is likely to affect user
interaction with GIMP bigly. Simply put, he moved a lot of on-canvas code
from tools like Rectangle Select, Measure and Paths into reusable code.

The effect of that is multifold:

* New tools can reuse on-canvas elements of other tools (adding shape drawing
tools should be easier now, although we are not planning that for 2.10,
unless someone sends a clean patch).
* GEGL-based filters can be interacted with directly on the canvas
(Spiral and Supernova so far as test case).

[video from https://streamable.com/7zvs4]

So far one still needs to write C code to make a GEGL-based filter use
on-canvas interaction. We expect to spend some time figuring out a way to
simplify this, possibly using the GUM language (see below).

## Layers, Linear and Perceptual Workflows

Since we want to make workflows in linear color spaces more prominent in GIMP,
it was time to update the blend modes code. You can now switch between two
sets of layer modes: legacy (perceptual) and default (linear). The user
interface for switching was a quick design, we'd like to come up with something
better, so we are interested in your input.

Moreover, we made both compositing of layers and blending color space
configurable, should you have the need to use that for advanced image
manipulation.

We also added a new *Colors -> Linear Invert* command to provide
radiometrically correct color inversion. And the histogram dialog now features
a toggle between gamma and linear modes—again, it's a design we'd like to
improve.

Thanks to Øyvind Kolås and his Patreon supporters GIMP now also has a simple
'blendfun' framework that greatly simplifies implementing new color modes. Ell
made use of that by adding Linear Burn, Vivid Light, Linear Light, Pin Light,
Hard Mix, Exclusion, Merge, Split, and Luminance (RGB) blending modes (most of
them now also supported in the PSD plug-in).

Newly added color tags simplify managing large projects with a lot of layers
and layer groups. To make more use of that, we need someone to step up and
implement multiple layers selection. For an initial research, see
[this wiki page](https://gui.gimp.org/index.php?title=Multi-layer_selection_workgroup).

For full access to all the new features, we updated the Layer Attributes
dialog to provide the single UI for setting layer's name, blending mode,
opacity, and offset, toggling visibility, link status, various locks,
color tags.

[screenshot]

## CIE LCH and CIE LAB

Under the influence of Elle Stone (and with her code contributions), CIE LCH
and CIE LAB color spaces are finding more use in GIMP now.

Color dialogs now have an LCH color selector that, in due time, will most
likely replace outdated HSV selector for reasons outlined in
[this article](http://ninedegreesbelow.com/photography/determine-image-tonality-and-palette-part-1.html).
The LCH selector also supports gamut checking.

A new *Hue-Chroma* filter in the Colors menu works much like *Hue-Saturation*,
but operates in CIE LCH color space. Moreover, the *Fuzzy Select* and the
*Bucket Fill* tool now can select colors by CIE L, C, and H.

Finally, both the *Color Picker* and the *Sample Points* dialog now display
pixel values in CIE LAB and CIE LCH.

## Tools

New *Handle Transform* tool contributed	by Johannes Matschke in 2015 has
been finally cleaned up by Michael Natterer and available by default. It's
a little tricky to get used to, but we hear reports that once you get the
hang of it, you love it.

Thanks to Ell, the *Warp Transform* tool is now a lot faster, partially thanks
to a switch that toggles high-quality preview that isn't always necessary.

All transformation tools don't display grid by default anymore, and during
an interactive transformation the original layer gets hidden now. The latter
greatly simplifies transforming upper layer in relation to a lower layer.
Before that, the original layer used to block the view.

Free Select tool now waits for Enter being pressed to confirm selection, which
enables you to tweak positions of polygonal selection.

## Painting

An important new feature that is somewhat easy to overlook is being able to
paint on transparent layers with modes other than normal.

Thanks to shark0r, the Smudge tool now has a Flow control that allows mixing
in both constant and gradient color while smudging. There's another new option
to never decrease alpha of existing pixels while smudging in the tools options
now as well. For more on this, please read
[this forum thread](https://www.gimp-forum.net/Thread-Customized-smudge-tool-Smudge-with-painting).

Canvas rotation has been improved: it got snappier in certain cases, and
rulers, scrollbars, as well as the Navigation dialog follow the rotation now.

Alexia introduced some improvements to the brush engine. For bitmap brushes,
GIMP now caches hardness and disables dynamic change of hardness to improve
painting performance. Bitmap brushes also don't get clipped anymore, when
hardness is less than 100. Plus there's a specialized convolution algorithm
for the hardness blur to make it faster now.

## Processing Raw Images

Since 2.9.4, GIMP is capable of opening raw (digital camera) images via
[darktable](http://www.darktable.org), and the plan was to open it up to more
plug-in developers, because nothing sparks a thoughtful, civil conversation
like a raw processor of choice.

This is now possible: 2.9.6 ships with a RawTherapee plug-in (v5.2 or newer
should be installed) and a new file-raw-placeholder plug-in that registers
itself for loading all raw formats, but does nothing except returning an error
message pointing to darktable and RawTherapee, if neither is installed.

Moreover, you can now choose preferred raw plug-in, when multiple options are
available on your computer. For this, open the *Preferences* dialog and go to
the *Image Import* page, then click on the plug-in you prefer and click OK to
confirm your choice. You will need to restart GIMP.

## Better PSD Support

The PSD plug-in now supports a wider range of blending modes for layers,
at both importing and exporting: linear burn, linear light, vivid light,
pin light, and hard mix layer modes. It also finally supports exporting
layer groups and reads/writes pass-through mode in those. Additionally,
GIMP now imports and exports color tags from/to PSD files.

## Metadata Viewing and Editing

Thanks to Benoit Touchette, GIMP now ships a new metadata viewer that
uses Exiv2 to display Exif, XMP, IPTC, and DICOM metadata (the latter
is displayed on the XMP tab).

[screenshot]

Moreover, Benoit implemented a much anticipated metadata editor that
supports adding/editing writing XMP, IPTC, DICOM, and GPS/Exif metadata,
as well as loading/exporting metadata from/to XMP files.

[screenshot]

## Filters

Thanks to contributions from Thomas Manni and Ell, GIMP now has 9 more
GEGL-based filters, including much anticipated Wavelet Decompose, as well
as an Extract Component plug-in that simplifies fetching e.g. CMYK's K
channel or LAB's L* channel from an image.

Another new feature that we expect to develop further is GUM—a simple
metadata language that helps automatically building more sensible UI for
GEGL filters. Here's a quick video:

[video from https://streamable.com/ajbi4]

## Resources and Presets

To make GIMP more useful by default we now ship it with some basic presets
for the Crop tool: 2×3, 3×4, 16:10, 16:9, and Square.

Documents templates have been updated and now feature popular, contemporary
presets for both print and digital media.

## What's Next

We still have a bunch of bugs to fix before we can release 2.10 and we
appreciate all the huge and tiny useful patches contributors send us to that
effect.

GIMP 2.9.8 is expected to ship with more bug fixes and an updated Blend
(Gradient Fill) tool that works completely on canvas, including adding and
removing color stops and assigning colors.