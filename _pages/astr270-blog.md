---
layout: page
permalink: /astr270-blog/
title: ASTR 270 Blog
nav: false
nav_order: 7
---
<style>
.blog-article h2 {
  font-size: 1.5rem;
  margin-top: 0;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.blog-article h4 {
  margin-top: 1.2rem;
  color: #444;
  font-weight: 600;
  border-bottom: 1px solid #ddd;
  padding-bottom: 0.2rem;
}
.blog-article blockquote {
  border-left: 4px solid #007acc;
  background: #f0f8ff;
  padding: 0.7rem 1rem;
  margin: 1rem 0;
  font-style: italic;
  color: #333;
}
.callout {
  background: #fff8e1;
  border: 1px solid #ffcc80;
  padding: 1rem;
  margin-top: 1.5rem;
  border-radius: 6px;
  font-size: 0.95rem;
}
</style>


Welcome to the ASTR 270 Blog! Dive into explainers, course insights, and stories from the stars.

---
<div class="blog-container">

  <!-- BLOG CARD 1 -->
  <div class="blog-card" onclick="toggleBlog('article1')">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Light_curve_of_a_supernova.svg/1024px-Light_curve_of_a_supernova.svg.png" class="blog-image" alt="Light curve">
    <div class="blog-preview">
      <div class="blog-title">🌀 What Is a Light Curve, Really?</div>
      <div class="blog-description">A star’s diary, hidden in its light over time. Learn how we decode it in ASTR 270.</div>
    </div>
  </div>

  <div id="article1" class="blog-article">
    <h2>🌀 What Is a Light Curve, Really?</h2>
    <h4>✨ A Glimpse Into Stellar Stories</h4>
    <p>Light curves are more than just squiggly lines on a graph — they’re a star’s diary. In ASTR 270, we’ll use light curves to decode stellar rotation, eclipses, transits, and more.</p>

    <blockquote>
      "A light curve is time’s way of whispering a star’s secrets."
    </blockquote>

    <h4>📈 What Can a Light Curve Tell Us?</h4>
    <ul>
      <li><strong>Dips</strong>: Often signal something passing in front of the star, like a planet or dust.</li>
      <li><strong>Peaks</strong>: Might be flares, stellar activity, or even instrumental artifacts.</li>
      <li><strong>Patterns</strong>: Repeating shapes reveal rotation, pulsation, or eclipsing binaries.</li>
    </ul>

    <div class="callout">
      💡 <strong>Takeaway:</strong> Time-series analysis is a powerful tool. Patterns in brightness can reveal planets, binary companions, or dusty disks around stars — and you’ll get to analyze these firsthand!
    </div>

    <h4>🔬 Coming Up in ASTR 270</h4>
    <p>We'll walk through how to build your own light curves using ZTF and Gaia data, model simple eclipses, and learn how to spot real astrophysical signals from noise. You'll also get a taste of how astronomers discover planets using light curves!</p>

    <p><em>Next: stay tuned for a data lab where you’ll generate and interpret your own light curves.</em></p>
  </div>
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
