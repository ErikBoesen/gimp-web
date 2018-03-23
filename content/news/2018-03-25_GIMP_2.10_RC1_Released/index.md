Title: GIMP 2.10 Release Candidate 1 Released
Date: 2018-03-25
Category: News
Authors: Wilber
Slug: gimp-2-10-rc1-released
Summary: GIMP 2.10 RC1: bugfixes, stability and polish
Status: draft

Newly released GIMP 2.10 RC1 is the first release candidate before GIMP
2.10 stable release. With more than 730 commits since the 2.9.8
development version mid-December, for an average of 7 commits a day, the
focus has really been on getting the last details right.

We actually got a few fancy new features, and in particular a new
Dashboard dock to display GEGL cache, swap size and CPU usage, as well
as a new debugging dialog which appears upon crashes or various critical
errors, encouraging you to report bugs, hence helping us to improve GIMP
even faster! And finally GIMP is now trying to recover your images in
the unfortunate event when a crash were to happen.
As you can see, even new features are mostly targetted at efficiency and
debugging.

For a complete list of changes please see [NEWS](https://git.gnome.org/browse/gimp/tree/NEWS).

## Dashboard dockable

A new dock is available in GIMP under the title "**Dashboard**". It was
contributed by _Ell_, as always one of GIMP most productive developers.

The dashboard helps monitoring GIMP's resource usage to keep things in
check, allowing you to make more educated decisions about various
configuration options.

On developer side, it also helps us in debugging and profiling more
easily various operations or parts of the interface, which is important
in our constant quest to improve GIMP and GEGL, and detect which parts
are the biggest bottlenecks.

## Debug dialog

GIMP is quite stable and maintained. Still as any software, it is
not exempt from bugs, and sometimes might unfortunately even crash.

We are encouraging you to report every bugs you encounter. Yet often, it
is not easy to produce the right information. If we get a bug saying
"*GIMP crashed. I don't know what I was doing and have no logs.*", you
can understand there is not much we can do.

This is after handling one more of such bug reports that _Jehan_ from
[ZeMarmot](https://film.zemarmot.net/) project realized GIMP needed a
[debugging system](https://girinstud.io/news/2018/02/automatic-bug-report-stack-traces-gimp/)
gathering technical details on errors and crashes. By default, on
development versions, the dialog will be raised on all kind of errors
(even some minor ones) whereas it will be raised only during crashes on
stable releases. This can be customized in `Edit > Preferences >
Debugging`.

*Note: you are still expected to write down contextual information when
you report bugs, i.e.: What were you doing when the bug happened? And if
possible, step by step reproduction procedures are a must.*

## Image Recovery after crash

As a natural step after the debugging system, *ZeMarmot* project also
implemented image recovery after crashes. In the unfortunate event where
GIMP would end unexpectedly, it would now try and backup any image with
unsaved changes right at crash time; then at next startup, it would
propose you to reopen these backups.

This is not 100%-guaranteed procedure, since a program state during a
crash is unstable by definition, so backing up images might not always
succeed. What matters is that it will succeed sometimes, and this might
save your unsaved work!

## Finishing features
### Layer masks on layer groups

Masks on layer groups are finally possible! This work started years ago
has finally been finalized by _Ell_.

Group-layer masks work similarly to ordinary-layer masks, with the
following considerations:
The group's mask size is the same as group's size (i.e., the
bounding box of its children) at all times. When the group's size
changes, the mask is cropped to the new size — areas of the mask
that fall outside of the new bounds are discarded and their data is
lost (sans undo), and newly added areas are filled with black (and
hence are transparent by default).

### JPEG 2000 support ported to OpenJPEG

JPEG 2000 image import were already supported, using the library *Jasper*.
Yet this library is deprecated and slowly disappearing from most
distributions. This is why we moved to [OpenJPEG](http://www.openjpeg.org/).

The port was initially started by _Mukund Sivaraman_. This has later
been completed by _Darshan Kadu_, under the FSF internship program, and
mentored by _Jehan_, who made the last polishing.

In particular, now GIMP can properly import JPEG 2000 images in any bit
depth (over 32-bit per channel will be clamped to 32-bit and
non-multiple of 8-bit will be promoted, for instance 12-bit will end up
as 16-bit per channel in GIMP). Images in `YCbCr` and `xvYCC` color spaces
will be converted to `sRGB`.

JPEG 2000 codestream are also supported. Whereas color space can be
detected for JPEG 2000 images, you will be interactively queried to
specify the color space for codestream files.

### Screenshot and color-picking

**On Linux**, Screenshot with the Freedesktop API has been implemented.
This should become the prefered API in a hopefully close future,
especially because it is meant to work also inside sandboxed
applications. Though for the time being, it is still not given priority
because it lacks some basic features and is not color-managed in any
implementation we know of, which makes it a regression compared to other
implementations.

**On Windows**, _Simon Mueller_ has improved the screenshot plug-in as
well to handle hardware-rendered software and multi-monitor displays.

**On macOS** finally, color picking with the Color dock is now
color-managed.

### Missing icons

8 new icons were added by _Alexandre Prokoudine_, _Aryeom Han_
(*ZeMarmot* film director) and _Ell_.

### Metadata preferences

Settings were added for metadata export handling in "Image Import &
Export" page of Preferences. By default, the settings are checked, which
means that GIMP will export all metadata, but you can uncheck them (in
particular since metadata can often contain a lot of sensitive
information).

Note also that these options can also be changed per format ("Load
Defaults" and "Save Defaults" button), and of course per file during
export, as any other option.

### Various GUI refining

Many last-minute details have been handled, such as renaming the
composite modes to be more descriptive, shortened color channel labels
with their conventional 1 or 2-letter abbreviations, color models
rearranged in the Color dock, and much more!

## Translations

String freeze has started and GIMP received updates from:
Basque, Brazilian Portuguese, Catalan, Chinese (Taiwan), Danish,
Esperanto, French, German, Greek, Hungarian, Icelandic, Italian,
Japanese, Latvian, Polish, Russian, Serbian, Slovenian, Spanish,
Swedish, Turkish.

Also the Windows installer now localized with gettext.

## Helping GIMP

We remind that GIMP is Free Software. Therefore the first way to help is
to contribute your time. You can report useful bugs, and send us
patches, whereas they are code patches, but also icons, data,
documentation, translations, etc.

In this release for instance, about 15% of changes were done by
non-regular contributors.

You may also contribute tutorials or news for our website, as _Patrick
David_ explained it so well in his talk [*Why the GIMP Team Obviously
Hates You*](https://www.youtube.com/watch?v=AemoQzCFHpc). _Patrick
David_ is himself one of GIMP important contributors on the community
side (and he is also the one who made us our current website, [back in
2015](https://www.gimp.org/news/2015/11/22/20-years-of-gimp-release-of-gimp-2816/#new-website)).

Last but not least, we remind that you can contribute financially in a
few ways. You can donate to the project itself, or you can support the
core team developers who raise funds individually, in particular
[_Øyvind Kolås_](https://www.patreon.com/pippin) for his work on GEGL,
GIMP graphics engine, and [_ZeMarmot_ project](https://film.zemarmot.net/en/donate)
(_Aryeom & Jehan_) for their work on GIMP itself (about 34% of this
release is contributed by *ZeMarmot*).
[_Alexandre Prokoudine_](https://www.patreon.com/prokoudine), one of
GIMP major non-developer contributors, also recently started raising
funds for his writing work on creative Free Software.

## What's Next

We are now in the last straight line before GIMP 2.10 finale release.
It can be noted that this release is actually a hybrid between a
development version and a release candidate, thus we have been wondering
how we should call it. We are still planning some changes before finale
release, which should usually forbid it to be called "Release
Candidate". For instance, [_Americo Gobbo_](http://americogobbo.com.br/)
is working (with minor help from _ZeMarmot_) on improving our default
brush set, but this is not available yet in this RC.

On the other hand, we are trying to accelerate the process because we
have just been pushing the stable release for too long now. Therefore
we are not sure if we will have any other release candidate.

With only 12 blocker bugs remaining to day of writing, you can count the
weeks before GIMP 2.10!
