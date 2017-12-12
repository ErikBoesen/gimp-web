Title: GIMP 2.9.8 Released
Date: 2017-12-13
Category: News
Authors: Alexandre Prokoudine
Slug: gimp-2-9-8-released
Summary: GIMP 2.9.8 introduces on-canvas gradient editing and various
enhancements while focusing on bugfixing and stability.
Status: draft

Newly released GIMP 2.9.8 introduces on-canvas gradient editing and various
enhancements while focusing on bugfixing and stability. For a complete list of
changes please see [NEWS](https://git.gnome.org/browse/gimp/tree/NEWS).

## On-Canvas Gradient Editing

One of the most user-visible changes in 2.9.8 is the updated Blend tool.
Here's what's new about it.

First of all, it pretty much eliminates the need for the old Gradient Editor
dialog, as all of the dialog's features are now available directly on the
canvas. You can create and delete color stops, select and shift them, assign
colors to color stops, change blending and coloring for segments between color
stops, create new color stops from midpoints.

-- [missing video from Ell] --

Secondly, default gradients are now "editable". As you probably know, the
reason most resources such as brushes, painting dynamics, and gradients are not
direclty editable is that they are typically installed into a system directory
where non-privileged user can't make any changes.

Now when you try to change an existing gradient from a system folder, GIMP will
create a copy of it, call it a 'Custom Gradient' and preserve it across
sessions. Unless, of course, you edit another 'system' gradient, in which case
it will become the new custom gradient.

Since this feature is useful for more than just gradients, it was made generic
enough to be used for brushes and other types of resources in the future.
We expect to revisit this in the future releases of GIMP.

<figure>
    <img src="{filename}gimp-2-9-8-on-canvas-gradient.png" alt="Editing a gradient fill on the canvas" width='FIXME' height='FIXME' />
</figure>


Now that 2.9.8 is out with the updated Blend tool, we are interested in your
feedback, as we still expect some cleanup and enhancements to be done there.

Most of the programming was done by _Ell_, however we also want to acknowledge
two other people who contributed to that effort one way or another.

_Michael Henning_ improved the Blend tool for 2.9.2, making the position of its
endpoints editable before applying the gradient fill.

_Michael Natterer_ refactored source code of GIMP's tools to make them reuse one
another's on-canvas handles. That greatly simplified adding on-canvas handles
for color stops. He also added the generic on-canvas dialog with the most
important options for tools.

## Clip Warning

_Ell_ also implemented a feature request made in our public mailing list,
where Elle Stone asked for some way to visualize underexposed and overexposed
areas of a photo — a common feature in digital photography tools such as
darktable and RawTherapee.

The new _Clip Warning_ display filter targets that use case and fills
underexposed and overexposed areas with user-configurable colors. For now,
it's mostly geared towards images where colors are stored with floating point
precision. You will mostly benefit from this, if you work on 16/32 bit per
channel float images such as EXR and TIFF.

-- [video from alexandre] --

Implementing this feature as a display filter has certain disadvantages such
as having to go through the whole routine of adding a display filter for every
image. We are thinking of better ways to do this.

## Color Management

GIMP now uses the babl library for doing conversion of images between color
spaces when matrix-based ICC profiles are used. This leads to completing
transforms ca. 5 times faster in comparison to LittleCMS v2 on a few test
images we tried this on. We expect to make further use of babl for doing color
transforms once the library supports ICC profiles based on lookup tables.

## Wayland support

While we already had the screenshot plug-in working under GNOME/Wayland,
we now implemented screenshots for KDE/Wayland (though it misses [rectangular
area selection](https://bugs.kde.org/show_bug.cgi?id=387721)).

The Color Picker widget will now also work in KDE/Wayland.
Note that there is still [no color-picking interface in GNOME for
Wayland](https://bugzilla.gnome.org/show_bug.cgi?id=789756), so as a workaround,
color picking will only work inside GIMP windows for this platform.

Color-picked and screenshot pixels are not color-managed yet in Wayland.

## Paste in Place

Michael Natterer implemented another small feature request from a user who
asked for an Inkscape-like _Paste in Place_ command. The idea is that GIMP
should be able to paste contents of the clipboard at exact coordinates the
contents was originally copied from. This feature is available for both the
regular clipboard and named buffers.

-- [missing screenshot from alexandre] --

_Paste in Place_ complements the usual 'Paste' command which places contents
of the clipboard into the center of the viewport.

## GUI and Usability

The spinscale widget now highlights vertical parts of the slider section
differently to hint that position of cursor above the widget matters.
When changing values in the lower step section, the pointer will be wrapped
around the screen so that you could continue adjusting the value without
interruptions.

When using transform tools, you can now press a modifier key before or after
pressing/releasing a mouse button.

The _Info_ window for the color picker now remembers the modes across session.
So if you prefer seeing LAB values, that's what you will see every time until
you choose something else.

Canvas rotation and flip information is now visible in the status bar, as angle
value and flip icon. Clicking on these canvas status will respectively raise the
_Select Rotation Angle_ dialog or unflip the canvas.

## Help manuals

Upon detection of locally installed manuals in several languages, GIMP will now
allow selection of the manual language to display in the preferences (tab
`Interface > Help System`).

<figure>
<img src="{filename}help-localization.png" alt='manual localization in preferences' width='831' height='420'>
<figcaption>
Manual localization settings in GIMP preferences
</figcaption>
</figure>

This is especially useful since GIMP interface has localization in 80 languages
yet its [manual](https://www.gimp.org/docs/) is translated in *only* 17
languages. You may therefore not have a choice of viewing a manual in
your preferred language.

Moreover one may use an interface in a language while still preferring read the
manual in another for any personal reasons, and may not want or have the
possibility to read it online. Hence this choice made available in
preferences.

## Improved Wavelet Decompose Filter

The much demanded _Wavelet Decompose_ filter got a small round of updates
and gained a couple of new options: placing decomposition stack into its own
layer group and adding a layer mask to each scales layers. It also produces
more expected results now.

## File formats

* Various fixes were done to PSD format support.
* Password-protected PDF files can now be imported in GIMP.
* HGT files can now be imported. HGT is the format for [Digital Elevation Model
  data by the NASA and other space agencies](https://dds.cr.usgs.gov/srtm/version2_1/Documentation/SRTM_Topo.pdf).
  GIMP now supports both the SRTM-1 and SRTM-3 types (as far as we know, the
  only 2 variants) which will be imported as grayscale RGB images.
  In order to obtain more visible relief information, you will want to map
  altitudes to colors, for instance with "Gradient Map" filter as we did in the
  example image below (see also this [explicative post on the
  process](https://girinstud.io/news/2017/12/new-format-in-gimp-hgt/)).

<figure>
<img src="{filename}GIMP-import-hgt.png" alt='Importing HGT files in GIMP' width='950' height='616'>
<figcaption>
NASA HGT file import followed by appropriate "Gradient Map" filtering
</figcaption>
</figure>

## Translations

Translation of GIMP was updated for 13 languages: Catalan, Croatian, Galician,
German, Greek, Hungarian, Icelandic, Indonesian, Italian, Polish, Russian,
Spanish, and Swedish.

## What's Next

We had been hoping, earlier this year, to release GIMP 2.10 by the end of 2017.
As you can see, the chances of it happening are rather slim now and this only
proves that we should never give any temporal hints for release dates!

Nevertheless we are getting very close to GIMP 2.10 and are thinking of entering
feature and string freeze periods, which may actually happen soon after the
release of GIMP 2.9.8 development version. Exciting times!
