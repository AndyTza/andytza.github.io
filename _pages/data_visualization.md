---
layout: archive
permalink: /data_viz/
title: "Data Visualization"
author_profile: true
---


### Data visualization -
------
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
* {box-sizing: border-box;}

.img-comp-container {
  position: relative;
  height: 200px; /*should be the same height as the images*/
}

.img-comp-img {
  position: absolute;
  width: auto;
  height: auto;
  overflow:hidden;
}

.img-comp-img img {
  display:block;
  vertical-align:middle;
}

.img-comp-slider {
  position: absolute;
  z-index:9;
  cursor: ew-resize;
  /*set the appearance of the slider:*/
  width: 10px;
  height: 10px;
  background-color: #2196F3;
  opacity: 0.7;
  border-radius: 50%;
}
</style>
<script>
function initComparisons() {
  var x, i;
  /*find all elements with an "overlay" class:*/
  x = document.getElementsByClassName("img-comp-overlay");
  for (i = 0; i < x.length; i++) {
    /*once for each "overlay" element:
    pass the "overlay" element as a parameter when executing the compareImages function:*/
    compareImages(x[i]);
  }
  function compareImages(img) {
    var slider, img, clicked = 0, w, h;
    /*get the width and height of the img element*/
    w = img.offsetWidth;
    h = img.offsetHeight;
    /*set the width of the img element to 50%:*/
    img.style.width = (w / 2) + "px";
    /*create slider:*/
    slider = document.createElement("DIV");
    slider.setAttribute("class", "img-comp-slider");
    /*insert slider*/
    img.parentElement.insertBefore(slider, img);
    /*position the slider in the middle:*/
    slider.style.top = (h / 2) - (slider.offsetHeight / 2) + "px";
    slider.style.left = (w / 2) - (slider.offsetWidth / 2) + "px";
    /*execute a function when the mouse button is pressed:*/
    slider.addEventListener("mousedown", slideReady);
    /*and another function when the mouse button is released:*/
    window.addEventListener("mouseup", slideFinish);
    /*or touched (for touch screens:*/
    slider.addEventListener("touchstart", slideReady);
    /*and released (for touch screens:*/
    window.addEventListener("touchstop", slideFinish);
    function slideReady(e) {
      /*prevent any other actions that may occur when moving over the image:*/
      e.preventDefault();
      /*the slider is now clicked and ready to move:*/
      clicked = 1;
      /*execute a function when the slider is moved:*/
      window.addEventListener("mousemove", slideMove);
      window.addEventListener("touchmove", slideMove);
    }
    function slideFinish() {
      /*the slider is no longer clicked:*/
      clicked = 0;
    }
    function slideMove(e) {
      var pos;
      /*if the slider is no longer clicked, exit this function:*/
      if (clicked == 0) return false;
      /*get the cursor's x position:*/
      pos = getCursorPos(e)
      /*prevent the slider from being positioned outside the image:*/
      if (pos < 0) pos = 0;
      if (pos > w) pos = w;
      /*execute a function that will resize the overlay image according to the cursor:*/
      slide(pos);
    }
    function getCursorPos(e) {
      var a, x = 0;
      e = e || window.event;
      /*get the x positions of the image:*/
      a = img.getBoundingClientRect();
      /*calculate the cursor's x coordinate, relative to the image:*/
      x = e.pageX - a.left;
      /*consider any page scrolling:*/
      x = x - window.pageXOffset;
      return x;
    }
    function slide(x) {
      /*resize the image:*/
      img.style.width = x + "px";
      /*position the slider:*/
      slider.style.left = img.offsetWidth - (slider.offsetWidth / 2) + "px";
    }
  }
}
</script>
</head>
<body>

<h1>Compare Two Images</h1>

<p>Click and slide the blue slider to compare two images:</p>

<p> welcome to my page! </p>

<div class="img-comp-container">
  <div class="img-comp-img">
    <img src="/images/no2_2019.jpg" width="500" height="600">
  </div>
  <div class="img-comp-img img-comp-overlay">
    <img src="/images/no2_2020.jpg" width="500" height="600">
  </div>
</div>

<script>
/*Execute a function that will execute an image compare function for each element with the img-comp-overlay class:*/
initComparisons();
</script>

</body>
</html>


### Data visualization - Animations: Astronomy
___

Throughout my academic research, I have dedicated the last four years to making sophisticated data visualizations for the application of astrophysical discovery. My visuals aim to bridge the understanding of astrophysical data and the physical understanding of how galaxies look like in three-dimensional space.


*All visuals seen here are created by Anastasios Tzanidakis. If you have questions about the data and visuals please feel free to contact me.*


![alt text](/images/datviz/3d_mw_shells.gif "Shells of the MW" height="400" width="400")

![alt text](/images/datviz/Mw_Disk.gif "Shells of the MW" height="400" width="400")

![alt text](/images/datviz/bar-mw.gif "Shells of the MW" height="400" width="400")

![alt text](/images/datviz/density_mw.gif "Shells of the MW" height="400" width="400")

![alt text](/images/datviz/m311_gdr2.gif "Shells of the MW" height="400" width="400")

![alt text](/images/datviz/feathers_laporte_tzanidakis.gif "Shells of the MW" height="400" width="400")

![alt text](/images/datviz/3D_mw_gdr2.gif "Shells of the MW" height="400" width="400")

![alt text](/images/datviz/sims_radial_profile.gif "Shells of the MW" height="400" width="400")

![alt text](/images/datviz/m33_rot.gif "Shells of the MW" height="400" width="400")

![alt text](/images/datviz/galaxy_waves.gif "Shells of the MW" height="400" width="400")

### Data visualization - Interactive Data: Astronomy
___

Interactive density map of M31, using data from [*Gaia DR2*](https://www.cosmos.esa.int/web/gaia/dr2)
<iframe src="/images/m31_bo.html"
    sandbox="allow-same-origin allow-scripts"
    width="150%"
    height="600"
    scrolling="no"
    seamless="seamless"
    frameborder="0">
</iframe>



### Data visualization: Astronomy videos
___

<a href="http://www.youtube.com/watch?feature=player_embedded&v=Rpk0sVoqdKI
" target="_blank"><img src="http://img.youtube.com/vi/Rpk0sVoqdKI/0.jpg"
alt="Youtube: N-body Simulation of MW After Collision with Sagittarius dSph" width="470" height="290" border="10" /></a>

video can be found [here](http://www.youtube.com/watch?feature=player_embedded&v=Rpk0sVoqdKI) on YouTube

<a href="http://www.youtube.com/watch?feature=player_embedded&v=QaAzRI1zYsA
" target="_blank"><img src="http://img.youtube.com/vi/QaAzRI1zYsA/0.jpg"
alt="Youtube: N-body Simulation of MW After Collision with Sagittarius dSph" width="470" height="290" border="10" /></a>

video can be found [here](http://www.youtube.com/watch?feature=player_embedded&v=QaAzRI1zYsA) on YouTube
