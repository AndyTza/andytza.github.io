---
title: "[Tutorial] How to Build Your Own Weather Reporting App"
date: 2020-07-24
tags: [python, data, datavisualization, webscrapi-

<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-164344843-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-164344843-1');
</script>

(Currently working on this article - come back later!)

Almost four years ago, I remember during my very first internship I fell in love with coding. Undeniably, if you have ever attempted to write any kind of software, you know how fustrating yet rewarding the experience can be. Aside from my academic research that requires a major part of my time analyzing data with coding, I actually think that a more common practice of writing software can be very handy.

This is the most common question I am asked; how did you learn Python?



```python

  def forecast_zip(zip_customer):
    """Given a user zip-code, return some general weather summary statistics.

       Input
       -----
       zip_customer (str): Zip-code location

       Output
       -----
       index=0 (float): Median daily temperature
       index=1 (float): Minimum daily temperature
       index=2 (float): Maximum daily temperature
       index=3 (float): Median chance of rain
       index=4 (float): Minimum chance of rain
       index=5 (float): Maximum chance of rain
    """
    # Define path to chromedriver.exe
    PATH="ENTER_YOUR_PATH_HERE"
    HOST_WEBSITE = "https://www.wxyz.com/weather" # website we will be scraping

    # Open url path with google chrome
    driver = webdriver.Chrome(PATH)
    driver.get(host_website)

```
