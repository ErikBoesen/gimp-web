Title: GIMP 2.10 Release Candidate 1 Released
Date: 2018-03-25
Category: News
Authors: Wilber
Slug: gimp-2-10-rc1-released
Summary: GIMP 2.10 RC1: bugfixes, stability and polish
Status: draft

Newly released GIMP 2.10 RC1 is the first release candidate before GIMP
2.10 stable release. With more than 740 commits since the 2.9.8
development version mid-December, the focus has really been on getting the
last details right.

All the new features we added for this release are instrumental in either
improving how GIMP handles system resources, or helping you to report bugs
and recover lost data. For a complete list of changes please see
[NEWS](https://git.gnome.org/browse/gimp/tree/NEWS).

## New features
### Dashboard dockable

A new _Dashboard_ dock helps monitoring GIMP's resource usage to keep
things in check, allowing you to make more educated decisions about various
configuration options.

<figure>
    <img src="{filename}gimp-2-10-rc1-dashboard.jpg" alt="Dashboard dock" width='950' height='685' />
</figure>

On developer side, it also helps us in debugging and profiling various
operations or parts of the interface, which is important in our constant
quest to improve GIMP and GEGL, and detect which parts are the biggest
bottlenecks.

The feature was contributed by _Ell_ — one of GIMP's most productive
developers of late.

### Debug dialog

What we consistently hear from users is that they have had zero GIMP
crashes in years of using it. Still, as any software, it is not exempt
from bugs, and unfortunately sometimes might even crash.

And while we encourage you to report all bugs you encounter, we do admit
that producing useful information for a report can be difficult, and there
is little we can do about a complaint that says _"GIMP crashed. I don't
know what I was doing and I have no logs"_.

So GIMP now ships with a built-in [debugging system](https://girinstud.io/news/2018/02/automatic-bug-report-stack-traces-gimp/) that gathers
technical details on errors and crashes.

<figure>
    <img src="{filename}gimp-2-10-rc1-bug-reporting.jpg" alt="Debug dialog to simplify bug reporting" width='914' height='662' />
</figure>

On development versions, the dialog will be raised on all kind of errors
(even minor ones). On stable releases, it will be raised only during crashes.
The default behavior can be customized in _Edit > Preferences >
Debugging_.

*Note: you are still expected to write down contextual information when
you report bugs, i.e.: What were you doing when the bug happened? And if
possible, step by step reproduction procedures are a must.*

The feature was contributed by _Jehan Pages_ from [ZeMarmot](https://film.zemarmot.net/) project.

### Image recovery after crash

Now that the debugging system was in place to detect a crash, it was easy
enough to add crash recovery. In case of a crash, GIMP will now attempt
to backup all images with unsaved changes, then suggest to reopen them
the next time you start the application.

<figure>
    <img src="{filename}gimp-2-10-rc1-crash-recovery.jpg" alt="Crash recovery dialog" width='914' height='507' />
</figure>

This is not a 100%-guaranteed procedure, since a program state during
a crash is unstable by nature, so backing up images might not always
succeed. What matters is that it will succeed sometimes, and this might
rescue your unsaved work!

This feature was also contributed by _ZeMarmot_ project.

### Shadows-Highlights

This new filter is now available in GIMP in the _Colors_ menu thanks
to the contribution by _Thomas Manni_ who created a likewise named GEGL
operation.

<figure>
    <img src="{filename}gimp-2-10-rc1-shadows-highlights.jpg" alt="Shadows-Highlights" width='950' height='685' />
</figure>

The filter allows adjusting shadows and highlights in an image separately,
with some options available. The implementation closely follows its
counterpart in [darktable](https://www.darktable.org) digital photography software.

## Completed features
### Layer masks on layer groups

Masks on layer groups are finally possible! This work, started years ago,
has finally been finalized by _Ell_. Group-layer masks work similarly
to ordinary-layer masks, with the following considerations.

<figure>
    <img src="{filename}gimp-2-10-rc1-mask-on-layer-group.jpg" alt="Mask on a layer group" width='950' height='685' />
</figure>

The group's mask size is the same as group's size (i.e., the
bounding box of its children) at all times. When the group's size
changes, the mask is cropped to the new size — areas of the mask
that fall outside of the new bounds are discarded, and newly added
areas are filled with black (and hence are transparent by default).

### JPEG 2000 support ported to OpenJPEG

JPEG 2000 images importing was already supported, using the library called
*Jasper*. Yet this library is now deprecated and slowly disappearing from
most distributions. This is why we moved to [OpenJPEG](http://www.openjpeg.org/).

The port was initially started by _Mukund Sivaraman_. This has later
been completed by _Darshan Kadu_, under the FSF internship program, and
mentored by _Jehan_ who made the last polishing.

In particular, now GIMP can properly import JPEG 2000 images in any bit
depth (over 32-bit per channel will be clamped to 32-bit and
non-multiple of 8-bit will be promoted, for instance 12-bit will end up
as 16-bit per channel in GIMP). Images in `YCbCr` and `xvYCC` color spaces
will be converted to `sRGB`.

<figure>
    <img src="{filename}gimp-2-10-rc1-j2k-importing.jpg" alt="Imported JPEG 2000 file" width='949' height='599' />
</figure>

JPEG 2000 codestream files are also supported. Whereas color space can be
detected for JPEG 2000 images, for codestream files you will be asked
to specify the color space.

### Linear workflow updates

_Curves_ and _Levels_ filters have been updated to have a switch between
linear and perceptual (non-linear) modes, depending on which one you need.

<figure>
    <img src="{filename}gimp-2-10-rc1-curves-linear.jpg" alt="Curves in linear mode" width='965' height='642' />
</figure>

You can apply _Levels_ in perceptual mode to a linear image, or _Curves_ in
linear mode to a perceptual image — whichever suits you best for the task
at hand.

The same switch in the _Histogram_ dock has been updated accordingly.

### Screenshot and color-picking

**On Linux**, taking screenshots with the Freedesktop API has been implemented.
This should become the preferred API in a hopefully close future, especially
because it is meant to work inside sandboxed applications. Though for the time
being, it is still not given priority because it lacks some basic features and
is not color-managed in any implementation we know of, which makes it a
regression compared to other implementations.

**On Windows**, _Simon Mueller_ has improved the screenshot plug-in as
well to handle hardware-accelerated software and multi-monitor displays.

**On macOS** finally, color picking with the Color dock is now
color-managed.

### Metadata preferences

Settings were added for metadata export handling in "Image Import &
Export" page of the _Preferences_ dialog. By default, the settings are
checked, which means that GIMP will export all metadata, but you can uncheck
them (in particular since metadata can often contain a lot of sensitive
private information).

<figure>
    <img src="{filename}gimp-2-10-rc1-metadata-preservation.png" alt="Metadata preservation" width='914' height='380' />
</figure>

Note that these options can also be changed per format ("Load Defaults"
and "Save Defaults" button), and of course per file during exporting,
just like any other option.

### Lock brush to view

GIMP finally gives you a choice whether you want a brush locked to
a certain zoom level and rotation angle of the canvas.

<figure>
    <img src="{filename}gimp-2-10-rc1-lock-brush-to-view.jpg" alt="Lock brush to view demo" width='950' height='568' />
</figure>

The option is available for all painting tools that use a brush except
for the MyPaint Brush tool.

### Missing icons

8 new icons were added by _Alexandre Prokoudine_, _Aryeom Han_
(*ZeMarmot* film director), and _Ell_.

### Various GUI refining

Many last-minute details have been handled, such as renaming the
composite modes to be more descriptive, shortened color channel labels
with their conventional 1- or 2-letter abbreviations, color models
rearranged in the Color dock, and much more!

## Translations

String freeze has started and GIMP received updates from:
Basque, Brazilian Portuguese, Catalan, Chinese (Taiwan), Danish,
Esperanto, French, German, Greek, Hungarian, Icelandic, Italian,
Japanese, Latvian, Polish, Russian, Serbian, Slovenian, Spanish,
Swedish, Turkish.

The Windows installer is now also localized with gettext.

## Helping GIMP

We'd like to remind you that GIMP is free software. Therefore the first way
to help is to contribute your time. You can report bugs and send patches,
whether they are code patches, icons, brushes, documentation, translations, etc.

In this release for instance, about 15% of changes were done by
non-regular contributors.

You can also contribute tutorials or news for our website, as _Patrick
David_ explained it so well in his talk [*Why the GIMP Team Obviously
Hates You*](https://www.youtube.com/watch?v=AemoQzCFHpc). _Patrick
David_ is himself one of GIMP important contributors on the community
side (and he is also the one who created our current website [back in
2015](https://www.gimp.org/news/2015/11/22/20-years-of-gimp-release-of-gimp-2816/#new-website)).

Last but not least, we remind that you can contribute financially in a
few ways. You can [donate to the project itself](https://www.gimp.org/donating/),
or you can support the core team developers who raise funds
individually, in particular [_Øyvind Kolås_](https://www.patreon.com/pippin)
for his work on GEGL, GIMP graphics engine, and [_ZeMarmot_ project](https://film.zemarmot.net/en/donate)
(_Aryeom & Jehan_) for their work on GIMP itself (about 35% of this
release is contributed by their project).

## What's Next

This is the last stretch before making the final GIMP 2.10 release. There are
a few more changes planned before we wrap it up. For instance, [_Americo Gobbo_](http://americogobbo.com.br/)
is working (with minor help from _ZeMarmot_) on improving our default brush
set. His work will be available either in another release candidate (if we
make another one) or in the final release.

We are currently 12 blocker bugs away from making the final release. We'll do our best to make it quick!
