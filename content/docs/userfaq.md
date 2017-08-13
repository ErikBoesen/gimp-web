Title: Frequently Asked Questions
Date: 2015-08-14T15:07:00-05:00
Author: Alexandre Prokoudine
lang: en
slug: userfaq

[TOC]

## General questions

### Is there a company or a foundation behind GIMP?

No. We are a diverse group of volunteers from around the world who work on this
project in their spare time. Code-wise most of project contributions come from
Europe where the current GIMP maintainers live. Our translators are an even
more diverse group of contributors, since GIMP is available in
80 languages/locales.

### Can I use GIMP commercially?

Yes, you can. GIMP is free software, it doesn't put restrictions on the kind
of work you produce with it.

### What's the GIMP's license, and how do I comply with it?

GIMP is distributed under terms of General Public License v3 and later. In a
nutshell, this means:

* You are free to use GIMP, for any purpose
* You are free to distribute GIMP
* You can study how GIMP works and change it
* You can distribute changed versions of GIMP

Note that once you distribute modified version of GIMP, you also must publish
your changes to the source code under GPLv3+ as well.

### Someone sold or tried to sell me GIMP on a 3rd party website. Is this legal?

Yes, under terms of the General Public License this is perfectly legal,
provided that the seller also gave you the source code of GIMP and any
modifications he/she introduced.

### Are you trying to develop a Photoshop killer app?

No. Most generic image editors look like Photoshop simply because Adobe's
application was among the first image editors as we know them now, so
developers tend to stick to what people know&nbsp;&mdash; in general terms.

What we aim to do is to create a high-end image manipulation application that
is free to use and modify by everyone, ever.

Feature-wise, the proposed "high-end" status does automatically put GIMP into
direct comparison against Photoshop, but we don't think about competition
much. We have too many ideas of our own to implement, and too many things to
improve before the notion of competition begins to make the slightest sense.

We do, however, acknowledge the fact that people will treat GIMP as Photoshop
replacement no matter what we tell them, and that's all right with us. You
own this software, it's up to you to decide how you make use of it.

### I don't like GIMP's user interface. Why can't you just copy Adobe Photoshop?

In the past, the development in the project was somewhat erratic with regards
to taking usability into consideration, which is rather typical for free
software projects, but inexcusable for a high-end image editor that GIMP aims to become.

Between 2006 and 2013, we worked with Peter Sikking of Man+Machine Works, a
professional usability architect, who helped us shape the project vision for
GIMP, interviews professional users to better understand their workflows and
demands, and wrote functional specifications for various GIMP features.

[This collaboration](http://gui.gimp.org) resulted in major improvements of
GIMP's usability, in particular: the rectangular-based selection/cropping
tools, the unified free/polyline selection tool, the single-window mode, the
upcoming unified transformation tool etc.

While working on functional specifications, Peter researched how various
features are implemented in applications with a partially matching feature set
(such as Adobe Photoshop), but the final design was made to help actual users
complete their tasks as fast as possible. This is exactly the kind of approach
to designing interfaces that we consider to be superior to merely copying user
interaction decisions.

### I don't like the name GIMP. Will you change it?

With all due respect, no.

We've been using the name GIMP for more than 20 years and it's widely known.

The name was originally (and remains) an acronym; although the word "gimp" can
be used offensively in some cultures, that is not our intent.

On top of that, we feel that in the long run, sterilization of language will
do more harm than good. GIMP has been quite popular for a long time in search
engine results compared to the use of the word "gimp". So we think we are on
the right track to make a positive change and make "gimp" something people
actually feel good about. Especially if we add all the features we've been
meaning to implement and fix the user interface.

Finally, if you still have strong feelings about the name "GIMP", you should
feel free to promote the use of the long form GNU Image Manipulation Program
or maintain your own releases of the software under a different name.


## Releases

### When do you release the next version of GIMP?

We release both updates to the current stable version and development versions.

We cut new updates of the stable version in two cases: 1) some newly introduced
bug is knowingly affecting a lot of users; 2) the amount of improvements and
bug fixes is large enough to justify an update&nbsp;&mdash; typically, a few
dozens of each, but there is no rule.

Currently we are cleaning up GIMP code for v2.10 release some time in 2017.

### Why can't you announce dates of future releases?

We are a team of volunteers with day jobs, families, and personal interests
beyond development of software. Given that, we try to avoid the situation when
we cannot deliver a release, because something else at work/in family came up.

Instead we provide a [feature-based roadmap](http://wiki.gimp.org/wiki/Roadmap)
that roughly outlines, in what order we will be implementing various popular
requests made by users.

### Aren't you interested in doing paid development of GIMP via crowdfunding?

We already have jobs we love. However we actively encourage personal
fundraisers by trusted contributors. There are two such campaigns running at
the moment. You can learn more about them on the
[Donate](https://www.gimp.org/donating/) page.

If you are willing to launch a campaign and develop some features for GIMP,
talk to us about changes you are about to propose. We'll help you to flesh
out your idea and promote it to a larger community.

### Will you release GIMP for Android or iOS devices?

Apps for mobile devices imply a different approach to designing interfaces.
Since most of GIMP's source code is related to the user interface one way or
another, it means that we would have to design and then develop a whole new
application. Given the current manpower, we'd rather focus on delivering a
great image manipulation program for desktop users.

However, we are interested to consult 3rd party developers willing to make a
free/libre GIMP-branded image manipulation program for Android. As for iOS,
please note that GIMP is licensed under GNU GPL v3+ which conflicts with
Apple's Terms of Service. For a full story, please read
[this article](https://www.engadget.com/2011/01/09/the-gpl-the-app-store-and-you/)
by Richard Gaywood.

## Features

### When will GIMP support HDR imaging and processing with 16bit per color channel precision?

GIMP 2.10 will be the first version to feature processing with precision of
16-bit and 32-bit per color channel. This version is currently in the works,
and this particular feature has already been implemented and available in
v2.9.2 and newer releases.

### When will GIMP support any kind of non-destructive editing like adjustment layers, layer filters, and/or full-blown node-based editing?

Currently the plan is to introduce non-destructive editing in GIMP 3.2. This
is a huge change that will require rethinking the workflow, designing a new
file format for GIMP projects etc.

### Will GIMP open raw (.NEF, .CR2 etc.) files from my camera?

Currently you need to install [UFRaw](http://ufraw.sourceforge.net/) to open
raw files. It's both a standalone application and a GIMP plug-in for opening
and processing raw images.

Upcoming GIMP 2.10 is featuring plug-ins for using
[darktable](http://www.darktable.org/) and [RawTherapee](http://rawtherapee.com/) to process raw images on Linux, as well as a preference
for a default raw processing plug-in.

### I do a lot of desktop publishing related work. Will you ever support CMYK?

Yes, better support for CMYK has been on our roadmap for a long time. However
this project has certain prerequisites such as the complete port of GIMP to
GEGL.

The idea, how we want to make this work, was introduced by user interaction
architect Peter Sikking at Libre Graphics Meeting 2009 and later&nbsp;&mdash;
in his two-part article in his company's blog:
[1](http://blog.mmiworks.net/2009/05/gimp-enter.html),
[2](http://blog.mmiworks.net/2009/06/gimp-squaring-cmyk-circle.html). Please
take some time to read up on that.

It's worth mentioning that currently CMYK is considered by us a low-priority
project. Here's why.

Things like non-destructive editing are required by pretty much all
users&nbsp;&mdash; photographers, designers, desktop publishing engineers,
and even scientists. At the same time, CMYK is required only by a small subset
of our user base. We prioritize our work accordingly.

Note that should a new developer join the team to specifically work on
CMYK-related features, we will do our best to help him/her to complete this
project and get it to our users as soon as possible. Now that GIMP (as of git
master) has been ported to GEGL, adding better CMYK support is finally a
sensible idea.

### I don't like some changes you introduced in recent GIMP versions. Why can't you add a checkbox to disable them?

We realize that some changes are disruptive to some groups of users,
especially those who got used to GIMP as an image editor for doing quick fixes
to lossy files such as JPEG, PNG etc. (i.e. files that cannot store layers,
masks, custom channels, paths).

However, adding a switch for every change we make adds numerous levels of
complexity that we'd rather avoid. Additionally, it would lead to dramatically
changing the way we mean GIMP to work. Hence we respectfully disagree to make
extra behaviour switches.

At the same time, if you don't wish to abandon GIMP completely, we recommend
having a look at the
[Saver and Save/export clean plug-ins](http://www.shallowsky.com/software/gimp-save/)
by Akkana Peck, as well as at various GIMP forks on GitHub, although typically
they aren't maintained up to date with regards to bugfixes.

### Why doesn't GIMP use GTK+3?

We made a preliminary port of GIMP to GTK+3 a few years ago and intend to
complete it once v2.10 is out. GTK+3 based GIMP will be eventually released
as v3.0 (see the [roadmap](http://wiki.gimp.org/wiki/Roadmap) for reference).

The reason we prioritize it that way is that users who don't make a heavy
use of Wacom tablets on Windows can live with GTK+2 based GIMP another year
or so. However not providing high bit depth precision for editing makes GIMP
unusable in professional workflows involving color grading and retouching.

While completing the GTK+3 port, we will have to break API/ABI compatibility
to make GIMP's custom widgets work with GTK+3. Moreover, we need to break a
few more things to make GIMP's architecture cleaner and prepare it for
non-destructive editing (a feature currently planned for v3.2).

## Tips

### How do I draw a straight line?

In any of the drawing tools (Pen, Pencil, etc.), click on one endpoint of the
line. Then hold the shift key and click on the other endpoint.

### How do I draw a circle or square?

In the Rectangular or Elliptical selection tool, click in one corner of your
square or circle, then press Shift while dragging toward the other corner. Or
enable the checkbox for Fixed: Aspect Ratio in tool options and make sure the
aspect ratio is set to 1:1 before starting your square or circular selection.

Once you have a selection, Edit->Stroke Selection... will draw a line the
shape of the selection you just made.

For curved selections, like circles, stroking with the Paintbrush paint tool
will usually give a smoother looking line. You can get an even smoother line
by converting the selection to a path (Select->To Path), then using
Edit->Stroke Path... instead of Stroke Selection...

## Troubleshooting

### My graphic tablet doesn't work on Windows/Mac. Does GIMP support advanced input devices such as Wacom?

Yes, GIMP does support graphic tablets and maps pressure, stroke speed and
other events to its advanced brush engine properties. However, the version of
the user interface toolkit that  GIMP currently relies on (GTK+ 2.x) is broken
beyond repair on Windows and Mac with regards to supporting advanced input
devices such as Wacom's.

To fix this, we need to port GIMP to GTK+3 where everything works as expected.
Some work on that has already been done in the
[gtk3-port](https://git.gnome.org/browse/gimp/log/?h=gtk3-port) Git branch.
However we won't have time to give this our full attention until GIMP 2.10 is
out. We encourage interested developers to either work on the GTK+3 port or,
better yet, help us finish GIMP 2.10.

###  My macOS system doesn't let me open GIMP. What do I do?

We haven't yet joined the Apple Developer Program, so the DMG files we provide
are unsigned, hence the "unidentified developer" warning. Please follow the
procedure [described in the Apple's knowledge base](https://support.apple.com/kb/PH21769).

## Contributing

### I'm a developer. How do I help you?

Great! Please check the [wiki](http://wiki.gimp.org/wiki/Hacking:Developer_FAQ)
for introduction on GIMP development and talk to us on
[IRC](http://www.gimp.org/irc.html).

### I'm not a developer. Can I still help you somehow?

Absolutely! Here are some of the ways you can help us:

* Post awesome art online and tell people you made it with GIMP.
* Help new GIMP users in an online forum you visit.
* Write a great tutorial on getting something done with GIMP and post it
online or submit to [GIMP Magazine](http://gimpmagazine.org/).
* Do a GIMP workshop in your local community.
* Improve translation of [GIMP](https://l10n.gnome.org/module/gimp/) and/or its
[user manual](http://docs.gimp.org/) into your native language (read
[this page](https://wiki.gnome.org/TranslationProject) to find out, how).
