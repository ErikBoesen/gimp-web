Title: GIMP 2.10.0 Release Candidate 2 Released
Date: 2018-04-14
Category: News
Authors: Wilber
Slug: gimp-2-10-0-rc2-released
Summary: GIMP 2.10.0-rc2: the end is near
Status: draft

Here is the second release candidate! In the last 3 weeks, since GIMP
2.10.0-RC1, 38 bugs have been fixed, with more than 140 commits pushed,
quite a high rate of fixes as often just before a major release.

For a complete list of changes please see [NEWS](https://git.gnome.org/browse/gimp/tree/NEWS).

## Optimizations and multi-threading for painting and display

A major regression of GIMP 2.10, compared to 2.8, was slower painting.
Several optimizations have been merged in GIMP core, but also in babl
and GEGL regarding this issue, by several contributors (Ell, Jehan,
Massimo Valentini, Øyvind Kolås…), along with a lot of speed tests
performed by Elle Stone and Jose Americo Gobbo.

The whole issue pushed Ell to implement multi-threading within GIMP, so
that painting and display are now run on separate thread, hence greatly
speeding up feedback of the graphical interface.

## Themes Rewritten

Since the development version 2.9.4, we had [new themes shipped with
GIMP](https://www.gimp.org/news/2016/07/13/gimp-2-9-4-released/), and in
particular dark themes, as is now common for graphics applications.
Unfortunately there was no maintainers anymore and bugs were piling up in
the themes, providing a poor experience.

Ville Pätsi, long time contributor, has taken up the task of creating
brand new themes without any of the usability issues and glitches of
previous ones. While cleaning up, only the *Gray* theme has been kept,
whereas *Light* and *Dark* were rewritten from scratch. *Darker* and
*Lighter* themes have been removed (they won't likely reappear unless
someone decides to rewrite and contribute them as well, and unless this
person stays around for maintainance).

### New on-canvas control for 3D rotation

A new widget for on-canvas interaction of 3D rotation (yaw, pitch, roll)
has been implemented by Ell. This new widget is currently only used for
the Panorama Projection filter.

## Translations


## GEGL changes


## What's Next

We are now **8 blocker bugs** away from the final release.
On your marks, get set…
