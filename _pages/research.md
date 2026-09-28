---
layout: page
permalink: /research/
title: Research
nav: true
nav_order: 1
---

<script>document.documentElement.classList.add('rm-js');</script>

<style>
  /* ===== Research grid — everything is scoped under #research-mosaic ===== */
  #research-mosaic {
    --rm-accent: var(--global-theme-color, #3b6ea5);
    --rm-border: var(--global-divider-color, #e3e3e3);
    --rm-card:   var(--global-card-bg-color, #ffffff);
    --rm-text:   var(--global-text-color, #222222);
    --rm-muted:  var(--global-text-color-light, #6f6f6f);
    --rm-bed:    #12151c;   /* dark bed behind each cover image */
    --rm-radius: 12px;
    --rm-gap:    18px;
  }

  #research-mosaic .rm-hint {
    margin: 0 0 1.1rem;
    font-size: 0.95em;
    color: var(--rm-muted);
  }

  /* ---- 2 x 3 grid of equal panels ---- */
  #research-mosaic .rm-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: var(--rm-gap);
    margin-bottom: 2rem;
  }
  @media (max-width: 560px) {
    #research-mosaic { --rm-gap: 14px; }
    #research-mosaic .rm-grid { grid-template-columns: 1fr; }
  }

  #research-mosaic .rm-tile {
    display: flex;
    flex-direction: column;
    width: 100%;
    margin: 0;
    padding: 0;
    overflow: hidden;
    border: 1px solid var(--rm-border);
    border-radius: var(--rm-radius);
    background: var(--rm-card);
    color: var(--rm-text);
    font: inherit;
    text-align: left;
    cursor: pointer;
    transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
  }
  #research-mosaic .rm-tile:hover {
    transform: translateY(-2px);
    border-color: var(--rm-accent);
    box-shadow: 0 14px 34px rgba(0, 0, 0, 0.12);
  }
  #research-mosaic .rm-tile:focus-visible {
    outline: 2px solid var(--rm-accent);
    outline-offset: 3px;
  }
  #research-mosaic .rm-tile__media {
    aspect-ratio: 3 / 2;
    overflow: hidden;
    background: var(--rm-bed);
  }
  #research-mosaic .rm-tile__media img {
    display: block;
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
    transition: transform 0.45s ease;
  }
  #research-mosaic .rm-tile:hover .rm-tile__media img { transform: scale(1.04); }
  #research-mosaic .rm-tile__text {
    padding: 14px 16px 15px;
    border-top: 1px solid var(--rm-border);
  }
  #research-mosaic .rm-tile__title {
    margin: 0;
    font-size: 1.08em;
    font-weight: 600;
    line-height: 1.3;
    color: var(--rm-text);
  }
  #research-mosaic .rm-tile__sub {
    margin: 4px 0 0;
    font-size: 0.86em;
    line-height: 1.35;
    color: var(--rm-muted);
  }

  /* ---- Project source blocks (hidden once JS builds the grid; plain boxes without JS) ---- */
  html.rm-js #research-mosaic .rm-projects { display: none; }
  #research-mosaic .rm-project {
    border: 1px solid var(--rm-border);
    border-radius: var(--rm-radius);
    background: var(--rm-card);
    padding: 22px 24px;
    margin-bottom: 24px;
  }

  /* Shared content styling (no-JS fallback and inside the pop-up) */
  #research-mosaic .rm-project h2,
  #research-mosaic .rm-modal__content h2 {
    margin: 0;
    font-size: 1.65em;
    line-height: 1.15;
    color: var(--rm-text);
  }
  #research-mosaic .rm-sub {
    margin: 6px 0 0;
    padding-bottom: 14px;
    border-bottom: 1px solid var(--rm-border);
    font-size: 0.98em;
    color: var(--rm-muted);
  }
  #research-mosaic .rm-body { margin-top: 16px; }
  #research-mosaic .rm-body p { margin: 0 0 1rem; }
  #research-mosaic .rm-body p:last-child { margin-bottom: 1.25rem; }
  #research-mosaic .rm-figrow {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
  }
  #research-mosaic .rm-fig { margin: 0 0 1.1rem; }
  #research-mosaic .rm-fig img,
  #research-mosaic .rm-figrow img {
    display: block;
    width: 100%;
    border-radius: 8px;
  }
  #research-mosaic .rm-fig figcaption,
  #research-mosaic .rm-caption {
    margin: 0.6rem 0 0;
    text-align: center;
    font-style: italic;
    font-size: 0.95em;
    color: var(--rm-muted);
  }
  #research-mosaic .rm-caption:empty { display: none; }
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
    background: rgba(8, 10, 14, 0.66);
    -webkit-backdrop-filter: blur(5px);
    backdrop-filter: blur(5px);
    animation: rm-fade 0.2s ease-out;
  }
  #research-mosaic .rm-modal__panel {
    position: relative;
    width: min(900px, 100%);
    max-height: calc(100vh - 40px);
    max-height: calc(100dvh - 40px);
    overflow-y: auto;
    border: 1px solid var(--rm-border);
    border-radius: 14px;
    background: var(--rm-card);
    color: var(--rm-text);
    padding: 28px 30px 20px;
    box-shadow: 0 30px 80px rgba(0, 0, 0, 0.4);
    animation: rm-pop 0.22s ease-out;
  }
  #research-mosaic .rm-modal__close {
    position: absolute;
    top: 14px; right: 14px;
    width: 36px; height: 36px;
    padding: 0;
    border: 1px solid var(--rm-border);
    border-radius: 50%;
    background: var(--rm-card);
    color: var(--rm-muted);
    font-size: 1.3em;
    line-height: 1;
    display: grid;
    place-items: center;
    cursor: pointer;
    transition: background 0.15s ease, color 0.15s ease, border-color 0.15s ease;
  }
  #research-mosaic .rm-modal__close:hover,
  #research-mosaic .rm-modal__close:focus-visible {
    background: var(--rm-accent);
    border-color: var(--rm-accent);
    color: #fff;
    outline: none;
  }
  #research-mosaic .rm-modal__content h2 { padding-right: 44px; }

  #research-mosaic .rm-modal__nav {
    display: flex;
    justify-content: space-between;
    gap: 12px;
    margin-top: 0.25rem;
    padding-top: 14px;
    border-top: 1px solid var(--rm-border);
  }
  #research-mosaic .rm-modal__navbtn {
    flex: 1 1 0;
    max-width: 48%;
    padding: 8px 10px;
    border: 0;
    border-radius: 8px;
    background: transparent;
    color: var(--rm-text);
    font: inherit;
    text-align: left;
    cursor: pointer;
    transition: background 0.15s ease;
  }
  #research-mosaic .rm-modal__navbtn--next { text-align: right; }
  #research-mosaic .rm-modal__navbtn small {
    display: block;
    font-size: 0.8em;
    color: var(--rm-muted);
  }
  #research-mosaic .rm-modal__navbtn strong { font-weight: 600; }
  #research-mosaic .rm-modal__navbtn:hover,
  #research-mosaic .rm-modal__navbtn:focus-visible {
    background: color-mix(in srgb, var(--rm-accent) 12%, transparent);
    outline: none;
  }

  @keyframes rm-fade { from { opacity: 0; } to { opacity: 1; } }
  @keyframes rm-pop  { from { opacity: 0; transform: translateY(10px) scale(0.985); } to { opacity: 1; transform: none; } }
  @media (prefers-reduced-motion: reduce) {
    #research-mosaic * { animation: none !important; transition: none !important; }
  }
</style>


<div id="research-mosaic">

  <!-- The 2 x 3 grid is built here by the script below, one panel per project -->
  <div class="rm-grid" id="rm-grid" aria-label="Research areas"></div>

  <!-- ===================================================================
       PROJECT CONTENT
       Each <article> is one research area. data-cover is the image shown
       on its panel; the whole article is shown in the pop-up.
       To add a project: copy an <article>, set id, data-cover, the text
       and the images. Nothing else needs editing.
       =================================================================== -->
  <section class="rm-projects" id="rm-projects">

    <article class="rm-project" id="giant-impacts" data-cover="/images/gi-sim.gif">
      <h2>Giant Impacts</h2>
      <p class="rm-sub">Catching Planetary Collisions in the Time Domain</p>
      <div class="rm-body">
        <p>Giant impacts, collisions between planet-sized bodies, are thought to shape the final assembly of rocky planets, yet we have almost never caught one in the act. The dust produced in the aftermath of such a collision can briefly veil its host star, producing deep, long-lasting dimming events in the optical and a fresh infrared excess as the debris settles into orbit. Using the Gaia Photometric Science Alerts, I am conducting a systematic search for these giant impact candidates (GICs), which led to the discovery of Gaia-GIC-1 (Tzanidakis &amp; Davenport 2026), a candidate for the dusty aftermath of a recent planetary-scale collision. To connect these observations to physics, I am also developing a reproducible simulation pipeline that follows the collision debris with N-body dynamics and models its dust optics to predict light curves as they would be observed by surveys such as ZTF and NEOWISE. Together, these efforts aim to establish how often giant impacts occur and what they can tell us about the birth of planetary systems.</p>
      </div>
      <figure class="rm-fig">
        <img src="/images/gi-sim.gif" alt="Simulation of the dusty debris produced by a giant impact around a star." />
        <figcaption>Simulation of the debris and dust produced by a giant impact around a Sun-like star.</figcaption>
      </figure>
    </article>

    <article class="rm-project" id="main-sequence-dippers" data-cover="/images/msdip.jpeg">
      <h2>Main-Sequence Dippers</h2>
      <p class="rm-sub">Circumstellar Environments around Dwarf Stars</p>
      <div class="rm-body">
        <p>In 2016, <a href="https://ui.adsabs.harvard.edu/abs/2016MNRAS.457.3988B/abstract">Boyajian et al. (2016)</a> revealed one of the first main-sequence stars with erratic dimming events, stirring discussions and theories on the origins of such rare stars. Only a small number of similar systems have been identified since, leaving many open questions about their origins and if they are connected at all with the initial discovery of the Boyajian star. My Ph.D dissertation work conducts the first ever large-scale systematic search for these irregularly variable dwarf stars, analyzing extensive time-domain data to assess their occurrence and potential origins, such as planetary-scale collisions or Earth-Moon-like formation events. This work also drives the development of scalable tools for examining stellar variability across billions of stars, expanding our ability to probe diverse behavior of stellar variability phenomena.</p>
      </div>
      <div class="rm-figrow">
        <img src="/images/msdip.jpeg" alt="Sky position of main-sequence dipper stars and example of ZTF light curve." />
        <img src="/images/mslc1.png" alt="Disk Eclipse Comparison" />
      </div>
      <p class="rm-caption"></p>
    </article>

    <article class="rm-project" id="disk-eclipses" data-cover="/images/disk-eclipse-comp.png">
      <h2>Disk Eclipses</h2>
      <p class="rm-sub">Gaia17bpp and other Disk Eclipses</p>
      <div class="rm-body">
        <p>We are now at the cusp of probing stellar variability on timescales spanning decades, which opens the door to uncovering new and rare types of variable stars. In my first year of graduate school, I serendipitously discovered <a href="https://andytza.github.io/Gaia17bpp/">Gaia17bpp</a> (<a href="https://iopscience.iop.org/article/10.3847/1538-4357/aceda7">Tzanidakis et al. 2023</a>), a system that we believe could be an extreme analog to the famous <a href="https://arxiv.org/pdf/1004.2464.pdf">Epsilon Aurigae</a> binary, and currently holds the record for the longest duration dimming event we have found. This discovery offers a unique opportunity to study eclipses caused by massive circumstellar disks, pushing the boundaries of our understanding of long-period stellar variables.</p>
      </div>
      <div class="rm-figrow">
        <img src="/images/disk-eclipse-comp.png" alt="Disk Eclipse Comparison" />
        <img src="/images/Gaia17bpp_WISE.gif" alt="Gaia17bpp and WISE Comparison" />
      </div>
      <p class="rm-caption">Left: Light curve mosaic of known Epsilon Aurigae analog systems including Gaia17bpp. Right: Movie from WISE revealing long-term variability.</p>
    </article>

    <article class="rm-project" id="lsst-time-series-features" data-cover="/images/lsst-lc.png">
      <h2>LSST Time Series Features</h2>
      <p class="rm-sub">Time-Series Features in the LSST Era</p>
      <div class="rm-body">
        <p>In the era of large time-domain surveys with gappy, multi-band, and sparse photometric measurements, time series features have become an important tool to search for populations of variable stars and transient phenomena <a href="https://ui.adsabs.harvard.edu/abs/2011ApJ...733...10R/abstract">(Richards et al. 2011)</a>. During my first year of graduate school, I worked with Professor Eric Bellm and the UW Data Management group on transient alert processing. My interests aimed to characterize the recovery of periodic objects in data like the LSST alerts and what are the optimum techniques used to increase the efficiency of finding reliable periods. Some of my work also included characterizing alert light curve time series features and statistical properties of transients and variable stars. Our findings have been reported in the <a href="https://dmtn-221.lsst.io/">LSST Data Management Technotes-221</a>.</p>
      </div>
      <figure class="rm-fig">
        <img src="/images/lsst-lc.png" alt="LSST simulated light curves of RR Lyrae and eclipsing binaries." />
        <figcaption>Synthetic LSST Alert-like photometry of two periodic sources: RR Lyrae and Eclipsing Binaries.</figcaption>
      </figure>
    </article>

    <article class="rm-project" id="ztf-census-of-the-local-universe" data-cover="/images/CLU_snap.png">
      <h2>ZTF Census of the Local Universe (CLU) Experiment</h2>
      <p class="rm-sub">Type-II Supernovae in the Local Universe with the Zwicky Transient Facility</p>
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

    <article class="rm-project" id="milky-way-stellar-disk-substructure" data-cover="/images/sgr-col.gif">
      <h2>Understanding the Milky Way Stellar Disk Substructure</h2>
      <p class="rm-sub">Galactic Archeology: Tomography of the Galactic Disk</p>
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

  function titleOf(project) {
    return project.querySelector('h2').textContent.trim();
  }

  // ---------- Build the grid: one panel per project ----------
  projects.forEach(function (project, index) {
    var title    = titleOf(project);
    var subEl    = project.querySelector('.rm-sub');
    var subtitle = subEl ? subEl.textContent.trim() : '';
    var firstImg = project.querySelector('img');
    var cover    = project.getAttribute('data-cover') || (firstImg ? firstImg.getAttribute('src') : '');
    var coverAlt = '';
    Array.prototype.forEach.call(project.querySelectorAll('img'), function (img) {
      if (img.getAttribute('src') === cover) { coverAlt = img.getAttribute('alt') || ''; }
    });

    var tile = document.createElement('button');
    tile.type = 'button';
    tile.className = 'rm-tile';
    tile.setAttribute('data-project', String(index));
    tile.setAttribute('aria-label', 'Read about ' + title);

    var media = document.createElement('div');
    media.className = 'rm-tile__media';
    var img = document.createElement('img');
    img.src = cover;
    img.alt = coverAlt;
    img.loading = 'lazy';
    img.decoding = 'async';
    media.appendChild(img);

    var text = document.createElement('div');
    text.className = 'rm-tile__text';
    var h = document.createElement('p');
    h.className = 'rm-tile__title';
    h.textContent = title;
    text.appendChild(h);
    if (subtitle) {
      var s = document.createElement('p');
      s.className = 'rm-tile__sub';
      s.textContent = subtitle;
      text.appendChild(s);
    }

    tile.appendChild(media);
    tile.appendChild(text);
    tile.addEventListener('click', function () {
      lastFocus = tile;
      openProject(index);
    });
    grid.appendChild(tile);
  });

  // ---------- Pop-up ----------
  function openProject(index) {
    current = (index + projects.length) % projects.length;
    var project = projects[current];

    // Show the project exactly as written in its <article>
    content.innerHTML = project.innerHTML;
    var heading = content.querySelector('h2');
    if (heading) { heading.id = 'rm-modal-title'; }

    var prev = projects[(current - 1 + projects.length) % projects.length];
    var next = projects[(current + 1) % projects.length];
    prevBtn.querySelector('strong').textContent = titleOf(prev);
    nextBtn.querySelector('strong').textContent = titleOf(next);

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
    if (e.key === 'Escape')     { e.preventDefault(); closeModal(); return; }
    if (e.key === 'ArrowRight') { e.preventDefault(); openProject(current + 1); return; }
    if (e.key === 'ArrowLeft')  { e.preventDefault(); openProject(current - 1); return; }
    if (e.key === 'Tab')        { trapFocus(e); }
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

  // Deep links: /research/#disk-eclipses opens that pop-up directly
  function openFromHash() {
    var id = window.location.hash.replace('#', '');
    if (!id) { return; }
    for (var i = 0; i < projects.length; i++) {
      if (projects[i].id === id) {
        lastFocus = grid.querySelector('.rm-tile[data-project="' + i + '"]');
        openProject(i);
        return;
      }
    }
  }
  openFromHash();
  window.addEventListener('hashchange', openFromHash);
})();
</script>