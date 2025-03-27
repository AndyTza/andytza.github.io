---
layout: page
permalink: /astr270-blog/
title: ASTR 270 Blog
nav: false
nav_order: 7
---

# 🌠 ASTR 270 Blog Hub

Welcome to the ASTR 270 Blog! This is where I’ll post course-related articles, astronomy explainers, behind-the-scenes stories from the UW Planetarium, and helpful TA tips. Click a title below to expand the post.

---

## 📚 Blog Articles

<div id="blog-summaries">
  <ul>
    <li><a href="#" onclick="showArticle('article1'); return false;">🌀 What Is a Light Curve, Really?</a></li>
    <li><a href="#" onclick="showArticle('article2'); return false;">🌌 How We Simulate the Night Sky in the Planetarium</a></li>
    <li><a href="#" onclick="showArticle('article3'); return false;">🛸 My Favorite Misconceptions in Astronomy</a></li>
  </ul>
</div>

---

<div id="blog-articles">

### <div id="article1" style="display:none;">
## 🌀 What Is a Light Curve, Really?

Light curves are more than just squiggly lines on a graph — they’re a star’s diary. In ASTR 270, we’ll use light curves to decode stellar rotation, eclipses, transits, and more.

A few quick takeaways:
- A **dip** usually means something passed in front of the star.
- A **brightening** could be a flare or an instrumental issue.
- Time-series analysis is *everything*.

Stay tuned for a lab where you'll create your own light curve with real data!

[↑ Back to top](#📚-blog-articles)

---

</div>

### <div id="article2" style="display:none;">
## 🌌 How We Simulate the Night Sky in the Planetarium

Ever wonder how we recreate the Milky Way overhead in the UW dome?

The system uses:
- A digital star catalog synced with time and location
- Dome projection and fisheye lenses
- A scripting engine for animations and narratives

This means we can *literally* fast forward 10,000 years or pause to highlight a meteor shower. It's a powerful tool for storytelling and scientific outreach.

[↑ Back to top](#📚-blog-articles)

---

</div>

### <div id="article3" style="display:none;">
## 🛸 My Favorite Misconceptions in Astronomy

Let’s bust some myths:

- **The Moon has a dark side.** Nope — it’s *tidally locked*, not half-invisible.
- **Winter is colder because we’re farther from the Sun.** Actually, Earth is closest to the Sun in January.
- **Black holes suck everything in.** Only if you get too close — gravity still follows the rules!

Got a favorite myth? Send it my way!

[↑ Back to top](#📚-blog-articles)

---

</div>

</div>

<script>
  function showArticle(id) {
    const articles = document.querySelectorAll('#blog-articles > div');
    articles.forEach(article => article.style.display = 'none');
    document.getElementById(id).style.display = 'block';
    window.scrollTo({ top: document.getElementById(id).offsetTop - 60, behavior: 'smooth' });
  }
</script>
