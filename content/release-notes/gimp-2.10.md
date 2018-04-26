Title: GIMP 2.10 Release Notes
Date: 2018-04-26
Authors: Wilber
Status: hidden

## Introduction

GIMP 2.10 is the result of six years of work that originally focused on porting
the program to a new image processing engine, GEGL. However the new version
ships with far more new features, including new and improved tools, better file
formats support, various usability improvements, revamped color management
support, a plethora of improvements targeted at digital painters and
photographers, metadata editing, and much, much more.

## Updated user interface and initial HiDPI support

One thing immediately noticeable about GIMP 2.10 is the new dark theme and
symbolic icons enabled by default. This is meant to somewhat dim the environment
and shift the focus towards content.

FIXME screenshot

There are now 4 user interface themes available in GIMP: Dark (default), Gray,
Light, and System. Icons are now separate from themes, and we maintain both
color and symbolic icons, so you can configure GIMP to have System theme with
color icons if you prefer the old look.

Moreover, icons are available in four sizes now, so that GIMP would look better
on HiDPI displays. GIMP will do its best to detect which size to use, but you
can manually override that selection in _Edit > Preferences > Interface >
Icon Themes_.

**Contributors:** Benoit Touchette, Ville Pätsi, Aryeom Han, Jehan Pagès,
Alexandre Prokoudine…

## GEGL port, high bit depth support, multi-threading, and more

The ultimate goal for v2.10 was completing the port to GEGL image processing
library, started with v2.6 when we introduced optional use of GEGL for color
tools and an experimental GEGL tool, and continued with v2.8 where we added
GEGL-based projection of layers.

Now GIMP uses GEGL for all tile management and builds an acyclic graph for
every project. This is a prerequisite for adding non-destructive editing planned
for v3.2.

There are many benefits from using GEGL, and some of them you can already enjoy
in GIMP 2.10.

**High bit depth support** allows processing images with up to 32-bit per color
channel precision and open/export PSD, TIFF, PNG, EXR, and RGBE files in their
native fidelity. Additionally, FITS images can be opened with up to 64-bit per
channel precision.

**Multi-threading** allows making use of multiple cores for processing. Not all
features in GIMP make use of that, it's something we intend to work on further.
A point of interest is that multi-threading happens through GEGL processing, but
also in core GIMP itself, for instance to separate painting from display code.

**GPU-side processing** is still optional, but available for systems with stable
OpenCL drivers.

You can find configuration options for multi-threading and hardware acceleration
in _Edit > Preferences > System Resources_.

**Contributors:** Michael Natterer, Øyvind Kolås, Ell, Jehan Pagès…

## Linear color space workflow

Another benefit of using GEGL is being able to work on images in a linear RGB
color space as opposed to gamma-corrected (perceptual) RGB color space.

<figure>
    <img src="https://www.gimp.org/news/2018/03/26/gimp-2-10-0-rc1-released/gimp-2-10-rc1-curves-linear.jpg" alt="Curves in linear mode" width='965' height='642' />
</figure>

Here is what it boils down to:

* You now have both linear and perceptual versions of most blending modes.
* There is now a linear version of the _Color Invert_ command.
* You can freely switch between the two at any time via _Image > Precision_
submenu.
* You can choose which mode id displayed in the _Histogram_ docker.
* You can apply _Levels_ and _Curves_ filters in either perceptual or linear
mode
* When higher than 8-bit per channel precision is used, all channels data is
linear.
* You can choose whether the gradient tool should work in perceptual RGB, linear
RGB, or CIE LAB color space

**Contributors:** Michael Natterer, Øyvind Kolås, Ell…

## Color management revamped

Color management is now a core feature of GIMP rather than a plug-in. This
made it possible, in particular, to introduce color management to all custom
widgets we could think of: image previews, color and pattern previews etc.

<figure>
    <img src="https://www.gimp.org/news/2016-07-13%20GIMP%202.9.4%20Released/gimp-2-9-4-preferences-cms.png" alt="Color Management Preferences" width='975' height='920' />
</figure>

GIMP now uses LittleCMS v2, which allows it to use ICC v4 color profiles.
It also partially relies on the babl library for handling color transforms,
since babl is simply up to 10 times faster than LCMS2 for the cases we tested
both of them on. Eventually babl could replace LittleCMS in GIMP.

**Contributors:** Michael Natterer, Øyvind Kolås…

## Layers and masks

GIMP now ships with two groups of blending modes: legacy (perceptual) and
default (linear).

New blend modes are:

* LCH layer modes: Hue, Chroma, Color, and Lightness
* Pass-Through mode for layer groups
* Linear Burn, Vivid Light, Linear Light, Pin Light, Hard Mix, Exclusion, Merge,
and Split

Layers, paths, and channels can also be tagged with color labels to improve
project organization. This will be even more useful once we add multi-layer
selection later on.

Compositing options for layers are exposed to users now, and all layer-related
settings are finally available in the _Layer Attributes_ dialog.

<figure>
    <img src="https://www.gimp.org/news/2017-08-24%20GIMP%202.9.6%20Released/gimp-2-9-6-layer-attributes-dialog.png" alt="Updated Layer Attributes dialog" width='608' height='579' />
</figure>

Moreover, if you always need alpha in your layers, you can enable automatic
generation of the alpha channel in imported images upon opening them. See
_Edit > Preferences > Image Import & Export_ page for this and more policies.

Layer groups can finally have masks on:

<figure>
    <img src="https://www.gimp.org/news/2018/03/26/gimp-2-10-0-rc1-released/gimp-2-10-rc1-mask-on-layer-group.jpg" alt="Mask on a layer group" width='950' height='685' />
</figure>

## More use for CIE LAB and CIE LCH

With GIMP 2.10, we introduced a number of features that make use of CIE LAB and
CIE LCH color spaces:

* Color dialogs now have an LCH color selector you can use instead of HSV. The LCH
selector also displays out-of-gamut warning.
* A new _Hue-Chroma_ filter in the _Colors_ menu works much like _Hue-Saturation_,
but operates in CIE LCH color space.
* The _Fuzzy Select_ and the _Bucket Fill_ tools can now select colors by their
values in CIE _L_, _C_, and _H_ channels.
* Both the _Color Picker_ and the _Sample Points_ dialog now display pixel
values in CIE LAB and CIE LCH at your preference.

**Contributors:** Michael Natterer, Elle Stone, Ell…

## Tools

### Unified Transform

New _Unified Transform_ tool simplifies making multiple transforms, such as
scaling, rotating, and correcting perspective in one go. The design is based
on a functional spec written by our former UX expert Peter Sikking.

FIXME: screenshot

**Contributors:** Mikael Magnusson…

### Warp Transform

The new _Warp Transform_ tool allows doing localized transforms like growing or
shifting pixels with a soft brush and undo support. Such tools are commonly used
in fashion photography for retouching.

As such, the new tool retires the old _iWarp_ filter that was innovative at the
time of its inception (and pre-dated Photoshop's Liquify filter), but was
ultimately cumbersome to use. The _Warp Transform_ tool also features an
_Eraser_ mode to selectively remove changes, previously unavailable in the
_iWarp_ filter.

FIXME screenshot

**Contributors:** Michael Muré, Michael Natterer, Jonathan Tait…

### Handle Transform

The new _Handle Transform_ tool provides an interesting approach at applying
scaling, rotating, and perspective correction using handles placed on the
canvas. People who are used to editing on touch surfaces might find this tool
strangely easy to grasp.

**Contributors:** Johannes Matschke, Michael Natterer, Ell…

### Blend tool becomes Gradient tool and gets on-canvas editing

We renamed the _Blend_ tool to _Gradient_ tool and changed its default shortcut
to **G**. But this pales in comparison to what the tool can actually do now, and
it's a lot.

The new tool pretty much obsoletes the old _Gradient Editor_ dialog. Now you can
create and delete color stops, select and shift them, assign colors to color
stops, change blending and coloring for segments between color stops and create
new color stops from midpoints _right on the canvas_.

<p>
<video width="830" height="467" controls>
  <source src="https://download.gimp.org/mirror/pub/gimp/video/v2.9/gimp-2-9-8-gradient-edit.webm" type="video/webm">
  <source src="https://download.gimp.org/mirror/pub/gimp/video/v2.9/gimp-2-9-8-gradient-edit.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>
</p>

All gradients available by default are also "editable" now. What it means is
that when you try to change an existing gradient from a system folder, GIMP will
create a copy of it, call it a _Custom Gradient_ and preserve it across
sessions. Unless, of course, you edit another 'system' gradient, in which case
it will become the new custom gradient.

We intend to use the generic implementation of this later for brushes and other
types of resources.

**Contributors:** Michael Henning, Michael Natterer, Ell, Øyvind Kolås…

## Better selection tools

The _Foreground Select_ tool can finally make subpixel selections in complex
cases such as strays of hair on textured background. Two new masking methods are
now available for that.

The _Select by Color_ and _Fuzzy Select_ tools now both feature a _Draw mask_
option to display future selection area with a magenta fill, and the latter tool
also got a _Diagonal neighbors_ option to select diagonally neighboring pixels.

For the _Free Select_ tool, closing a polygonal/free selection now doesn't
confirm the selection automatically. Instead you still can tweak positions of
nodes (where applicable), then press **Enter**, double-click inside the
selection, or switch to another tool to confirm the selection.

The _Intelligent Scissors_ tool finally allows to remove the last added segment
with **Backspace** key, and GIMP now checks, whether the first and the last
segments are distinct before closing the curve.

**Contributors:** Michael Natterer, Jan Rüegg, Daniel Sabo, Ell…

### Color tools

All color tools have been refactored to become GEGL-based filters, so they could
be properly used later on when we introduce non-destructive editing. Hence,
the _Color_ submenu in the _Tools_ menu has been removed, and these filters
are now mostly unavailable in the toolbox.

**Contributors:** Michael Natterer…

## Text tool supports CJK and more writing systems

The _Text_ tool now fully supports advanced input methods for CJK and other
non-western languages. The pre-edit text is now displayed just as expected,
depending on your platform and Input Method Engine. Several input method-related
bugs and crashes have also been fixed.

<figure>
    <img src="https://www.gimp.org/news/2016-07-13%20GIMP%202.9.4%20Released/gimp-2-9-4-ime.png" alt="Input Method Engine support in text tool" width='417' height='240' />
</figure>

**Contributors:** Jehan Pagès…

### Experimental tools

Two new tools were incomplete for inclusion to GIMP 2.10 by default, but still
can be enabled. Please note that they are highly experimental and likely to be
broken for you (up to have GIMP crash). We only mention them, because we need
contributors to get them into the releasable state.

_N-Point Deformation_ tool introduces the kind of smooth, as little rigid as
possible warping you would expect physical objects to have. FIXME

_Seamless Clone_ tool is aimed to simplify making layered compositions.
Typically when you paste one image into another, there are all sorts of
mismatches: color temperature, brightness etc. This new experimental tool tries
to adapt various properties of a pasted image with regards to its backdrop.

To enable these tools, you need to first enable the _Playground_ page of the
_Preferences_ dialog. Do it by running GIMP with a '--show-playground.' switch
(for Windows, you might want tweaking the path to GIMP in the shorcut properties
accordingly). Then you need to go to _Edit -> Preferences -> Playground_ and
enable the respective options, so that the tools would show up in the toolbox.

We need to stress again that you should only do so either if you are very
curious, or (which we hope for) intend to help us fix them.

**Contributors:** Marek Dvoroznak, Barak Itkin, Jehan Pagès, Michael Natterer…

## Digital painting improvements

GIMP 2.10 ships with a number of improvements requested by digital painters. One
of the most interesting new additions here is the _MyPaint Brush_ tool that
first appeared in the GIMP-Painter fork.

The _Smudge_ tool got updates specifically targeted in painting use case. The
new _No erase effect_ option prevents the tools from changing alpha of pixels.
And the foreground color can now be blended into smudged pixels, controlled by
a new _Flow_ slider, where 0 means no blending.

FIXME screenshot from https://www.gimp-forum.net/Thread-Customized-smudge-tool-Smudge-with-painting  ???

All painting tools now have explicit _Hardness_ and _Force_ sliders except for
the _MyPaint Brush_ tool that only has the _Hardness_ slider.

Most importantly, GIMP now supports canvas rotation and flipping to help
illustrators checking proportions and perspective.

FIXME video or screenshot?

New _Symmetry Painting_ dockable dialog, enabled on per-image basis, allows to
use all painting tools with various symmetries (mirror, mandala, tiling…).

FIXME screenshot

A new _Brush lock to view_ option gives you a choice whether you want a brush
locked to a certain zoom level and rotation angle of the canvas. The option is
available for all painting tools that use a brush except for the _MyPaint Brush_
tool.

FIXME screenshot

This new version of GIMP also ships with more new brushes available by default. FIXME

**Contributors:**: Michael Natterer, Alexia Death, Daniel Sabo, shark0r, Jehan
Pagès, Ell, Jose Americo Gobbo, Aryeom Han…

## Digital photography improvements

Some of the new GEGL-based filters are specifically targeted at photographers:
_Exposure_, _Shadows-Highlights_, _High-pass_, _Wavelet Decompose_, _Panorama
Projection_ and others will be an important addition to your toolbox.

<figure>
    <img src="https://www.gimp.org/news/2018/03/26/gimp-2-10-0-rc1-released/gimp-2-10-rc1-shadows-highlights.jpg" alt="Shadows-Highlights" width='950' height='685' />
</figure>

On top of that, the new _Extract Component_ filter simplifies extracting a
channel of an arbitrary color model (LAB, LCH, CMYK etc.) from currently
selected layer. If you were used to decomposing and recomposing images just for
this, your work will be that easier now.

Moreover, you can now use either darktable or RawTherapee as GIMP plug-ins for
opening raw files. Any recent version of either application will do.

A new _Clip Warning_ display filter will visualize underexposed and overexposed
areas of a photo for you, with customizable colors. For now, it’s mostly geared
towards images where colors are stored with floating point precision. You will
mostly benefit from this if you work on 16/32 bit per channel float images such
as EXR and TIFF.

<p>
<video width="830" height="467" controls>
  <source src="https://download.gimp.org/mirror/pub/gimp/video/v2.9/gimp-2-9-8-clipped-colors-warning.webm" type="video/webm">
  <source src="https://download.gimp.org/mirror/pub/gimp/video/v2.9/gimp-2-9-8-clipped-colors-warning.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>
</p>

**Contributors:**: Michael Natterer, Ell, Thomas Manni, Tobias Ellinghaus,
Øyvind Kolås, Jehan Pagès, Alberto Griggio…

## Plug-ins

GIMP now ships with over 60 GEGL-based filters.

FIXME screenshot

A lot of those are former GIMP effects. Here is why GEGL-based implementations
are better:

* You can apply them on images in 32-bit per color channel precision mode.
* You can preview them right on the canvas, and if an image is larger than the
viewport, GIMP will render the viewport first for immediate feedback.
* You can use split preview to compare original image with its processed version
and swap before/after sides both horizontally and vertically.
* In a future non-destructive GIMP, you will be able to adjust settings of those
filters without undoing a ton of steps.

Some of the GEGL-based filters have OpenCL version for hardware acceleration.
This will come in handy, if OpenCL drivers work well for you.
Furthermore many operations can come multi-threaded to use your processor at
their full power.

## Usability improvements

While working with active users, we got rid of quite a few usability issues.
Here are just some of these changes:

* All transformation tools now automatically disable original layer
view so that you could clearly see adjustments against the backdrop.
* Masks can now easily be created with last values you used by just pressing
**Shift** and clicking on respective layer's preview.
* All dialogs except the ones like _Scale_ now remember last values you used
across sessions.
* All GEGL-based filters allow saving named presets and automatically make
timestamped presets for the last time you used them.
* You can now choose fill color or pattern for empty spaces after resizing the
canvas.

There is a lot to improve to make GIMP better suited for professional workflows.
As usual, we welcome constructive discussion and recently create a
[mailing list](https://mail.gnome.org/mailman/listinfo/gimp-gui-list)
to discuss the topic of improving GIMP's usability. This is a long-term
enhancement process, which can take more time than localized changes and
features.

## File formats support

GIMP is now capable of reading and writing TIFF, PNG, PSD, and FITS files with
up to 32-bit per channel precision where applicable.

The PSD plug-in additionally supports pass-through, hard mix, pin light, vivid
light, and linear light blending modes.

GIMP now also ships with native WebP support, including features like animation,
ICC profiles, and metadata. Both importing and exporting are supported.

The JPEG 2000 plug-in was rewritten to use the *OpenJPEG* library rather than
the somewhat obsolete *Jasper* library.

Finally, the PDF plug-in now supports importing password-protected files (you
need to know the password) and exporting multipage PDF documents (each layer
will be a page).

## Metadata viewing, editing, and preservation

GIMP now ships with plug-ins for viewing and editing Exif, XMP, IPTC, GPS, and
DICOM metadata. They are available via the _Image > Metadata_ submenu.

<figure>
<img src="{filename}images/2.8-single-window-mode.png" alt="Single-window mode screenshot" />
</figure>

GIMP will also preserve existing metadata in TIFF, PNG, JPEG, and WebP files.
Each plug-in has respective options when exporting to enable or disable
exporting the metadata.

Additionally, users now can set defaults to preserving or not preserving
metadata in all affected file format plug-ins at once depending on whether they
want complete privacy or, instead, do a lot of microstock photography. The
settings are available on the _Image Import & Export_ page in _Preferences_.

**Contributors:** Benoit Touchette, Michael Natterer, Jehan Pagès…

## On-canvas interaction

GIMP 2.10 ships with a new feature that allows some GEGL-based filters to render
on-canvas controls. For now, this applies to just three filters: _Spiral_,
_Supernova_, and _Panorama Projection_. But there will be more in the future.

<p>
<video width="880" height="528" controls>
  <source src="https://download.gimp.org/mirror/pub/gimp/video/v2.9/gimp-2-9-6-spiral-filter.webm" type="video/webm">
  <source src="https://download.gimp.org/mirror/pub/gimp/video/v2.9/gimp-2-9-6-spiral-filter.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>
</p>

**Contributors:** Michael Natterer, Ell…

### Simplified bug reporting and crash recovery

We need good bug reports to make GIMP better for you, so we introduced a new
feature to watch and intercept critical errors and crashes, then generate a
useful error log that you can copy/paste to a bug report.

<figure>
    <img src="https://www.gimp.org/news/2018/03/26/gimp-2-10-0-rc1-released/gimp-2-10-rc1-bug-reporting.jpg" alt="Debug dialog to simplify bug reporting" width='914' height='662' />
</figure>

On development versions, the dialog will be raised on all kind of errors (even
minor ones). On stable releases, it will be raised only during crashes. The
default behavior can be customized in _Edit > Preferences > Debugging_.

Please note that we still need you to provide context, e.g. what you were doing
when a crash occured. A step-by-step description of how to reproduce this bug
will be most helpful.

Additionally, in case of a crash, GIMP will now attempt to backup all images
with unsaved changes, then suggest to reopen them the next time you start the
application.

<figure>
    <img src="https://www.gimp.org/news/2018/03/26/gimp-2-10-0-rc1-released/gimp-2-10-rc1-crash-recovery.jpg" alt="Crash recovery dialog" width='914' height='507' />
</figure>

We cannot guarantee 100% success, but it will succeed sometimes, and this might
rescue your unsaved work!

**Contributors**: Jehan Pagès…

## Known regressions

FIXME

## API changes

Over the course of this development cycle, we deprecated a lot of API, providing
a compatibility layer for 3rd party developers who write scripts and plug-ins.

For the full list of changes in PDB, please [see the
wiki](https://wiki.gimp.org/wiki/Release:2.10_changelog#API_Changes).
This ChangeLog page also has a verbose list of all other changes in
2.10.

### Roadmap and what's next

We maintain a [roadmap for GIMP development](http://wiki.gimp.org/index.php/Roadmap)
that outlines the order of features to be implemented based on priorities.

The next big update will be v3.0 that will feature GTK+3 port and a lot of
internal changes. For users, this will mostly mean: updated user interface,
better support for graphic tablets, better support for HiDPI displays, better
support for Wayland on Linux.

We are also opening the 2.10.x series for new features. This means you don't
have to wait for exciting improvements for years anymore: any new feature can
indeed be backported to a 2.10.x release as long as its code is not too invasive
and making maintenance difficult.

All the new features from 2.10.x will be part of 3.0 as well.

## Getting involved with contributing to GIMP

FIXME

## Download and install pre-made packages

GIMP can be downloaded directly from our [Downloads](/downloads/) section.
As usual, we will have Windows installers and macOS packages readily
available. We now also provide a Flatpak repository for Linux.

Please be very cautious when downloading from anywhere else — some sites use
GIMP's popularity to lure unwary users into their traps by shipping modified
installer packages.

## Bugs

If you think you found a bug in GIMP, please make sure that it hasn't been
already reported. Search [Bugzilla](http://bugzilla.gnome.org/) before filing a
new bug-report. Here are some interesting Bugzilla queries:

* [Open bugs with milestone 2.10](https://bugzilla.gnome.org/buglist.cgi?product=GIMP&target_milestone=2.10&bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED)
* [Resolved bugs with milestone 2.10](https://bugzilla.gnome.org/buglist.cgi?product=GIMP&target_milestone=2.10&bug_status=RESOLVED&bug_status=VERIFIED&bug_status=CLOSED)

## Contributing

We need your help to make GIMP 2.10 a success. If you want to join us hacking,
show up on [IRC](https://www.gimp.org/irc.html) in #gimp (on *irc.gimp.org*
server) or introduce yourself on the [gimp-developer
mailing-list](https://mail.gnome.org/mailman/listinfo/gimp-developer-list).
We are also looking for people to look after the web-site and update the
[tutorials](https://www.gimp.org/tutorials/).
Or you might want to join the [documentation team](http://docs.gimp.org/).
