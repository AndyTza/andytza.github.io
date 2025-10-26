---
layout: about
title: 
permalink: /
subtitle: Astronomy Ph.D. Candidate | Director of UW Planetarium | Science Communicator

profile:
  align: right
  image: atzan_img.jpg
  image_circular: false # crops the image to make it circular
  address: >
    <p>Seattle, WA</p>

news: true  # includes a list of news items
selected_papers: false # includes a list of papers marked as "selected={true}"
social: true  # includes social icons at the bottom of the page
---

<!-- Language Switcher Button -->
<button id="translateBtn" onclick="translateToGreek()" style="position: fixed; top: 10px; right: 10px; z-index: 1000; padding: 8px 16px; background: #4285f4; color: white; border: none; border-radius: 4px; cursor: pointer; font-family: Arial, sans-serif;">
  🇬🇷 Ελληνικά
</button>

<div id="google_translate_element" style="display: none;"></div>

<script type="text/javascript">
function googleTranslateElementInit() {
  new google.translate.TranslateElement({
    pageLanguage: 'en',
    includedLanguages: 'el,en',
    autoDisplay: false
  }, 'google_translate_element');
}

function translateToGreek() {
  var selectField = document.querySelector("select.goog-te-combo");
  if (selectField) {
    if (selectField.value === 'el') {
      selectField.value = 'en';
      document.getElementById('translateBtn').innerHTML = '🇬🇷 Ελληνικά';
    } else {
      selectField.value = 'el';
      document.getElementById('translateBtn').innerHTML = '🇺🇸 English';
    }
    selectField.dispatchEvent(new Event('change'));
  }
}
</script>

<script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>

Hello, I'm Anastasios (Andy) Tzanidakis 👋 

I'm a Ph.D. candidate at the University of Washington and the former director for the [University of Washington Planetarium](https://astro.washington.edu/uw-planetarium). My academic interests include data analysis of large-scale astronomical surveys, stellar variability, time-domain astronomy, and the classification of transient phenomena.

Please contact me by email: [atzanida@uw.edu](mailto:atzanida@uw.edu).