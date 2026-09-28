---
layout: page
permalink: /Outreach/
title: Outreach
nav: true
nav_order: 5
---

<script>document.documentElement.classList.add('om-js');</script>

<style>
  /* ===== Outreach grid — everything is scoped under #outreach-mosaic ===== */
  #outreach-mosaic {
    --om-accent: var(--global-theme-color, #3b6ea5);
    --om-border: var(--global-divider-color, #e3e3e3);
    --om-card:   var(--global-card-bg-color, #ffffff);
    --om-text:   var(--global-text-color, #222222);
    --om-muted:  var(--global-text-color-light, #6f6f6f);
    --om-bed:    #12151c;   /* dark bed behind each cover image */
    --om-radius: 12px;
    --om-gap:    18px;
  }

  #outreach-mosaic .om-hint {
    margin: 0 0 1.1rem;
    font-size: 0.95em;
    color: var(--om-muted);
  }

  /* ---- 2 x 3 grid of equal panels ---- */
  #outreach-mosaic .om-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: var(--om-gap);
    margin-bottom: 2rem;
  }
  @media (max-width: 560px) {
    #outreach-mosaic { --om-gap: 14px; }
    #outreach-mosaic .om-grid { grid-template-columns: 1fr; }
  }

  #outreach-mosaic .om-tile {
    display: flex;
    flex-direction: column;
    width: 100%;
    margin: 0;
    padding: 0;
    overflow: hidden;
    border: 1px solid var(--om-border);
    border-radius: var(--om-radius);
    background: var(--om-card);
    color: var(--om-text);
    font: inherit;
    text-align: left;
    cursor: pointer;
    transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
  }
  #outreach-mosaic .om-tile:hover {
    transform: translateY(-2px);
    border-color: var(--om-accent);
    box-shadow: 0 14px 34px rgba(0, 0, 0, 0.12);
  }
  #outreach-mosaic .om-tile:focus-visible {
    outline: 2px solid var(--om-accent);
    outline-offset: 3px;
  }
  #outreach-mosaic .om-tile__media {
    aspect-ratio: 3 / 2;
    overflow: hidden;
    background: var(--om-bed);
  }
  #outreach-mosaic .om-tile__media img {
    display: block;
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
    transition: transform 0.45s ease;
  }
  #outreach-mosaic .om-tile:hover .om-tile__media img { transform: scale(1.04); }
  #outreach-mosaic .om-tile__text {
    padding: 14px 16px 15px;
    border-top: 1px solid var(--om-border);
  }
  #outreach-mosaic .om-tile__title {
    margin: 0;
    font-size: 1.08em;
    font-weight: 600;
    line-height: 1.3;
    color: var(--om-text);
  }
  #outreach-mosaic .om-tile__sub {
    margin: 4px 0 0;
    font-size: 0.86em;
    line-height: 1.35;
    color: var(--om-muted);
  }

  /* ---- Project source blocks (hidden once JS builds the grid; plain boxes without JS) ---- */
  html.om-js #outreach-mosaic .om-projects { display: none; }
  #outreach-mosaic .om-project {
    border: 1px solid var(--om-border);
    border-radius: var(--om-radius);
    background: var(--om-card);
    padding: 22px 24px;
    margin-bottom: 24px;
  }

  /* Shared content styling (no-JS fallback and inside the pop-up) */
  #outreach-mosaic .om-project h2,
  #outreach-mosaic .om-modal__content h2 {
    margin: 0;
    font-size: 1.65em;
    line-height: 1.15;
    color: var(--om-text);
  }
  #outreach-mosaic .om-sub {
    margin: 6px 0 0;
    padding-bottom: 14px;
    border-bottom: 1px solid var(--om-border);
    font-size: 0.98em;
    color: var(--om-muted);
  }
  #outreach-mosaic .om-body { margin-top: 16px; }
  #outreach-mosaic .om-body p { margin: 0 0 1rem; }
  #outreach-mosaic .om-body p:last-child { margin-bottom: 1.25rem; }
  #outreach-mosaic .om-figrow {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-bottom: 1.1rem;
  }
  #outreach-mosaic .om-figrow + .om-caption { margin-top: -0.5rem; }
  #outreach-mosaic .om-fig { margin: 0 0 1.1rem; }
  #outreach-mosaic .om-figrow .om-fig { margin: 0; }
  #outreach-mosaic .om-figrow a { display: block; }
  #outreach-mosaic .om-fig img,
  #outreach-mosaic .om-figrow img {
    display: block;
    width: 100%;
    border-radius: 8px;
  }
  #outreach-mosaic .om-fig figcaption,
  #outreach-mosaic .om-caption {
    margin: 0.6rem 0 1.1rem;
    text-align: center;
    font-style: italic;
    font-size: 0.95em;
    color: var(--om-muted);
  }
  #outreach-mosaic .om-caption:empty { display: none; }
  @media (max-width: 600px) {
    #outreach-mosaic .om-figrow { grid-template-columns: 1fr; }
  }

  /* ---- Pop-up ---- */
  #outreach-mosaic .om-modal {
    position: fixed;
    inset: 0;
    z-index: 9999;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px;
  }
  #outreach-mosaic .om-modal[hidden] { display: none; }
  #outreach-mosaic .om-modal__backdrop {
    position: absolute;
    inset: 0;
    background: rgba(8, 10, 14, 0.66);
    -webkit-backdrop-filter: blur(5px);
    backdrop-filter: blur(5px);
    animation: om-fade 0.2s ease-out;
  }
  #outreach-mosaic .om-modal__panel {
    position: relative;
    width: min(900px, 100%);
    max-height: calc(100vh - 40px);
    max-height: calc(100dvh - 40px);
    overflow-y: auto;
    border: 1px solid var(--om-border);
    border-radius: 14px;
    background: var(--om-card);
    color: var(--om-text);
    padding: 28px 30px 20px;
    box-shadow: 0 30px 80px rgba(0, 0, 0, 0.4);
    animation: om-pop 0.22s ease-out;
  }
  #outreach-mosaic .om-modal__close {
    position: absolute;
    top: 14px; right: 14px;
    width: 36px; height: 36px;
    padding: 0;
    border: 1px solid var(--om-border);
    border-radius: 50%;
    background: var(--om-card);
    color: var(--om-muted);
    font-size: 1.3em;
    line-height: 1;
    display: grid;
    place-items: center;
    cursor: pointer;
    transition: background 0.15s ease, color 0.15s ease, border-color 0.15s ease;
  }
  #outreach-mosaic .om-modal__close:hover,
  #outreach-mosaic .om-modal__close:focus-visible {
    background: var(--om-accent);
    border-color: var(--om-accent);
    color: #fff;
    outline: none;
  }
  #outreach-mosaic .om-modal__content h2 { padding-right: 44px; }

  #outreach-mosaic .om-modal__nav {
    display: flex;
    justify-content: space-between;
    gap: 12px;
    margin-top: 0.25rem;
    padding-top: 14px;
    border-top: 1px solid var(--om-border);
  }
  #outreach-mosaic .om-modal__navbtn {
    flex: 1 1 0;
    max-width: 48%;
    padding: 8px 10px;
    border: 0;
    border-radius: 8px;
    background: transparent;
    color: var(--om-text);
    font: inherit;
    text-align: left;
    cursor: pointer;
    transition: background 0.15s ease;
  }
  #outreach-mosaic .om-modal__navbtn--next { text-align: right; }
  #outreach-mosaic .om-modal__navbtn small {
    display: block;
    font-size: 0.8em;
    color: var(--om-muted);
  }
  #outreach-mosaic .om-modal__navbtn strong { font-weight: 600; }
  #outreach-mosaic .om-modal__navbtn:hover,
  #outreach-mosaic .om-modal__navbtn:focus-visible {
    background: color-mix(in srgb, var(--om-accent) 12%, transparent);
    outline: none;
  }

  @keyframes om-fade { from { opacity: 0; } to { opacity: 1; } }
  @keyframes om-pop  { from { opacity: 0; transform: translateY(10px) scale(0.985); } to { opacity: 1; transform: none; } }
  @media (prefers-reduced-motion: reduce) {
    #outreach-mosaic * { animation: none !important; transition: none !important; }
  }
</style>


<div id="outreach-mosaic">

  <!-- The 2 x 3 grid is built here by the script below, one panel per project -->
  <div class="om-grid" id="om-grid" aria-label="Outreach activities"></div>

  <!-- ===================================================================
       PROJECT CONTENT
       Each <article> is one outreach area. data-cover is the image shown
       on its panel; the whole article is shown in the pop-up.
       To add a project: copy an <article>, set id, data-cover, the text
       and the images. Nothing else needs editing.
       =================================================================== -->
  <section class="om-projects" id="om-projects">
    <article class="om-project" id="uw-planetarium" data-cover="/images/uw-planetarium-img.png">
      <h2>UW Planetarium</h2>
      <p class="om-sub">Director and Program Coordinator</p>
      <div class="om-body">
        <p>The University of Washington (UW) Planetarium serves as a platform to train the next generation of science communicators, bridging the gap between academic research and public engagement. With state-of-the-art projectors and astronomical software (WorldWide Telescope) our planetarium offers free planetarium experiences to the greater Seattle community. Each year, 30-40 dedicated astronomy undergraduate and graduate volunteers, alongside local amateur astronomy enthusiasts, present over 300 free shows to inspire the next generation of young students. Since 2022, I have been proud to serve as the program director and coordinator, working alognside with astronomy students, fostering partnerships with other UW departments and promoting astronomy education, science literacy, wellness programs centered around climate advocacy, mental health, and space policy.</p>
        <p>Learn more about our planetarium <a href="https://astro.washington.edu/uw-planetarium">here</a>.</p>
      </div>
      <figure class="om-fig">
        <img src="/images/uw-planetarium-img.png" alt="UW-planetarium" />
      </figure>
    </article>

    <article class="om-project" id="in-the-media" data-cover="/images/AndyinNews.jpg">
      <h2>In the Media</h2>
      <p class="om-sub">KING 5, KUOW / NPR, and the SETI Institute</p>
      <div class="om-body">
        <p>Sharing astronomy beyond the university is one of the most rewarding parts of my work, and I am always glad to talk about it wherever the conversation happens. I have appeared on KING 5 News in Seattle to bring astronomy to a local television audience, been featured on <a href="https://www.npr.org/podcasts/fis-1269164192/pocket-science">Pocket Science</a>, the KUOW (Seattle's NPR station) podcast that visits scientists around the region to ask what they are working on, and joined the SETI Institute's weekly livestream, <a href="https://www.youtube.com/watch?v=eW0dJu8xv1E">SETI Live</a>, to discuss my research with a global audience.</p>
      </div>
      <div class="om-figrow">
        <figure class="om-fig">
          <img src="/images/AndyinNews.jpg" alt="Andy on KING 5 News" />
          <figcaption>On KING 5 News.</figcaption>
        </figure>
        <figure class="om-fig">
          <a href="https://www.youtube.com/watch?v=eW0dJu8xv1E" target="_blank" rel="noopener">
            <img src="https://img.youtube.com/vi/eW0dJu8xv1E/0.jpg" alt="SETI Live episode on YouTube" />
          </a>
          <figcaption>On SETI Live, the SETI Institute's weekly livestream.</figcaption>
        </figure>
      </div>
    </article>

    <article class="om-project" id="public-talks-and-demonstrations" data-cover="/images/AndyAoTTalk.png">
      <h2>Public Talks and Demonstrations</h2>
      <p class="om-sub">Astronomy on Tap and hands-on science</p>
      <div class="om-body">
        <p>I regularly give public talks on the science of stars, planets, and the surveys that watch the night sky, including at Astronomy on Tap, where astronomers share their research over a drink in a relaxed setting. Wherever possible, I bring the science into the room with hands-on demonstrations, because there is no substitute for seeing an idea in action. Even my Ph.D. defense included a live liquid nitrogen demonstration for the audience.</p>
      </div>
      <div class="om-figrow">
        <figure class="om-fig">
          <img src="/images/AndyAoTTalk.png" alt="Andy giving an Astronomy on Tap talk" />
          <figcaption>My most recent Astronomy on Tap talk.</figcaption>
        </figure>
        <figure class="om-fig">
          <img src="/images/Andy_LN2%20(2).gif" alt="Liquid nitrogen demonstration during the Ph.D. defense" />
          <figcaption>Hands-on liquid nitrogen demonstration during my Ph.D. defense.</figcaption>
        </figure>
      </div>
    </article>

    <article class="om-project" id="science-communication" data-cover="/images/mqdefault_6s.webp">
      <h2>Science Communication and Outreach</h2>
      <p class="om-sub">Video and social media</p>
      <div class="om-body">
        <p>Engaging the public with science is a vital part of my work. Through various platforms, including YouTube, I strive to make complex astronomical concepts accessible and exciting for all. Below is a recent video discussing astronomical discoveries and their impact on our understanding of the universe.</p>
      </div>
      <div class="om-figrow">
        <a href="https://www.youtube.com/watch?v=smCAEWqOffE&amp;t=2282s" target="_blank" rel="noopener">
          <img src="https://img.youtube.com/vi/smCAEWqOffE/0.jpg" alt="Science Communication Video" />
        </a>
        <img src="/images/mqdefault_6s.webp" alt="Animation from one of my YouTube videos about stars" />
        <img src="/images/outreach1.jpg" alt="Outreach photo" />
        <img src="/images/outreach2.jpg" alt="Outreach photo" />
        <img src="/images/andy-dirac.jpeg" alt="Outreach photo" />
      </div>
    </article>

    <article class="om-project" id="starbites-radio" data-cover="/images/StarBites_Team.png">
      <h2>StarBites Radio</h2>
      <p class="om-sub">A student-run astrophysics podcast</p>
      <div class="om-body">
        <p>StarBites Radio is a podcast I founded to unite students passionate about astrophysics. StarBites Radio was created to provide a platform for undergraduate astronomy students to come together and practice their science communication skills with an emphasis on the historical aspect of astronomy. We've launched two seasons covering topics from general relativity to women in astronomy. Join our community and listen to our episodes <a href="https://anchor.fm/starbites-radio">here</a> and follow us on <a href="https://www.instagram.com/starbitesradio/">Instagram</a>.</p>
      </div>
      <div class="om-figrow">
        <img src="/images/IMG_6397.jpg" alt="" />
        <img src="/images/sb_18.jpg" alt="" />
        <img src="/images/nasa_starbites.jpg" alt="" />
        <img src="/images/StarBites_Team.png" alt="" />
      </div>
    </article>

    <article class="om-project" id="local-hackathons" data-cover="/images/gaia-hackathon24.png">
      <h2>Local Hackathons</h2>
      <p class="om-sub">Coding, data science, and the Gaia Data Sprint</p>
      <div class="om-body">
        <p>Throughout my undergraduate and graduate career, I have had the wonderful opportunity to organize several local astronomy hackathons. These events have allowed students to engage with  hands-on programming experiences, data science, and research in astronomy in a collaborative and fun environment. From early hackathons where participants explored coding and data visualization, to more specialized events like the Gaia Data Sprint at the University of Washington, each experience has emphasized innovation and community.</p>
      </div>
      <div class="om-figrow">
        <img src="/images/coding_blueshift.jpeg" alt="" />
        <img src="/images/gaia-hackathon24.png" alt="" />
      </div>
    </article>

  </section>

  <!-- ===== Pop-up (filled in by the script) ===== -->
  <div class="om-modal" id="om-modal" hidden role="dialog" aria-modal="true" aria-labelledby="om-modal-title">
    <div class="om-modal__backdrop" data-om-close></div>
    <div class="om-modal__panel" tabindex="-1">
      <button class="om-modal__close" type="button" data-om-close aria-label="Close">&times;</button>
      <div class="om-modal__content" id="om-modal-content"></div>
      <div class="om-modal__nav">
        <button class="om-modal__navbtn om-modal__navbtn--prev" type="button" id="om-prev">
          <small>Previous</small><strong></strong>
        </button>
        <button class="om-modal__navbtn om-modal__navbtn--next" type="button" id="om-next">
          <small>Next</small><strong></strong>
        </button>
      </div>
    </div>
  </div>

</div>


<script>
(function () {
  'use strict';

  var root     = document.getElementById('outreach-mosaic');
  var grid     = document.getElementById('om-grid');
  var projects = Array.prototype.slice.call(root.querySelectorAll('.om-project'));
  var modal    = document.getElementById('om-modal');
  var panel    = modal.querySelector('.om-modal__panel');
  var content  = document.getElementById('om-modal-content');
  var prevBtn  = document.getElementById('om-prev');
  var nextBtn  = document.getElementById('om-next');
  var closeEls = modal.querySelectorAll('[data-om-close]');

  var current   = -1;   // index of the open project
  var lastFocus = null; // element to return focus to on close

  function titleOf(project) {
    return project.querySelector('h2').textContent.trim();
  }

  // ---------- Build the grid: one panel per project ----------
  projects.forEach(function (project, index) {
    var title    = titleOf(project);
    var subEl    = project.querySelector('.om-sub');
    var subtitle = subEl ? subEl.textContent.trim() : '';
    var firstImg = project.querySelector('img');
    var cover    = project.getAttribute('data-cover') || (firstImg ? firstImg.getAttribute('src') : '');
    var coverAlt = '';
    Array.prototype.forEach.call(project.querySelectorAll('img'), function (img) {
      if (img.getAttribute('src') === cover) { coverAlt = img.getAttribute('alt') || ''; }
    });

    var tile = document.createElement('button');
    tile.type = 'button';
    tile.className = 'om-tile';
    tile.setAttribute('data-project', String(index));
    tile.setAttribute('aria-label', 'Read about ' + title);

    var media = document.createElement('div');
    media.className = 'om-tile__media';
    var img = document.createElement('img');
    img.src = cover;
    img.alt = coverAlt;
    img.loading = 'lazy';
    img.decoding = 'async';
    media.appendChild(img);

    var text = document.createElement('div');
    text.className = 'om-tile__text';
    var h = document.createElement('p');
    h.className = 'om-tile__title';
    h.textContent = title;
    text.appendChild(h);
    if (subtitle) {
      var s = document.createElement('p');
      s.className = 'om-tile__sub';
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
    if (heading) { heading.id = 'om-modal-title'; }

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

  // Deep links: /Outreach/#starbites-radio opens that pop-up directly
  function openFromHash() {
    var id = window.location.hash.replace('#', '');
    if (!id) { return; }
    for (var i = 0; i < projects.length; i++) {
      if (projects[i].id === id) {
        lastFocus = grid.querySelector('.om-tile[data-project="' + i + '"]');
        openProject(i);
        return;
      }
    }
  }
  openFromHash();
  window.addEventListener('hashchange', openFromHash);
})();
</script>