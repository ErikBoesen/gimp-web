Title: GIMP 2.9.6 Released
Date: 2017-08-24
Category: News
Authors: Alexandre Prokoudine
Slug: gimp-2-9-6-released
Summary: After more than a year of hard work we are excited to release GIMP 2.9.6 featuring many improvements, some new features, translation updates for 23 languages, and 204 bug fixes.

After more than a year of hard work we are excited to release GIMP 2.9.6
featuring many improvements, some new features, translation updates for 23
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

<figure>
    <img src="{filename}gimp-2-9-6-system-resources.png" alt="Setting amount of threads in GIMP 2.9.6" width='772' height='660' />
</figure>

## GUI, Usability, and Configurability

Benoit Touchette improved mask creation workflow for users who use a ton of
masks in their projects. Now GIMP remembers the last type of mask
initialization, and you can use key modifiers + mouse click on layer previews
to create, apply, or remove masks. There’s a new button in the *Layers*
dockable dialog for that as well.

<figure>
    <img src="{filename}gimp-2-9-6-create-mask.png" alt="Easily create new mask with GIMP 2.9.6" width='418' height='431' />
</figure>

To make that feature possible, Michael Natterer introduced saving of last
dialogs' settings across sessions and made these defaults configurable via the
new *Interface / Dialog Defaults* page in the *Preferences* dialog.

<figure>
    <img src="{filename}gimp-2-9-6-dialog-defaults.png" alt="Configurable Dialog Defaults in GIMP 2.9.6" width='772' height='660' />
</figure>

Additionally, the *Preferences* dialog got a vertical scrollbar where
applicable to keep its height more sensible, and settings on individual pages
of the dialog can be reset separately now.

The *Quit* dialog got a few updates: automatically exiting when all the images
in the list have been saved, and a *Save As* button for every opened image
(clicking an image in the list will raise it easy checks).

<figure>
    <img src="{filename}gimp-2-9-6-fill-with.png" alt="Configurable Fill With option in GIMP 2.9.6" width='361' height='597' />
</figure>

Yet another new feature is an option (on the screenshot above) to choose fill
color or pattern for empty spaces after resizing the canvas.

## Better Hi-DPI Support

While most changes for better Hi-DPI displays support are planned for v3.0, when
GIMP is expected to be based on either GTK+3 or GTK+4, we were able to remove at
least some of the friction by introducing icon sizes at different resolutions
and a switch for icon sizes on the *Icon Theme* page of the *Preferences*
dialog.

<figure>
    <img src="{filename}gimp-2-9-6-icon-themes.png" alt="Configurable icon size in GIMP 2.9.6" width='772' height='660' />
</figure>

## On-canvas Interaction Changes

Michael Natterer did a huge under-the-hood work that is likely to affect user
interaction with GIMP bigly. Simply put, he moved a lot of on-canvas code
from tools like *Rectangle Select*, *Measure* and *Path* into reusable code.

The effect of that is multifold:

* New tools can reuse on-canvas elements of other tools (adding shape drawing
tools should be easier now, although we are not planning that for 2.10,
unless someone sends a clean patch).
* GEGL-based filters can be interacted with directly on the canvas
(*Spiral* and *Supernova* so far as test case).

<p>
<video width="880" height="528" controls>
  <source src="https://download.gimp.org/mirror/pub/gimp/video/v2.9/gimp-2-9-6-spiral-filter.webm" type="video/webm">
  <source src="https://download.gimp.org/mirror/pub/gimp/video/v2.9/gimp-2-9-6-spiral-filter.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>
</p>

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

Thanks to Øyvind Kolås and his
[Patreon supporters](https://www.patreon.com/pippin), GIMP now also has a
simple 'blendfun' framework that greatly simplifies implementing new color
modes. Ell made use of that by adding Linear Burn, Vivid Light, Linear Light,
Pin Light, Hard Mix, Exclusion, Merge, Split, and Luminance (RGB) blending modes
(most of them now also supported in the PSD plug-in).

Another prominent change is the introduction of the Pass Through mode for layer
groups. When this mode is used instead of any other one, GIMP mixes layers
inside that group directly to the layers below, skipping creation of the group
projection. The feature was implemented by Ell. The screenshot below features a
user-submitted PSD file that has TEXTURES layer group in the Pass Through mode,
as opened in GIMP 2.9.4 (left) and GIMP 2.9.6 (right).

<figure>
    <img src="{filename}gimp-2-9-6-pass-through.jpg" alt="Pass Through mode vs no Pass Through mode" width='960' height='586' />
</figure>

Newly added color tags simplify managing large projects with a lot of layers
and layer groups. The screenshot below is a real-life PSD file opened in GIMP
2.9.6.

<figure>
    <img src="{filename}gimp-2-9-6-color-tags-psd-xcf.png" alt="New User Interface Themes" width='468' height='674' />
</figure>

To make more use of that feature, we need someone to step up and implement
multiple layers selection. For an initial research, see
[this wiki page](https://gui.gimp.org/index.php?title=Multi-layer_selection_workgroup).

For full access to all the new features, we updated the *Layer Attributes*
dialog to provide the single UI for setting layer's name, blending mode,
opacity, and offset, toggling visibility, link status, various locks,
color tags.

<figure>
    <img src="{filename}gimp-2-9-6-layer-attributes-dialog.png" alt="Updated Layer Attributes dialog" width='608' height='579' />
</figure>

## CIE LCH and CIE LAB

Under the influence of Elle Stone (and with her code contributions), CIE LCH
and CIE LAB color spaces are finding more use in GIMP now.

Color dialogs now have an LCH color selector that, in due time, will most
likely replace outdated HSV selector for reasons outlined by Elle in
[this article](http://ninedegreesbelow.com/photography/determine-image-tonality-and-palette-part-1.html).
The LCH selector also supports gamut checking.

A new *Hue-Chroma* filter in the *Colors* menu works much like *Hue-Saturation*,
but operates in CIE LCH color space. Moreover, the *Fuzzy Select* and the
*Bucket Fill* tool now can select colors by CIE L, C, and H.

Finally, both the *Color Picker* and the *Sample Points* dialog now display
pixel values in CIE LAB and CIE LCH.

<figure>
    <img src="{filename}gimp-2-9-6-sample-points-lch-lab.jpg" alt="Sample points in LCH and LAB, GIMP 2.9.6" width='767' height='355' />
</figure>

## Tools

New *Handle Transform* tool contributed	by Johannes Matschke in 2015 has
been finally cleaned up by Michael Natterer and available by default. It's
a little tricky to get used to, but we hear reports that once you get the
hang of it, you love it.

Thanks to Ell, the *Warp Transform* tool is now a lot faster, partially thanks
to a switch that toggles high-quality preview that isn't always necessary.

<p>
<video width="856" height="566" controls>
  <source src="https://download.gimp.org/mirror/pub/gimp/video/v2.9/gimp-2-9-6-warp-transform.webm" type="video/webm">
  <source src="https://download.gimp.org/mirror/pub/gimp/video/v2.9/gimp-2-9-6-warp-transform.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
</p>

All transformation tools don't display grid by default anymore, and during
an interactive transformation the original layer gets hidden now. The latter
greatly simplifies transforming upper layer in relation to a lower layer.
Before that, the original layer used to block the view.

*Free Select* tool now waits for Enter being pressed to confirm selection, which
enables you to tweak positions of polygonal selection.

## Painting

An important new feature that is somewhat easy to overlook is being able to
paint on transparent layers with modes other than normal.

Thanks to shark0r, the *Smudge* tool now has a *Flow* control that allows mixing
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
at both importing and exporting: Linear Burn, Linear Light, Vivid Light,
Pin Light, and Hard Mix blending modes. It also finally supports exporting
layer groups and reads/writes the Pass Through mode in those. Additionally,
GIMP now imports and exports color tags from/to PSD files.

## WebP support

We already shipped GIMP 2.9.2 with initial support for opening and exporting
WebP files, however the plug-in was missing a number of essential features.
Last year, we replaced it with a pre-existing plug-in initially written by
[Nathan Osman](https://github.com/nathan-osman) back in 2011 and maintained
through the years. We now ship it by default as part of GIMP.

<figure>
    <img src="{filename}gimp-2-9-6-webp-exporting.jpg" alt="WebP exporting in GIMP 2.9.6" width='772' height='561' />
</figure>

The new plug-in received additional contributions from Benoit Touchette and
Pascal Massimino and supports both ICC profiles, metadata loading/exporting,
and animation.

## Metadata Viewing and Editing

Thanks to Benoit Touchette, GIMP now ships a new metadata viewer that
uses Exiv2 to display Exif, XMP, IPTC, and DICOM metadata (the latter
is displayed on the XMP tab).

<figure>
    <img src="{filename}gimp-2-9-6-metadata-viewer.jpg" alt="Metadata viewer in GIMP 2.9.6" width='772' height='601' />
</figure>

Moreover, Benoit implemented a much anticipated metadata editor that
supports adding/editing writing XMP, IPTC, DICOM, and GPS/Exif metadata,
as well as loading/exporting metadata from/to XMP files.

<figure>
    <img src="{filename}gimp-2-9-6-metadata-editor.jpg" alt="Metadata editor in GIMP 2.9.6" width='772' height='608' />
</figure>

## Filters

Thanks to contributions from Thomas Manni and Ell, GIMP now has 9 more
GEGL-based filters, including much anticipated *Wavelet Decompose*, as well
as an *Extract Component* plug-in that simplifies fetching e.g. CMYK's K
channel or LAB's L* channel from an image.

Another new feature that we expect to develop further is GUM—a simple
metadata language that helps automatically building more sensible UI for
GEGL filters. Here's a quick video:

<p>
<video width="384" height="544" controls>
  <source src="https://download.gimp.org/mirror/pub/gimp/video/v2.9/gimp-2-9-6-gegl-dynamic-op-ui.webm" type="video/webm">
  <source src="https://download.gimp.org/mirror/pub/gimp/video/v2.9/gimp-2-9-6-gegl-dynamic-op-ui.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>
</p>

## Resources and Presets

To make GIMP more useful by default, we now ship it with some basic presets
for the *Crop* tool: 2&times;3, 3&times;4, 16:10, 16:9, and Square.

Documents templates have been updated and now feature popular, contemporary
presets for both print and digital media.

## What's Next

We still have a bunch of bugs to fix before we can release 2.10 and we
appreciate all the huge and tiny useful patches contributors send us to that
effect.

GIMP 2.9.8 is expected to ship with more bug fixes and an updated *Blend*
(*Gradient Fill*) tool that works completely on canvas, including adding and
removing color stops and assigning colors.