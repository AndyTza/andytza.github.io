---
layout: page
permalink: /astr270-blog/
title: ASTR 270 Blog
nav: false
nav_order: 7
---
<style>
.blog-container {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.blog-card {
  border: 1px solid #ccc;
  border-radius: 10px;
  padding: 1rem;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 1rem;
  background: #f9f9f9;
  transition: box-shadow 0.2s ease;
  cursor: pointer;
}

.blog-card:hover {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}

.blog-image {
  width: 100px;
  height: 100px;
  border-radius: 8px;
  object-fit: cover;
}

.blog-preview {
  flex-grow: 1;
}

.blog-title {
  font-size: 1.2rem;
  font-weight: bold;
  margin-bottom: 0.3rem;
}

.blog-description {
  font-size: 0.95rem;
  color: #555;
}

.blog-article {
  display: none;
  padding: 1rem;
  border-left: 4px solid #007acc;
  background: #fcfcfc;
  margin-top: -1rem;
  margin-bottom: 2rem;
}
</style>


Welcome to the ASTR 270 Blog! Dive into explainers, course insights, and stories from the stars.

---

<div class="blog-container">

<!-- BLOG CARD 1 -->
<div class="blog-card" onclick="toggleBlog('article1')">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Light_curve_of_a_supernova.svg/1024px-Light_curve_of_a_supernova.svg.png" class="blog-image" alt="Light curve">
  <div class="blog-preview">
    <div class="blog-title">Tile</div>
    <div class="blog-description">A star’s diary, hidden in its light over time. Learn how we decode it in ASTR 270.</div>
  </div>
</div>
<div id="article1" class="blog-article">

## Title

Light curves are more than just squiggly lines on a graph — they’re a star’s diary. In ASTR 270, we’ll use light curves to decode stellar rotation, eclipses, transits, and more.Light curves are more than just squiggly lines on a graph — they’re a star’s diary. In ASTR 270, we’ll use light curves to decode stellar rotation, eclipses, transits, and more.Light curves are more than just squiggly lines on a graph — they’re a star’s diary. In ASTR 270, we’ll use light curves to decode stellar rotation, eclipses, transits, and more.Light curves are more than just squiggly lines on a graph — they’re a star’s diary. In ASTR 270, we’ll use light curves to decode stellar rotation, eclipses, transits, and more.

</div>

<!-- BLOG CARD 2 -->
<div class="blog-card" onclick="toggleBlog('article2')">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/DigitalSky2.jpg/800px-DigitalSky2.jpg" class="blog-image" alt="Planetarium">
  <div class="blog-preview">
    <div class="blog-title">🌌 Simulating the Sky in the Planetarium</div>
    <div class="blog-description">How we bring the cosmos indoors — with digital stars, scripts, and science.</div>
  </div>
</div>
<div id="article2" class="blog-article">

## 🌌 How We Simulate the Night Sky in the Planetarium

Ever wonder how we recreate the Milky Way overhead in the UW dome?

The system uses:
- A digital star catalog synced with time and location
- Dome projection and fisheye lenses
- A scripting engine for animations and narratives

This means we can *literally* fast forward 10,000 years or pause to highlight a meteor shower. It's a powerful tool for storytelling and scientific outreach.

</div>

<!-- BLOG CARD 3 -->
<div class="blog-card" onclick="toggleBlog('article3')">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Moon_and_Apollo_11_Lunar_Module.jpg/640px-Moon_and_Apollo_11_Lunar_Module.jpg" class="blog-image" alt="Astronomy myths">
  <div class="blog-preview">
    <div class="blog-title">🛸 Top Astronomy Misconceptions</div>
    <div class="blog-description">From black holes to the Moon’s "dark side", let’s bust a few cosmic myths.</div>
  </div>
</div>
<div id="article3" class="blog-article">

## 🛸 My Favorite Misconceptions in Astronomy

Let’s bust some myths:

- **The Moon has a dark side.** Nope — it’s *tidally locked*, not half-invisible.
- **Winter is colder because we’re farther from the Sun.** Actually, Earth is closest to the Sun in January.
- **Black holes suck everything in.** Only if you get too close — gravity still follows the rules!

Got a favorite myth? Send it my way!

</div>

</div>

<script>
function toggleBlog(id) {
  const all = document.querySelectorAll('.blog-article');
  all.forEach(el => {
    if (el.id !== id) el.style.display = 'none';
  });
  const selected = document.getElementById(id);
  selected.style.display = selected.style.display === 'block' ? 'none' : 'block';
  selected.scrollIntoView({ behavior: 'smooth', block: 'start' });
}
</script>
