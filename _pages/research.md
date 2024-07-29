---
layout: page
permalink: /research/
title: Research
nav: true
nav_order: 1
---
<!-- Add some styling to the table of contents and support for dark mode -->

<style>
  :root {
    --bg-color-light: #f9f9f9;
    --bg-color-dark: #333333;
    --text-color-light: #333333;
    --text-color-dark: #f9f9f9;
    --border-color-light: #cccccc;
    --border-color-dark: #444444;
  }

  .toc-container {
    background: var(--bg-color-light);
    border: 4px solid var(--border-color-light);
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 30px;
  }
  .toc-title {
    font-size: 1.5em;
    color: var(--text-color-light);
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

  .content-container {
    border: 4px solid var(--border-color-light);
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 30px;
    background: var(--bg-color-light);
  }
  .content-container h2 {
    color: var(--text-color-light);
  }
  .content-container p, .content-container a {
    color: var(--text-color-light);
  }
  .content-container img {
    width: 100%;
    border-radius: 10px;
  }
  .content-container p img {
    width: 100%;
  }
  .content-container p em {
    text-align: center;
  }

  @media (prefers-color-scheme: dark) {
    .toc-container {
      background: var(--bg-color-dark);
      border: 4px solid var(--border-color-dark);
    }
    .toc-title {
      color: var(--text-color-dark);
    }
    .toc-list a {
      color: #66B2FF;
    }

    .content-container {
      border: 4px solid var(--border-color-dark);
      background: var(--bg-color-dark);
    }
    .content-container h2 {
      color: var(--text-color-dark);
    }
    .content-container p, .content-container a {
      color: var(--text-color-dark);
    }
  }
</style>

<div class="toc-container">
  <div class="toc-title">Table of Contents</div>
  <ul class="toc-list">
    <li><a href="#deep-dive-into-slow-time-domain-astronomy">Deep Dive into Slow-Time Domain Astronomy</a></li>
    <li><a href="#characterizing-periodic-signals-in-the-lsst-era">Characterizing Periodic Signals in the LSST Era</a></li>
    <li><a href="#type-ii-supernovae-in-the-local-universe-with-the-zwicky-transient-facility">Type-II Supernovae in the Local Universe with the Zwicky Transient Facility</a></li>
    <li><a href="#galactic-archeology-tomography-of-the-galactic-disk">Galactic Archeology: Tomography of the Galactic Disk</a></li>
  </ul>
</div>

---

## Deep Dive into Slow-Time Domain Astronomy
___

<div class="content-container" style="border-color: #4CAF50;">
  <h2 style="color: #4CAF50;">Exploring Stellar Evolution</h2>
  <p>I am excited about slow-time domain astronomy, particularly studying stellar evolution through slowly evolving variability. Systems like <a href="https://andytza.github.io/Gaia17bpp/">Gaia17bpp</a> offer insights into exotic and extreme stellar binaries. This project is mentored by my advisor, <a href="https://depts.washington.edu/astron/profile/davenport-james/">Professor James Davenport</a>.</p>
  <img src="/images/gaia_dip.png" alt="Location of Gaia19asz on the Gaia HR diagram" />
  <p style="text-align: center;"><em>Example of a long-period-deep stellar variable discovered from the Gaia Alert Archive in unison with the Zwicky Transient Facility</em></p>
</div>

---

## Characterizing Periodic Signals in the LSST Era
___

<div class="content-container" style="border-color: #2196F3;">
  <h2 style="color: #2196F3;">LSST Survey Analysis</h2>
  <p>Under the guidance of Professor Eric Bellm, I work with the Vera C. Rubin Observatory Data Management group on transient alert processing. We focus on calculating and characterizing alert light curve moments and statistical properties for transient classification. Our findings will be published in the <a href="https://dmtn-221.lsst.io/">LSST Data Management Technotes-221</a>.</p>
</div>

---

## Type-II Supernovae in the Local Universe with the Zwicky Transient Facility
___

<div class="content-container" style="border-color: #FF9800;">
  <h2 style="color: #FF9800;">Research on Supernovae</h2>
  <p>I have been researching type-II supernovae in the local universe with the Zwicky Transient Facility (ZTF) under Professor Mansi Kasliwal and Ph.D. student Kishalay De. Our work, which aims to understand supernova populations, will soon be published on ArXiv.</p>
  <img src="/images/CLU_snap.png" alt="Census of the Local Universe Snapshots" />
  <p style="text-align: center;"><em>Science images of type II SNe discovered by the ZTF CLU experiment.</em></p>
  <img src="/images/typeIICLU_Lcs.png" alt="Type II Supernovae Lightcurve Models" />
  <p style="text-align: center;"><em>Modeling type II lightcurves using parametric lightcurve models.</em></p>
</div>

---

## Galactic Archeology: Tomography of the Galactic Disk
___

<div class="content-container" style="border-color: #FF5722;">
  <h2 style="color: #FF5722;">Understanding the Milky Way</h2>
  <p>During my undergraduate studies, I researched the shape of the Milky Way's disk, contributing to the discovery that the disk is oscillating. Our findings suggest dwarf satellite galaxies cause these large-scale oscillations. Learn more from our publications <a href="https://andytza.github.io/publications/">here</a>.</p>
  <img src="/images/sgr-col.gif" alt="Viewing angle from different observers, what the disk looks like!" />
  <p style="text-align: center;"><em>Interaction between the Milky Way and the Sagittarius dwarf satellite galaxy.</em></p>
  <img src="/images/mw.png" alt="Viewing angle from different observers, what the disk looks like!" />
  <p style="text-align: center;"><em>Oscillations of the Galactic disk after interaction with Sagittarius.</em></p>
</div>