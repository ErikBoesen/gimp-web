Title: GIMP 2.10.0 Released
Date: 2018-04-26
Category: News
Authors: Wilber
Slug: gimp-2-10-0-released
Summary: GIMP 2.10.0 is now out with a boom!
Status: draft

The long-awaited GIMP 2.10.0 is finally here! This is a huge release,
which contains the result of 6 long years of work ([GIMP
2.8 was released nearly exactly 6 years ago!](https://www.gimp.org/news/2012/05/03/gimp-28-released/)).

# The Changes in short #

We are not going to list the full changelog here, since you can get a
better idea with our [official GIMP 2.10 release
notes](https://ww.gimp.org/release-notes/gimp-2.10.html). To get an even more
detailed list of changes please see the [NEWS](https://git.gnome.org/browse/gimp/tree/NEWS) file.

Some of the most notable changes include:

* The image processing nearly fully ported to [GEGL](https://gegl.org),
  allowing high bit depth processing, multi-threaded and hardware
  accelerated pixel processing, and more.
* Color management is a core feature now, most widgets and preview areas
  are color-managed.
* Many tools improved and several new and exciting tools, such as the
  Warp transform, the Unified transform and the Handle transform tools.
* On-canvas preview for all filters ported to GEGL.
* Improved digital painting with canvas rotation and flipping, symmetry
  painting and [MyPaint](http://mypaint.org/) brush support.
* Several new image format support added (OpenEXR, RGBE, WebP, HGT), as
  well as improved support for many existing formats (in particular PSD
  importing is more robust now).
* Metadata viewing and editing for Exif, XMP, IPTC, and DICOM
* Basic HiDPI support: automatically or user-selected icon size.
* New themes for GIMP (Light, Gray, Dark, and System) and new symbolic
  icons meant to somewhat dim the environment and shift the focus
  towards content (former theme and color icons are still available in
  Preferences).

# Some statistics #

TODO: whip up some text around these stats!

Start date: 2012-05-02 18:17:00 +0400 - End date: 2018-04-26 15:45:44 +0200
Between GIMP_2_8_0 and HEAD, 237 people contributed 9545 commits to GIMP.
This is an average of 4 commits a day.

Statistics on all files: 7516 files changed, 2931926 insertions(+), 1163975 deletions(-)
