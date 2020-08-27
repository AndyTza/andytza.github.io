---
title: "[Tutorial] How to Build Your Own Weather Reporting App"
date: 2020-07-24
tags: [python, data, datavisualization, webscraping]
excerpt: "Fun python tutorials"
---

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


Objectives
---
- Learn how to utilize basic webscraping tools
- How t






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

    # Navigate search bar and search desired zipcode
  	search = driver.find_element_by_class_name("wxByLocation-ziporcity")

  	# Sent text to the search bar
  	search.send_keys(zip_customer) # search zip code
  	search.send_keys(Keys.RETURN) # sent ENTER to website
  	snooz()

  	# Navigate daily forecast by the CSS location
  	hr = driver.find_element_by_css_selector('body > div.Page-wrap > div > div.Weather.top > div.top-three > a:nth-child(1)')
  	hr.click() # click
  	snooz()

  	# Find forecast tabs
  	forecast = driver.find_elements_by_class_name("HourlyForecast")
  	snooz() # snooz again...

    fd = fr.text for fr in forecast # assign fd as your HTML text variable
  	snooz()

  	week_day_today = find_weekday(date.today()) # Find the day of the week for the current date of your query
  	print ("You have selected as your week day: %s"%week_day_today)
  	snooz()


    temp, rain = [], []
  	for i in range (0, len(fd.split(" "))):
  		val = fd.split(" ")[i].split() # break each category by element
      
  		# if the N_val=5: 0:condition, 1:temp, 2:percp. 3:day, 4:time

  		if len(val)==5: # select the data structure with data in
  			day_val = val[3] # day of the week

  			if day_val==week_day_today:
  				temp_val = float(val[1].split("°")[0])
  				rain_val = float(val[2].split("%")[0])

  				temp.append(temp_val)
  				rain.append(rain_val)

  		elif len(val)==6: # alternative structure...
  			day_val = val[4] # day of the week

  			if day_val==week_day_today:
  				temp_val = float(val[2].split("°")[0])
  				rain_val = float(val[3].split("%")[0])

  				temp.append(temp_val)
  				rain.append(rain_val)

  	temp, rain = np.array(temp), np.array(rain)

  	return (np.median(temp), min(temp), max(temp), np.median(rain), min(rain), max(rain))

```

Note that the `snooz()` function is a simple time function that waits for 2 seconds before moving to the next action.
