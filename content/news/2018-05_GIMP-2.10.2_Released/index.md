Title: GIMP 2.10.2 Released
Date: 2018-05-20
Category: News
Authors: Wilber
Slug: gimp-2-10-2-released
Summary: GIMP 2.10.2 released (bug fixes, HEIF support and new filters)
Status: draft

It's barely been a month since we released GIMP 2.10.0, and the
first bugfix version 2.10.2 is already there!
Its main purpose is fixing the various bugs and issues
which were to be expected after the 2.10.0 release.

**Therefore, 44 bugs have been fixed in less than a month!**

We have also been relaxing the policy for new
features and this is the first time we will be applying this policy
with features in a stable micro release! How cool is that?

*For a complete list of changes please see [NEWS](https://git.gnome.org/browse/gimp/tree/NEWS).*


# New features

## Added support for HEIF image format

This release brings [HEIF][] image support, both for loading and export!

Thanks to Dirk Farin for the HEIF plug-in.

[HEIF]: https://en.wikipedia.org/wiki/High_Efficiency_Image_File_Format "High Efficiency Image File Format"


## New filters

Two new filters have been added, based off GEGL operations:

**Spherize** filter to wrap an image around a spherical cap, based on the
  `gegl:spherize` operation.

<figure>
<img src="{attach}gimp-2-10-2-spherize.png" alt="Spherize filter">
<figcaption>
Spherize filter in GIMP 2.10.2.
<br/>
<a href="http://film.zemarmot.net/">Original image CC-BY-SA by Aryeom Han</a>.
</figcaption>
</figure>

**Recursive Transform** filter to create a Droste effect, based on the
  `gegl:recursive-transform` operation.

<figure>
<img src="{attach}gimp-2-10-2-recursive-transform.png" alt="Recursive Transform filter">
<figcaption>
Recursive transform filter in GIMP 2.10.2, with a custom on-canvas interface.
<br/>
<a href="https://www.flickr.com/photos/philipphaegi/39057406754">Original image
CC-BY by Philipp Haegi</a>.
</figcaption>
</figure>


# Noteworthy improvements
## Better single-window screenshots on Windows

While the screenshot plug-in was already better in GIMP 2.10.0, we
had a few issues with single-window screenshots on Windows 
when the target window was hidden behind other windows, 
partly off-screen, or when display scaling was activated.

All these issues have been fixed by our new contributor Gil Eliyahu.


## Histogram computation improved

GIMP now calculates histograms in separate threads which eliminates some
UI freezes. This has been implemented with some new internal APIs which
may be reused later for other cases.


# Working with third-parties
## Packagers: set your bug tracker address

As you know, we now have a debug dialog which may pop-up when crashes
occur with debug information. This dialog opens our bug tracker in a
browser.

We realized that we get a lot of bugs from third-party builds, and a
significant part of the bugs are package-specific. In order to relieve
that burden a bit (because we are a very small team), we would
appreciate if packagers could make a first triaging of bugs, reporting
to us what looks like actual GIMP bugs, and taking care of their own
packaging issues themselves.

This is why our `configure` script now has the `--with-bug-report-url`
option, allowing you to set your own bug tracker web URL. This way, when
people click the "*Open Bug Tracker*" button it will open the
package bug tracker instead.


## XCF-reader developers: format is documented

Since 2006, our work format, XCF, is
[documented](https://git.gnome.org/browse/gimp/tree/devel-docs/xcf.txt)
thanks to the initial contribution of Henning Makholm. We have recently
updated this document to integrate all the changes to the format since
the GIMP 2.10.0 release.

Any third-party applications wishing to read XCF files can refer to 
this updated documentation. 
The [git log view](https://git.gnome.org/browse/gimp/log/devel-docs/xcf.txt) 
may actually be more interesting since you can more easily spot the changes
and new features which have been documented recently.

Keep in mind that XCF is not meant to be an interchange format
(unlike for instance [OpenRaster](https://www.openraster.org/)) and
this document is not a "specification". 
The XCF reference document is the code itself. 
Nevertheless we are happy to help third-party applications, 
and if you spot any error or issues within this document feel free to 
[open a bug report](https://bugzilla.gnome.org/enter_bug.cgi?product=GIMP) 
so we can fix it.


# GIMP 3 is already on its way…

While GIMP 2.10.0 was still hot and barely released, our developers started
working on GIMP 3. 
One of the main tasks is cleaning the code from the many deprecated pieces 
of code or data as well as from code made useless by the switch to GTK+ 3.x.

The deletion is really going full-speed with more than 
[200 commits](https://git.gnome.org/browse/gimp/log/?h=gtk3-port) made in
less than a month on the gtk3-port git branch and with 9805 lines already
inserted for the 921,630 lines deleted!

*Delete delete delete… exterminate!*

<figure>
<img src="{attach}gimp-2-10-2-exterminate-bugs.png" alt="Exterminate (GTK+2)!">
<figcaption>
Michael Natterer and Jehan portrayed by Aryeom.
<br/>
It's actually misses Simon Budig, a long time contributor who made a big
comeback on the GTK+3 port with dozens of commits!
</figcaption>
</figure>
