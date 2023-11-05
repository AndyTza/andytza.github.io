---
title: "Is Data Visualization/Animation Software, Blender, the Future of Astronomical Education?"
date: 2020-04-05
tags: [astronomy, NASA, Jupiter, Voyager]
excerpt: "In this article, we discuss the importance of scientific data visualization of planetary and general astronomy"
---

In the innovative and expanding world of digital media, I think that static astronomical images that are classified as "educational" are falling behind to what modern graphics/animations are capable of doing. Sure, as a photography enthusiast myself, I can appreciate the raw beauty of a beautiful galaxy image taken from the Hubble Space Telescope. However, I suspect that the impact one such image may have is quite correlated with prior our knowledge of what we are looking at.

When it comes to exciting and educating the next generation astronomers, I ask: how do we acclimate to the standards of our generation? Let's face it, digital media are now part of many modern tools used to convey excitement and information to students and the general public. Data taken from the U.S show that in 2019 roughly 80% of internet users in the age range 15-25 years old use the video platform Youtube: 

![alt text](/personal_projects/blog_data/YoutubeImpact.jpeg "Data from YouTube U.S showing the relative frequency of users grouped by age" height="350" width="350")
(Data courtesy: J. Clement, Oct 10, 2019, by [Statista](https://www.statista.com/))

I think this alone proves that the current generation is naturally very used to digital-motion conent. This is where I think open source software like Blender can play a crucial role as a vehicle for education. For those who are not familiar with Blender, this is an free open-source data animation/video software often used in the animation industry. 

As a proof of concept, let's bring to life an image of Jupiter taken from the Gallileo spacecraft. Here was the general workflow: 

1. Find Mollweide projection maps of Jupiter (Voyager) and Calliso (Gallileo), download highest frame format
2. Generate in Blender "spherical" mesh objects (although to be more accurate one would have to create a oblate spheroid for Jupiter)
3. Stich and project the generated maps from the sattelite to the mesh objects
4. Add syntheic simulation of a mock atmosphere with some emission and opaquness factor
5. Generate a lighting sceene you find to look most realistic 
6. Generate a movie scene you think would attract your audience 
7. Post-processing adjust hues, grain and other image quality settings

![alt text](/images/jup_callisto.jpg "Blender rendered image of Jupiter and Callisto taken from Voyager 1" height="400" width="400")
(Static redendering image of Jupiter and Callisto)

![alt text](/images/Jupiter_Callisto_anim.gif "Blender rendered image of Jupiter and Callisto taken from Voyager 1" height="400" width="400")
(Dynamic video rendering of flyby camera passing by Callisto with Jupiter in the background)





P.S -- 
For my fellow educators and data visual artists, if you would like a detailed tutorial of how I created this animation, let's chat! 

Credits: 
--- 
- [NASA.gov](https://www.nasa.gov/)
- Community, B.O., 2018. Blender - a 3D modeling and rendering package, Stichting Blender Foundation, Amsterdam. Available at: [blender.org](http://www.blender.org).