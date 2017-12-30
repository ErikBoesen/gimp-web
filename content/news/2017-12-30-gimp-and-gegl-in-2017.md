Title: GIMP and GEGL in 2017
Date: 2017-12-31
Category: News
Authors: Wilber
Slug: gimp-and-gegl-in-2017
Summary: When you say you mostly do bugfixing now, seven kinds of new features will crawl under your bed and bite your silly toes off. If we were to come up with a short summary for 2017, it would be along those very lines.

When you say you _mostly_ do bugfixing now, seven kinds of new features will crawl under your bed and bite your silly toes off. If we were to come up with a short summary for 2017, it would be along those very lines.

So yes, we ended up with more new features that, however, make GIMP faster and improve workflows. Here's just a quick list of the top v2.10 parole violators: multi-threading via GEGL, linear color space workflow, better support for CIE LCH and CIE LAB color spaces, much faster on-canvas Warp Transform tool, complete on-canvas gradients editing, better PSD support, metadata viewing and editing, under- and overexposure warning on the canvas.

All of the above features (and many more) are available in GIMP 2.9.8 released earlier this month. We are now in the strings freeze mode which means there will be very few changes to the user interface so that translators could safely do their job in time for the v2.10 release.

Everyone is pretty tired of not having GIMP 2.10 out by now, so we _only_ work on bugs that block the v2.10 release. There are currently [25 such bugs](https://bugzilla.gnome.org/buglist.cgi?quicksearch=product%3A%22gimp%22%20severity%3Ablocker%20target%3A2.10&list_id=276540). Some are relatively easy to fix, some require more time and effort. Some have patches or there is work in progress, and some need further investigation. We will get there faster, if more people join to hack on GIMP.

Speaking of which, one thing that has changed in the GIMP project for the better this year is the workload among top contributors. Michael Natterer is still responsible for 33% of all GIMP commits in the past 12 months, but that's a ca. 30% decrease from the last year. Jehan Pagès and Ell now have a 38% share of all contributions, and Øyvind Kolås tops that with his 5% thanks to the work on layers blending/compositing and linear color space workflow in GIMP.

In particular, Ell fixed most of the bugs between 2.9.6 and 2.9.8, implemented on-canvas gradients editing, introduced other enhancements, and did a lot of work on tuning performance in both GIMP and GEGL.

Another increasingly active contributor in the GEGL project is Debarshi Ray who uses the library for his project, GNOME Photos. Debarshi focused mostly on GEGL operations useful for digital photography such as exposure and shadows-highlights, and did quite a lot of bugfixing. We also got a fair share of contributions from Thomas Manni who added some interesting experimental filters like SLIC (Simple Linear Iterative Clustering) and improved existing filters.

At least some of the work done by Øyvind Kolås on both GEGL and GIMP this year was sponsored by you, the GIMP community, via [Patreon](https://www.patreon.com/pippin) and [Liberapay](https://liberapay.com/pippin) platforms. Please see his [post on 2017 crowdfunding results](https://www.patreon.com/posts/first-year-on-15787128) for details and consider supporting him. Improving GEGL is crucial for GIMP to become a state-of-the art professional image editing program. Over the course of 2017, programming activity in GEGL increased by 120% in terms of commits, and we'd love to see the dynamics keep up in 2018 and onwards.

Even though the focus of another crowdfunded effort by Jehan Pagès and Aryeom Han is to create a [animated short movie](https://film.zemarmot.net/en/), Jehan Pagès contributed roughly 1/5 of code changes this year, fixing bugs, improving painting-related features, and working on a much more sophisticated animation plug-in currently available in a [dedicated Git branch](https://git.gnome.org/browse/gimp/log/?h=wip/animation). Hence supporting this project results in better user experience for GIMP users. You can help fund Jehan and Aryeom on both [Patreon](https://www.patreon.com/zemarmot) and [Liberapay](https://liberapay.com/ZeMarmot).

We also want to thank Julien Hardelin who has been a great help in updating the user manual for upcoming v2.10, as well as all the translators and people who contributed patches. They don't get nearly as much praise as they deserve.

Happy 2018!