Title: GIMP 2.10.2 Released
Date: 2018-05-20
Category: News
Authors: Wilber
Slug: gimp-2-10-2-released
Summary: GIMP 2.10.2 released (bug fixes, HEIF support and new filters)
Status: draft

It has barely been a month since we released GIMP 2.10.0, and the
version 2.10.2 is already there!
As expected, its main purpose is fixing the various bugs and issues
which can be expected from a major release.

**Therefore 43 bugs have been fixed in less than a month!**

Yet as you may recall, we have also been relaxing the policy for new
features, and this is the first time we will be applying this policy
with features in a minor release! How cool is that?

*For a complete list of changes please see [NEWS](https://git.gnome.org/browse/gimp/tree/NEWS).*

# New features
## Added support for HEIF image format

This release brings you HEIF image support, both for loading and export!

Thanks to Dirk Farin for the HEIF plug-in.

## New filters

TODO: New Spherize filter to wrap an image around a spherical cap

TODO: New Recursive Transform filter to create Droste effect.

# Noteworthy improvements
## Better single-window screenshots on Windows

While our screenshot plug-in was already a lot better in GIMP 2.10.0, we
had a few issues with single-window screenshots on Windows operating
systems, when the target window was hidden behind other windows, or
partly off-screen, as well as when display scaling was activated.

All these issues have been fixed by the new contributor Gil Eliyahu.

## Histogram computation improved

GIMP now calculates histograms in separate threads which eliminates some
UI freezes. This has been implemented with some new internal API which
may be reused later for other cases.

# Working with third-party
## Packagers: set your bug tracker address

As you know, we now have a debug dialog which may pop-up when crashes
occur, with debug information. This dialog opens our bug tracker in a
browser.

We realized that a lot of bugs are getting to us from third-party
builds, and a significant part of the bugs are package-specific. In
order to relieve a bit our burden, since we are a very small team,
we would appreciate if packagers could make a first filtering of bugs,
reporting us what looks like actual core bugs, and taking care of
packaging issues.

This is why our `configure` script now has the `--with-bug-report-url`
option, allowing you to set your own bug tracker web URL. This way, when
people will click the "*Open Bug Tracker*" button, it will open the
package bug tracker instead.

## XCF-reader developers: format is documented

Since 2006, our work format, XCF, is
[documented](https://git.gnome.org/browse/gimp/tree/devel-docs/xcf.txt)
thanks to the initial contribution of Henning Makholm. We have recently
updated this document to integrate all the changes in the format since
GIMP 2.10.0 release.

Any third-party application which wishes to be able to read XCF files is
welcome to get information from this updated documentation. The [git log
view](https://git.gnome.org/browse/gimp/log/devel-docs/xcf.txt) may
actually be more interesting since you can more easily spot the changes
and new features which have been documented these last days.

We remind though that XCF is not meant to be an interchange format
(unlike for instance [OpenRaster](https://www.openraster.org/)) and
this document is not a "specification". The XCF reference document is
the code itself. Nevertheless we are happy to help third-party
applications, and if you spot any error or issues within this document,
feel free to [open a bug
report](https://bugzilla.gnome.org/enter_bug.cgi?product=GIMP) so that
we can fix it.

# GIMP 3 is already on its way…

While GIMP 2.10.0 was still hot, barely released, our developers started
working on GIMP 3 like crazy. One of the main task is cleaning the code
out of the many deprecated pieces of code or data, as well as code made
useless by the switch to GTK+3.

The deletion is really going full-speed, with more than [200
commits](https://git.gnome.org/browse/gimp/log/?h=gtk3-port) made in
less than a month on the GTK+3 branch, with already 9805 lines inserted
for 921630 lines deleted!

*Delete delete delete… exterminate!*

<figure>
<img src="{attach}gimp-2-10-2-exterminate-bugs.png" alt="Exterminate (GTK+2)!">
<figcaption>
Michael Natterer and Jehan portrayed by <a href="http://film.zemarmot.net/">Aryeom</a>.
<br/>
It actually misses Simon Budig, a long time contributor who made a big
comeback on the GTK+3 port with dozens of commits!
</figcaption>
</figure>
