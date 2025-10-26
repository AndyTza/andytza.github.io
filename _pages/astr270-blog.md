---
layout: page
permalink: /astr270-blog/
title: titles.ASTR_270_Blog
nav: false
nav_order: 7
---

<style>
.blog-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  margin-top: 1.5rem;
}

.blog-card {
  background: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 10px;
  overflow: hidden;
  cursor: pointer;
  transition: box-shadow 0.3s ease;
  text-align: center;
  padding: 1rem;
}

.blog-card:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.blog-card img {
  width: 100%;
  max-height: 180px;
  object-fit: cover;
  border-radius: 6px;
}

.blog-card h3 {
  margin-top: 0.8rem;
  font-size: 1.1rem;
  color: #333;
}

.blog-article {
  display: none;
  margin-top: 2rem;
  padding: 1.5rem;
  border-left: 4px solid #007acc;
  background: #fefefe;
  border-radius: 8px;
}

.blog-article h2 {
  margin-top: 0;
  font-size: 1.5rem;
}

.blog-article blockquote {
  border-left: 4px solid #007acc;
  background: #f0f8ff;
  padding: 0.7rem 1rem;
  margin: 1rem 0;
  font-style: italic;
  color: #333;
}
</style>

# 🌠 ASTR 270 Blog Hub

Welcome! Click on any blog card below to explore stories, explainers, and behind-the-scenes content from the TA desk and the UW Planetarium.

---

<div class="blog-grid">

  <div class="blog-card" onclick="showArticle('article1')">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Light_curve_of_a_supernova.svg/1024px-Light_curve_of_a_supernova.svg.png" alt="Light Curve">
    <h3>🌀 What Is a Light Curve, Really?</h3>
  </div>

  <div class="blog-card" onclick="showArticle('article2')">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/DigitalSky2.jpg/800px-DigitalSky2.jpg" alt="Planetarium">
    <h3>🌌 Simulating the Sky in the Planetarium</h3>
  </div>

  <div class="blog-card" onclick="showArticle('article3')">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Moon_and_Apollo_11_Lunar_Module.jpg/640px-Moon_and_Apollo_11_Lunar_Module.jpg" alt="Misconceptions">
    <h3>🛸 Top Astronomy Misconceptions</h3>
  </div>

</div>

<!-- ARTICLES -->
<div id="article1" class="blog-article">
  <h2>🌀 What Is a Light Curve, Really?</h2>
  <p>Light curves are more than just squiggly lines on a graph — they’re a star’s diary. In ASTR 270, we’ll use light curves to decode stellar rotation, eclipses, transits, and more.</p>

  <blockquote>
    "A light curve is time’s way of whispering a star’s secrets."
  </blockquote>

  <ul>
    <li><strong>Dips</strong>: Something passed in front of the star (planet, dust).</li>
    <li><strong>Peaks</strong>: Flares, activity, or noise.</li>
    <li><strong>Patterns</strong>: Reveal rotation or eclipses.</li>
  </ul>

  <p><strong>Coming soon:</strong> You’ll build your own light curve in the lab using real ZTF data.</p>
</div>

<div id="article2" class="blog-article">
  <h2>🌌 Simulating the Sky in the Planetarium</h2>
  <p>Ever wonder how we recreate the Milky Way overhead in the UW dome?</p>

  <ul>
    <li>A digital star catalog synced with time and location</li>
    <li>Fisheye lens dome projection</li>
    <li>Scripting tools for flying through space, time-lapse starscapes, and more</li>
  </ul>

  <p>It’s a storytelling and teaching powerhouse. You’ll get a chance to run the system yourself this quarter!</p>
</div>

<div id="article3" class="blog-article">
  <h2>🛸 Top Astronomy Misconceptions</h2>
  <ul>
    <li><strong>“The Moon has a dark side.”</strong> Nope — it’s tidally locked. We just don’t see the far side.</li>
    <li><strong>“Winter is when Earth is far from the Sun.”</strong> Earth is actually closest to the Sun in January.</li>
    <li><strong>“Black holes suck everything in.”</strong> Not unless you’re close — they obey gravity like everything else.</li>
  </ul>

  <p>Send me your favorite space myths and I’ll feature them in a future post!</p>
</div>

<script>
function showArticle(id) {
  // Hide all articles
  document.querySelectorAll('.blog-article').forEach(el => el.style.display = 'none');
  // Show selected
  const article = document.getElementById(id);
  article.style.display = 'block';
  // Scroll into view
  article.scrollIntoView({ behavior: 'smooth', block: 'start' });
}
</script>
