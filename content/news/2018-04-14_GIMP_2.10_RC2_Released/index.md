Title: GIMP 2.10.0 Release Candidate 2 Released
Date: 2018-04-14
Category: News
Authors: Wilber
Slug: gimp-2-10-0-rc2-released
Summary: GIMP 2.10.0-rc2: the end is near
Status: draft

Here is the second release candidate! In the last 3 weeks since releasing
GIMP 2.10.0-RC1, we fixed 38 bugs and introduced important performance
improvements.

For a complete list of changes please see [NEWS](https://git.gnome.org/browse/gimp/tree/NEWS).

## Optimizations and multi-threading for painting and display

A major regression of GIMP 2.10, compared to 2.8, was slower painting.
To address this issue, several contributors (Ell, Jehan, Massimo Valentini,
Øyvind Kolås…) introduced improvements to the GIMP core, as well as to the
GEGL and babl libraries. Additionally, Elle Stone and Jose Americo Gobbo
contributed performance testing.

The whole issue pushed Ell to implement multi-threading within GIMP, so
that painting and display are now run on separate threads, thus greatly
speeding up feedback of the graphical interface.

The new parallelization framework is not painting-specific and could be
used for improving other parts of GIMP.

## Themes rewritten

Since the development version 2.9.4, we had [new themes shipped with
GIMP](https://www.gimp.org/news/2016/07/13/gimp-2-9-4-released/), and in
particular dark themes, as is now common for creative applications.
Unfortunately they were unmaintained, bugs kept piling up, and the user
experience wasn't exactly stellar.

Our long-time contributor Ville Pätsi took up the task of creating
brand new themes without any of the usability issues and glitches of
previous ones. While cleaning up, only the *Gray* theme has been kept,
whereas *Light* and *Dark* were rewritten from scratch. *Darker* and
*Lighter* themes have been removed (they won't likely reappear unless
someone decides to rewrite and contribute them as well, and unless this
person stays around for maintenance).

### New on-canvas control for 3D rotation

A new widget for on-canvas interaction of 3D rotation (yaw, pitch, roll)
has been implemented by Ell. This new widget is currently only used for
the Panorama Projection filter.

## Translations

8 translations have been updated betweeen the two release candidates.
We are very close to releasing the final version of GIMP 2.10.0. If you
plan to update translation into your language and be in time for the release,
we recommend starting now.

## GEGL changes


## What's Next

We are now **8 blocker bugs** away from the final release.
On your marks, get set…
