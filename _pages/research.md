---
layout: page
permalink: /research/
title: Research
nav: true
nav_order: 1
---

<script>document.documentElement.classList.add('rm-js');</script>

<style>
  /* ===== Research mosaic — everything is scoped under #research-mosaic ===== */
  #research-mosaic {
    --rm-gap: 10px;
    --rm-row: 170px;
    --rm-radius: 15px;
  }

  #research-mosaic .rm-hint {
    margin: 0 0 1rem;
    font-size: 0.95em;
    color: var(--global-text-color-light, #6b6b6b);
  }

  /* ---- Mosaic grid ---- */
  #research-mosaic .rm-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-auto-rows: var(--rm-row);
    grid-auto-flow: dense;
    gap: var(--rm-gap);
    margin-bottom: 2rem;
  }

  #research-mosaic .rm-tile {
    position: relative;
    display: block;
    overflow: hidden;
    padding: 0;
    margin: 0;
    border: 4px solid var(--accent, #cccccc);
    border-radius: var(--rm-radius);
    background: #000;
    cursor: pointer;
    text-align: left;
    color: #fff;
    font: inherit;
    outline: none;
    transition: transform 0.25s ease, box-shadow 0.25s ease;
  }
  #research-mosaic .rm-tile:hover,
  #research-mosaic .rm-tile:focus-visible {
    transform: translateY(-3px);
    box-shadow: 0 10px 28px rgba(0, 0, 0, 0.28);
  }
  #research-mosaic .rm-tile:focus-visible {
    box-shadow: 0 0 0 3px var(--global-bg-color, #fff), 0 0 0 6px var(--accent, #333);
  }
  #research-mosaic .rm-tile img {
    display: block;
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
    transition: transform 0.5s ease;
  }
  #research-mosaic .rm-tile:hover img,
  #research-mosaic .rm-tile:focus-visible img {
    transform: scale(1.05);
  }
  #research-mosaic .rm-tile__label {
    position: absolute;
    left: 0; right: 0; bottom: 0;
    padding: 28px 12px 10px;
    background: linear-gradient(to top, rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0));
    font-weight: 600;
    font-size: 0.9em;
    line-height: 1.25;
    opacity: 0;
    transform: translateY(6px);
    transition: opacity 0.25s ease, transform 0.25s ease;
  }
  #research-mosaic .rm-tile__label::before {
    content: "";
    display: inline-block;
    width: 10px; height: 10px;
    margin-right: 8px;
    border-radius: 50%;
    background: var(--accent, #ccc);
    vertical-align: 0;
  }
  #research-mosaic .rm-tile:hover .rm-tile__label,
  #research-mosaic .rm-tile:focus-visible .rm-tile__label {
    opacity: 1;
    transform: none;
  }
  @media (hover: none) {
    #research-mosaic .rm-tile__label { opacity: 1; transform: none; }
  }

  /* Tile sizes that make the mosaic */
  #research-mosaic .rm-tile--wide { grid-column: span 2; }
  #research-mosaic .rm-tile--tall { grid-row: span 2; }
  #research-mosaic .rm-tile--big  { grid-column: span 2; grid-row: span 2; }

  @media (max-width: 900px) {
    #research-mosaic { --rm-row: 150px; }
    #research-mosaic .rm-grid { grid-template-columns: repeat(3, 1fr); }
  }
  @media (max-width: 600px) {
    #research-mosaic { --rm-row: 130px; --rm-gap: 8px; }
    #research-mosaic .rm-grid { grid-template-columns: repeat(2, 1fr); }
  }

  /* ---- Project source blocks (hidden when JS builds the mosaic; shown as plain boxes without JS) ---- */
  html.rm-js #research-mosaic .rm-projects { display: none; }
  #research-mosaic .rm-project {
    border: 4px solid var(--accent, #cccccc);
    border-radius: var(--rm-radius);
    background: var(--rm-tint, #f9f9f9);
    padding: 20px;
    margin-bottom: 30px;
  }

  /* Shared content styling (used both in the no-JS fallback and inside the pop-up) */
  #research-mosaic .rm-section {
    margin: 0 0 0.35rem;
    font-size: 0.95em;
    color: var(--global-text-color-light, #6b6b6b);
  }
  #research-mosaic .rm-project h2,
  #research-mosaic .rm-modal__content h2 {
    margin: 0 0 0.75rem;
    color: var(--accent, #333);
    font-size: 1.6em;
    line-height: 1.2;
  }
  #research-mosaic .rm-body p { margin: 0 0 1rem; }
  #research-mosaic .rm-body p:last-child { margin-bottom: 1.25rem; }
  #research-mosaic .rm-figrow {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
  }
  #research-mosaic .rm-fig { margin: 0 0 1rem; }
  #research-mosaic .rm-fig img,
  #research-mosaic .rm-figrow img {
    display: block;
    width: 100%;
    border-radius: 10px;
  }
  #research-mosaic .rm-fig figcaption,
  #research-mosaic .rm-caption {
    text-align: center;
    font-style: italic;
    margin: 0.6rem 0 0;
  }
  @media (max-width: 600px) {
    #research-mosaic .rm-figrow { grid-template-columns: 1fr; }
  }

  /* ---- Pop-up ---- */
  #research-mosaic .rm-modal {
    position: fixed;
    inset: 0;
    z-index: 9999;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px;
  }
  #research-mosaic .rm-modal[hidden] { display: none; }
  #research-mosaic .rm-modal__backdrop {
    position: absolute;
    inset: 0;
    background: rgba(10, 10, 10, 0.62);
    -webkit-backdrop-filter: blur(4px);
    backdrop-filter: blur(4px);
    animation: rm-fade 0.2s ease-out;
  }
  #research-mosaic .rm-modal__panel {
    position: relative;
    width: min(920px, 100%);
    max-height: calc(100vh - 40px);
    max-height: calc(100dvh - 40px);
    overflow-y: auto;
    border: 4px solid var(--accent, #cccccc);
    border-radius: var(--rm-radius);
    background: var(--rm-tint, #ffffff);
    color: var(--global-text-color, #333333);
    padding: 24px 26px 20px;
    box-shadow: 0 24px 60px rgba(0, 0, 0, 0.35);
    animation: rm-pop 0.25s ease-out;
  }
  html[data-theme="dark"] #research-mosaic .rm-modal__panel,
  html[data-theme="dark"] #research-mosaic .rm-project {
    background: color-mix(in srgb, var(--accent, #888) 14%, var(--global-card-bg-color, #1c1c1c));
  }
  #research-mosaic .rm-modal__close {
    position: absolute;
    top: 12px; right: 12px;
    width: 38px; height: 38px;
    border: 2px solid var(--accent, #888);
    border-radius: 50%;
    background: var(--global-bg-color, #fff);
    color: var(--global-text-color, #333);
    font-size: 1.35em;
    line-height: 1;
    cursor: pointer;
    display: grid;
    place-items: center;
    padding: 0;
  }
  #research-mosaic .rm-modal__close:hover,
  #research-mosaic .rm-modal__close:focus-visible {
    background: var(--accent, #888);
    color: #fff;
    outline: none;
  }
  #research-mosaic .rm-modal__content { padding-right: 36px; }
  #research-mosaic .rm-modal__content .rm-body,
  #research-mosaic .rm-modal__content .rm-fig,
  #research-mosaic .rm-modal__content .rm-figrow,
  #research-mosaic .rm-modal__content .rm-caption { padding-right: 0; }

  #research-mosaic .rm-modal__nav {
    display: flex;
    justify-content: space-between;
    gap: 12px;
    margin-top: 0.5rem;
    padding-top: 14px;
    border-top: 2px solid var(--accent, #ccc);
  }
  #research-mosaic .rm-modal__navbtn {
    flex: 1 1 0;
    max-width: 48%;
    border: 0;
    background: transparent;
    color: var(--global-text-color, #333);
    font: inherit;
    text-align: left;
    padding: 6px 8px;
    border-radius: 8px;
    cursor: pointer;
  }
  #research-mosaic .rm-modal__navbtn--next { text-align: right; }
  #research-mosaic .rm-modal__navbtn small {
    display: block;
    font-size: 0.8em;
    color: var(--global-text-color-light, #6b6b6b);
  }
  #research-mosaic .rm-modal__navbtn strong { font-weight: 600; }
  #research-mosaic .rm-modal__navbtn:hover,
  #research-mosaic .rm-modal__navbtn:focus-visible {
    background: color-mix(in srgb, var(--accent, #888) 22%, transparent);
    outline: none;
  }

  @keyframes rm-fade { from { opacity: 0; } to { opacity: 1; } }
  @keyframes rm-pop  { from { opacity: 0; transform: translateY(12px) scale(0.98); } to { opacity: 1; transform: none; } }
  @media (prefers-reduced-motion: reduce) {
    #research-mosaic * { animation: none !important; transition: none !important; }
  }
</style>


<div id="research-mosaic">

  <p class="rm-hint">Click any image to read about that project.</p>

  <!-- The mosaic is built here by the script below, one tile per image -->
  <div class="rm-grid" id="rm-grid" aria-label="Research image mosaic"></div>

  <!-- ===================================================================
       PROJECT CONTENT
       Each <article> is one research area. The script turns every image
       inside it into a mosaic tile and shows the whole article in a pop-up.
       To add a project: copy an <article>, change data-accent / data-tint,
       the text, and the images. Nothing else needs editing.
       =================================================================== -->
  <section class="rm-projects" id="rm-projects">

    <article class="rm-project" id="main-sequence-dipper-stars" data-accent="#E6A8D7" data-tint="#ffe3d7">
      <p class="rm-section">Circumstellar Environments around Dwarf Stars</p>
      <h2>Main-Sequence Dipper Stars</h2>
      <div class="rm-body">
        <p>In 2016, <a href="https://ui.adsabs.harvard.edu/abs/2016MNRAS.457.3988B/abstract">Boyajian et al. (2016)</a> revealed one of the first main-sequence stars with erratic dimming events, stirring discussions and theories on the origins of such rare stars. Only a small number of similar systems have been identified since, leaving many open questions about their origins and if they are connected at all with the initial discovery of the Boyajian star. My Ph.D dissertation work conducts the first ever large-scale systematic search for these irregularly variable dwarf stars, analyzing extensive time-domain data to assess their occurrence and potential origins, such as planetary-scale collisions or Earth-Moon-like formation events. This work also drives the development of scalable tools for examining stellar variability across billions of stars, expanding our ability to probe diverse behavior of stellar variability phenomena.</p>
      </div>
      <div class="rm-figrow">
        <img src="/images/msdip.jpeg" alt="Sky position of main-sequence dipper stars and example of ZTF light curve." />
        <img src="/images/mslc1.png" alt="Disk Eclipse Comparison" />
      </div>
      <p class="rm-caption"><em></em></p>
    </article>

    <article class="rm-project" id="gaia17bpp-and-other-disk-eclipses" data-accent="#4CAF50" data-tint="#f0fff4">
      <p class="rm-section">Eclipses by Large Disks</p>
      <h2>Gaia17bpp and other Disk Eclipses</h2>
      <div class="rm-body">
        <p>We are now at the cusp of probing stellar variability on timescales spanning decades, which opens the door to uncovering new and rare types of variable stars. In my first year of graduate school, I serendipitously discovered <a href="https://andytza.github.io/Gaia17bpp/">Gaia17bpp</a> (<a href="https://iopscience.iop.org/article/10.3847/1538-4357/aceda7">Tzanidakis et al. 2023</a>), a system that we believe could be an extreme analog to the famous <a href="https://arxiv.org/pdf/1004.2464.pdf">Epsilon Aurigae</a> binary, and currently holds the record for the longest duration dimming event we have found. This discovery offers a unique opportunity to study eclipses caused by massive circumstellar disks, pushing the boundaries of our understanding of long-period stellar variables.</p>
      </div>
      <div class="rm-figrow">
        <img src="/images/disk-eclipse-comp.png" alt="Disk Eclipse Comparison" />
        <img src="/images/Gaia17bpp_WISE.gif" alt="Gaia17bpp and WISE Comparison" />
      </div>
      <p class="rm-caption"><em>Left: Light curve mosaic of known Epsilon Aurigae analog systems including Gaia17bpp. Right: Movie from WISE revealing long-term variability.</em></p>
    </article>

    <article class="rm-project" id="lsst-time-series-features" data-accent="#2196F3" data-tint="#e3f2fd">
      <p class="rm-section">Time-Series Features in the LSST Era</p>
      <h2>LSST Time-Series Features</h2>
      <div class="rm-body">
        <p>In the era of large time-domain surveys with gappy, multi-band, and sparse photometric measurements, time series features have become an important tool to search for populations of variable stars and transient phenomena <a href="https://ui.adsabs.harvard.edu/abs/2011ApJ...733...10R/abstract">(Richards et al. 2011)</a>. During my first year of graduate school, I worked with Professor Eric Bellm and the UW Data Management group on transient alert processing. My interests aimed to characterize the recovery of periodic objects in data like the LSST alerts and what are the optimum techniques used to increase the efficiency of finding reliable periods. Some of my work also included characterizing alert light curve time series features and statistical properties of transients and variable stars. Our findings have been reported in the <a href="https://dmtn-221.lsst.io/">LSST Data Management Technotes-221</a>.</p>
      </div>
      <figure class="rm-fig">
        <img src="/images/lsst-lc.png" alt="LSST simulated light curves of RR Lyrae and eclipsing binaries." />
        <figcaption>Synthetic LSST Alert-like photometry of two periodic sources: RR Lyrae and Eclipsing Binaries.</figcaption>
      </figure>
    </article>

    <article class="rm-project" id="ztf-census-of-the-local-universe" data-accent="#FF9800" data-tint="#fff3e0">
      <p class="rm-section">Type-II Supernovae in the Local Universe with the Zwicky Transient Facility</p>
      <h2>ZTF Census of the Local Universe (CLU) Experiment</h2>
      <div class="rm-body">
        <p>During my post-baccalaureate research, I was fortunate to work under <a href="https://sites.astro.caltech.edu/~mansi/">Professor Mansi Kasiwal</a>, <a href="https://dekishalay.github.io/">Professor Kishalay</a> at Caltech to co-lead the Zwicky Transient Facility (ZTF) Census of the Local Universe (CLU) supernova experiment. In short, CLU aimed achieve high completeness of all known discovered supernovae by ZTF within 200 Mpc (see <a href="https://arxiv.org/abs/2004.09029">De et al. 2020</a>). In parallel, I was interested in probing the luminosity function and distribution of core-collapse Type-II supernovae to better understand their origins and how their properties change as a function of host-galaxy.</p>
      </div>
      <figure class="rm-fig">
        <img src="/images/CLU_snap.png" alt="Census of the Local Universe Snapshots" />
        <figcaption>Science images of type II SNe discovered by the ZTF CLU experiment.</figcaption>
      </figure>
      <figure class="rm-fig">
        <img src="/images/typeIICLU_Lcs.png" alt="Type II Supernovae Lightcurve Models" />
        <figcaption>Modeling type II lightcurves using parametric lightcurve models.</figcaption>
      </figure>
    </article>

    <article class="rm-project" id="understanding-the-milky-way" data-accent="#FF5722" data-tint="#fbe9e7">
      <p class="rm-section">Galactic Archeology: Tomography of the Galactic Disk</p>
      <h2>Understanding the Milky Way</h2>
      <div class="rm-body">
        <p>During my undergraduate studies, I was extensively interested in probing the 3D distribution of stars in the Milky Way's disk under the mentorship of <a href="https://google.com">Professor Allyson Sheffield</a>, <a href="http://user.astro.columbia.edu/~kvj/">Professor Kathryn Johnston</a>, and <a href="https://icc.ub.edu/people/647">Dr. Chervin Laporte</a>. I was very fortunate to be part of a few studies that uncovered observational and simulated N-body models that the Galactic disk is oscillating and kicking out stars from the disk into the Galactic halo, due to past dwarf satellite galaxy interactions with the Milky Way (<a href="https://arxiv.org/pdf/1803.11198.pdf">Laporte et al. 2018</a>, <a href="https://arxiv.org/pdf/1801.01171.pdf">Sheffield et al. 2018</a>).</p>
      </div>
      <figure class="rm-fig">
        <img src="/images/sgr-col.gif" alt="Viewing angle from different observers, what the disk looks like!" />
        <figcaption>Interaction between the Milky Way and the Sagittarius dwarf satellite galaxy.</figcaption>
      </figure>
      <figure class="rm-fig">
        <img src="/images/mw.png" alt="Viewing angle from different observers, what the disk looks like!" />
        <figcaption>Oscillations of the Galactic disk after interaction with Sagittarius.</figcaption>
      </figure>
    </article>

  </section>

  <!-- ===== Pop-up (filled in by the script) ===== -->
  <div class="rm-modal" id="rm-modal" hidden role="dialog" aria-modal="true" aria-labelledby="rm-modal-title">
    <div class="rm-modal__backdrop" data-rm-close></div>
    <div class="rm-modal__panel" tabindex="-1">
      <button class="rm-modal__close" type="button" data-rm-close aria-label="Close">&times;</button>
      <div class="rm-modal__content" id="rm-modal-content"></div>
      <div class="rm-modal__nav">
        <button class="rm-modal__navbtn rm-modal__navbtn--prev" type="button" id="rm-prev">
          <small>Previous</small><strong></strong>
        </button>
        <button class="rm-modal__navbtn rm-modal__navbtn--next" type="button" id="rm-next">
          <small>Next</small><strong></strong>
        </button>
      </div>
    </div>
  </div>

</div>


<script>
(function () {
  'use strict';

  var root     = document.getElementById('research-mosaic');
  var grid     = document.getElementById('rm-grid');
  var projects = Array.prototype.slice.call(root.querySelectorAll('.rm-project'));
  var modal    = document.getElementById('rm-modal');
  var panel    = modal.querySelector('.rm-modal__panel');
  var content  = document.getElementById('rm-modal-content');
  var prevBtn  = document.getElementById('rm-prev');
  var nextBtn  = document.getElementById('rm-next');
  var closeEls = modal.querySelectorAll('[data-rm-close]');

  var current   = -1;   // index of the open project
  var lastFocus = null; // element to return focus to on close
  var tiles     = [];   // one tile per image, in order

  // Repeating size pattern that packs into a full mosaic (works for 4, 3 and 2 columns)
  var sizePattern = ['big', '', 'tall', 'wide', '', '', 'wide', 'tall', ''];

  // ---------- Build the mosaic ----------
  var tileIndex = 0;
  projects.forEach(function (project, pIndex) {
    var title  = project.querySelector('h2').textContent.trim();
    var accent = project.getAttribute('data-accent') || '#cccccc';

    Array.prototype.forEach.call(project.querySelectorAll('img'), function (img) {
      var tile = document.createElement('button');
      tile.type = 'button';
      tile.className = 'rm-tile';
      var size = sizePattern[tileIndex % sizePattern.length];
      if (size) { tile.classList.add('rm-tile--' + size); }
      tile.style.setProperty('--accent', accent);
      tile.setAttribute('aria-label', title);
      tile.setAttribute('data-project', String(pIndex));

      var thumb = document.createElement('img');
      thumb.src = img.getAttribute('src');
      thumb.alt = img.getAttribute('alt') || '';
      thumb.loading = 'lazy';
      thumb.decoding = 'async';

      var label = document.createElement('span');
      label.className = 'rm-tile__label';
      label.textContent = title;

      tile.appendChild(thumb);
      tile.appendChild(label);
      tile.addEventListener('click', function () {
        lastFocus = tile;
        openProject(pIndex);
      });

      grid.appendChild(tile);
      tiles.push(tile);
      tileIndex += 1;
    });
  });

  // ---------- Pop-up ----------
  function openProject(index) {
    current = (index + projects.length) % projects.length;
    var project = projects[current];

    panel.style.setProperty('--accent', project.getAttribute('data-accent') || '#cccccc');
    panel.style.setProperty('--rm-tint', project.getAttribute('data-tint') || '#ffffff');

    // Show the project exactly as written in its <article>
    content.innerHTML = project.innerHTML;
    var heading = content.querySelector('h2');
    if (heading) { heading.id = 'rm-modal-title'; }

    var prev = projects[(current - 1 + projects.length) % projects.length];
    var next = projects[(current + 1) % projects.length];
    prevBtn.querySelector('strong').textContent = prev.querySelector('h2').textContent.trim();
    nextBtn.querySelector('strong').textContent = next.querySelector('h2').textContent.trim();

    if (modal.hidden) {
      modal.hidden = false;
      document.body.style.overflow = 'hidden';
      document.addEventListener('keydown', onKeyDown);
    }
    panel.scrollTop = 0;
    panel.focus({ preventScroll: true });

    if (project.id && window.history && history.replaceState) {
      history.replaceState(null, '', '#' + project.id);
    }
  }

  function closeModal() {
    if (modal.hidden) { return; }
    modal.hidden = true;
    document.body.style.overflow = '';
    document.removeEventListener('keydown', onKeyDown);
    content.innerHTML = '';
    current = -1;
    if (window.history && history.replaceState) {
      history.replaceState(null, '', window.location.pathname + window.location.search);
    }
    if (lastFocus) { lastFocus.focus(); lastFocus = null; }
  }

  function onKeyDown(e) {
    if (e.key === 'Escape') { e.preventDefault(); closeModal(); return; }
    if (e.key === 'ArrowRight') { e.preventDefault(); openProject(current + 1); return; }
    if (e.key === 'ArrowLeft')  { e.preventDefault(); openProject(current - 1); return; }
    if (e.key === 'Tab') { trapFocus(e); }
  }

  // Keep keyboard focus inside the pop-up while it is open
  function trapFocus(e) {
    var focusable = panel.querySelectorAll('a[href], button:not([disabled]), [tabindex]:not([tabindex="-1"])');
    if (!focusable.length) { return; }
    var first = focusable[0];
    var last  = focusable[focusable.length - 1];
    if (e.shiftKey && (document.activeElement === first || document.activeElement === panel)) {
      e.preventDefault(); last.focus();
    } else if (!e.shiftKey && document.activeElement === last) {
      e.preventDefault(); first.focus();
    }
  }

  Array.prototype.forEach.call(closeEls, function (el) {
    el.addEventListener('click', closeModal);
  });
  prevBtn.addEventListener('click', function () { openProject(current - 1); });
  nextBtn.addEventListener('click', function () { openProject(current + 1); });

  // Deep links: /research/#gaia17bpp-and-other-disk-eclipses opens that pop-up directly
  function openFromHash() {
    var id = window.location.hash.replace('#', '');
    if (!id) { return; }
    for (var i = 0; i < projects.length; i++) {
      if (projects[i].id === id) {
        var firstTile = grid.querySelector('.rm-tile[data-project="' + i + '"]');
        lastFocus = firstTile;
        openProject(i);
        return;
      }
    }
  }
  openFromHash();
  window.addEventListener('hashchange', openFromHash);
})();
</script>