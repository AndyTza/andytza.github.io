---
title: "Using a Gaussian Process to Forecast Supernovae Lightcurves"
date: 2020-12-03
tags: [Gaussian Process, Supernovae, SNCOSMO, GP, astronomy]
excerpt: "Short demo how to fit a GP to supernovae lighcurves"
---

I recently got excited about the application of Gaussian Process (GP) forecasting on supernovae lightcurves, especially when it comes to fiting complex photometric behaviour. 

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Using GP&#39;s to forecast SN Ia lighcurves :) <a href="https://t.co/qfWv1vtJ0O">pic.twitter.com/qfWv1vtJ0O</a></p>&mdash; Andy Tzanidakis (@Andy_Tzanidakis) <a href="https://twitter.com/Andy_Tzanidakis/status/1294754197561380866?ref_src=twsrc%5Etfw">August 15, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

In the above example, I used a SALT type Ia supernovae lightcurve assuming a +3 day cadence at ~200Mpc. For each detection, I assign some error that is assumed to be drawn from a Gaussian. In terms of the GP analysis, I mainly used the open-source Python library that is used mainly for GP George. I assumed a standard square exponential kernel and maximized the likelihood for the free parameters for the kernel.

I was quite happy with the preliminary results. After messing around with various kernels (more on Kernels [here](https://www.cs.toronto.edu/~duvenaud/cookbook/)) I found that the current set-up with a simple SE is enough to forecast SN Ia lightcurves. In theory, this can be implemented as a neat tool in unison to TD surveys that perform regularly spectroscopic follow-up resources. Often as an observer one questions the evolution of their lightcurve after 10 or 20 days before their upcoming run. This can greatly impact the exposure times spent on each source since we assume that our source has reached a certain magnitude.

More on this coming soon! Please feel free to contact me if you would like the source code :)