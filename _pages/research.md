---
layout: page
permalink: /research/
title: Research
nav: true
nav_order: 1
---

<!-- Add some styling to the table of contents -->
<style>
  .toc-container {
    background: #f9f9f9;
    border: 4px solid #cccccc;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 30px;
  }
  .toc-title {
    font-size: 1.5em;
    color: #333333;
    text-align: center;
    margin-bottom: 10px;
  }
  .toc-list {
    list-style: none;
    padding: 0;
  }
  .toc-list li {
    margin: 10px 0;
  }
  .toc-list a {
    text-decoration: none;
    color: #007BFF;
    font-weight: bold;
  }
  .toc-list a:hover {
    text-decoration: underline;
  }
</style>


## Probing the Circumstellar Envionments around Dwarf

<div style="border: 4px solid #E6A8D7; padding: 20px; border-radius: 15px; margin-bottom: 30px; background: #f0fff4;">
  <h2 style="color: #E6A8D7;">Main-Sequence Dipper Stars</h2>
  <p>In 2016, <a href="https://ui.adsabs.harvard.edu/abs/2016MNRAS.457.3988B/abstract">Boyajian et al. (2016)</a> revealed one of the first main-sequence stars with erratic dimming events, stirring discussions and theories on the origins of such rare stars. Only a small number of similar systems have been identified since, leaving many open questions about their origins and if they are connected at all with the initial discovery of the Boyajian star. My Ph.D dissertation work pioneers the first ever large-scale systematic search for these irregularly variable dwarf stars, analyzing extensive time-domain data to assess their occurrence and potential origins, such as planetary-scale collisions or Earth-Moon-like formation events. This work also drives the development of scalable tools for examining stellar variability across billions of stars, expanding our ability to probe diverse behavior of stellar variability phenomena.</p>
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
    <img src="/images/msenvs.png" alt="Artist rendering" style="width: 100%; border-radius: 10px;" />
    <img src="/images/msss.png" alt="Gaia17bpp and WISE Comparison" style="width: 100%; border-radius: 10px;" />
  </div>
  <p style="text-align: center;"><em></em></p>
</div>




## Eclipses by Large Disks
___

<div style="border: 4px solid #4CAF50; padding: 20px; border-radius: 15px; margin-bottom: 30px; background: #f0fff4;">
  <h2 style="color: #4CAF50;">Gaia17bpp and other Disk Eclipses</h2>
  <p>We are now at the cusp of probing stellar variability on timescales spanning decades, which opens the door to uncovering new and rare types of variable stars. In my first year of graduate school, I serendipitously discovered <a href="https://andytza.github.io/Gaia17bpp/">Gaia17bpp</a> (<a href="https://iopscience.iop.org/article/10.3847/1538-4357/aceda7">Tzanidakis et al. 2023</a>), a system that we believe could be an extreme analog to the famous <a href="https://arxiv.org/pdf/1004.2464.pdf">Epsilon Aurigae</a> binary, and currently holds the record for the longest duration dimming event we have found. This discovery offers a unique opportunity to study eclipses caused by massive circumstellar disks, pushing the boundaries of our understanding of long-period stellar variables.</p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
    <img src="/images/disk-eclipse-comp.png" alt="Disk Eclipse Comparison" style="width: 100%; border-radius: 10px;" />
    <img src="/images/Gaia17bpp_WISE.gif" alt="Gaia17bpp and WISE Comparison" style="width: 100%; border-radius: 10px;" />
  </div>
  
  <p style="text-align: center;"><em>Left: Light curve mosaic of known Epsilon Aurigae analog systems including Gaia17bpp. Right: Movie from WISE revealing long-term variability.</em></p>
</div>

## Time-Series Features in the LSST Era
___

<div style="border: 4px solid #2196F3; padding: 20px; border-radius: 15px; margin-bottom: 30px; background: #e3f2fd;">
  <h2 style="color: #2196F3;">LSST Time-Series Features</h2>
  <p> In the era of large time-domain surveys with gappy, multi-band, and sparse photometric measurements, time series features have become an important tool to search for populations of variable stars and transient phenomena <a href="https://ui.adsabs.harvard.edu/abs/2011ApJ...733...10R/abstract">(Richards et al. 2011)</a>. During my first year of graduate school, I worked with Professor Eric Bellm and the UW Data Management group on transient alert processing. My interests aimed to characterize the recovery of periodic objects in data like the LSST alerts and what are the optimum techniques used to increase the efficiency of finding reliable periods. Some of my work also included characterizing alert light curve time series features and statistical properties of transients and variable stars. Our findings have been reported in the <a href="https://dmtn-221.lsst.io/">LSST Data Management Technotes-221</a>.</p>
  <img src="/images/lsst-lc.png" alt="LSST simulated light curves of RR Lyrae and eclipsing binaries." style="width:100%; border-radius: 10px;" />
  <p style="text-align: center;"><em>Synthetic LSST Alert-like photometry of two periodic sources: RR Lyrae and Eclipsing Binaries.</em></p>
</div>

---

## Type-II Supernovae in the Local Universe with the Zwicky Transient Facility
___

<div style="border: 4px solid #FF9800; padding: 20px; border-radius: 15px; margin-bottom: 30px; background: #fff3e0;">
  <h2 style="color: #FF9800;">ZTF Census of the Local Universe (CLU) Experiment</h2>
  <p> During my post-baccalaureate research, I was fortunate to work under <a href="https://sites.astro.caltech.edu/~mansi/">Professor Mansi Kasiwal</a>, <a href="https://dekishalay.github.io/">Professor Kishalay</a> at Caltech to co-lead the Zwicky Transient Facility (ZTF) Census of the Local Universe (CLU) supernova experiment. 
  In short, CLU aimed achieve high completeness of all known discovered supernovae by ZTF within 200 Mpc (see <a href="https://arxiv.org/abs/2004.09029">De et al. 2020</a>). In parallel, I was interested in probing the luminosity function and distribution of core-collapse Type-II supernovae to better understand their origins and how their properties change as a function of host-galaxy.</p>
  <img src="/images/CLU_snap.png" alt="Census of the Local Universe Snapshots" style="width:100%; border-radius: 10px;" />
  <p style="text-align: center;"><em>Science images of type II SNe discovered by the ZTF CLU experiment.</em></p>
  <img src="/images/typeIICLU_Lcs.png" alt="Type II Supernovae Lightcurve Models" style="width:100%; border-radius: 10px;" />
  <p style="text-align: center;"><em>Modeling type II lightcurves using parametric lightcurve models.</em></p>
</div>

---

## Galactic Archeology: Tomography of the Galactic Disk
___

<div style="border: 4px solid #FF5722; padding: 20px; border-radius: 15px; margin-bottom: 30px; background: #fbe9e7;">
  <h2 style="color: #FF5722;">Understanding the Milky Way</h2>
  <p>During my undergraduate studies, I was extensively interested in probing the 3D distribution of stars in the Milky Way's disk under the mentorship of <a href="https://google.com">Professor Allyson Sheffield</a>, <a href="http://user.astro.columbia.edu/~kvj/">Professor Kathryn Johnston</a>, and <a href="https://icc.ub.edu/people/647">Dr. Chervin Laporte</a>. I was very fortunate to be part of a few studies that uncovered observational and simulated N-body models that the Galactic disk is oscillating and kicking out stars from the disk into the Galactic halo, due to past dwarf satellite galaxy interactions with the Milky Way (<a href="https://arxiv.org/pdf/1803.11198.pdf">Laporte et al. 2018</a>, <a href="https://arxiv.org/pdf/1801.01171.pdf">Sheffield et al. 2018</a>).</p>
  <img src="/images/sgr-col.gif" alt="Viewing angle from different observers, what the disk looks like!" style="width:100%; border-radius: 10px;" />
  <p style="text-align: center;"><em>Interaction between the Milky Way and the Sagittarius dwarf satellite galaxy.</em></p>
  <img src="/images/mw.png" alt="Viewing angle from different observers, what the disk looks like!" style="width:100%; border-radius: 10px;" />
  <p style="text-align: center;"><em>Oscillations of the Galactic disk after interaction with Sagittarius.</em></p>
</div>
