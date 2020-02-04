
Author: *Andy Tzanidakis*


Hello! Welcome to my very first official blog post! Please pardon my expressions and rambling, as an avid 

This tutorial aims to educate newcomers and students who are interested in learning how to use the *Gaia DR2* dataset and ways of visualizing the survey data. This tutorial already assumes that the user knows how to plot data with `matplotlib` or any package of their preference and some basic data controlling.

I'll be covering some very basics about ADQL (Astronomical Database Query Language), however, in the resouces page you should be able to find more detailed tutorials. For the take of time, I will be explaining the very `CONE_SEARCH` to visualize galaxies in our local group. 

The scope of this tutorial? Friendly introduction to querying *Gaia DR2* data, and it's always fun to visualize data in fun ways. 




#### More detailed resouces
___



```python
import astropy.units as u
from astropy.coordinates import SkyCoord
from astroquery.gaia import Gaia


import matplotlib.pyplot as plt
%config InlineBackend.figure_formats = ['png']
%matplotlib inline
```


```python
import numpy as np

from bokeh.plotting import figure, show
from bokeh.layouts import row

# normal distribution center at x=0 and y=5
x = ra
y = dec

H, xe, ye = np.histogram2d(ra, dec, bins=200)

# produce an image of the 2d histogram
p = figure(x_range=(min(xe), max(xe)), y_range=(min(ye), max(ye)), title='Image')

p.image(image=[H], x=xe[0], y=ye[0], dw=xe[-1] - xe[0], dh=ye[-1] - ye[0], palette="Turbo256")

# produce hexbin plot
p2 = figure(title="Hexbin", match_aspect=True)
p.grid.visible = False

r, bins = p2.hexbin(x, y, size=0.1, hover_color="pink", hover_alpha=0.8, palette='Turbo256')

show(row(p))
```

### Local Group Galaxies
___

Based on the large volume of data in Gaia DR2, generally when searching for something specific in the sky we can query our search based on any criteria the databases has. In our case, since we simply want to visualize the galaxies all we need is to restrict our search based on coordinates of these sources in the sky. 

First, we need to know exactly the coordinates of the local group galaxies in order to query the data


M31 (Andromeda): ($\alpha^{o}$, $\delta^{o}$) $\approx$ = (121.174322, -21.573311) [Andromeda Coordinates - Simbad](http://simbad.u-strasbg.fr/simbad/sim-basic?Ident=m31&submit=SIMBAD+search)




`gaiadr2.gaia_source` where we can find gaia dr2 data


```python
# Define coordinates of M31 in Galactic coordinates 
m31_l, m31_b = 120.7162630976154*u.deg, -21.1387042770371*u.deg



m31_coord = SkyCoord(l=m31_l, b=m31_b, frame='galactic') # let's make 

```


```python
m31_coord.icrs
```




    <SkyCoord (ICRS): (ra, dec) in deg
        (10.091885, 41.685413)>



At first glance, ADQL can be quite daunting. But bare with me for a second, and I am certain this will make sense. Here I have broken down the query search line-by-line:

Let's desipher what's going on in the query string: 

- `SELECT ra, dec, phot_g_mean_mag...`: GaiaDR2 has a large number of variables that we can query. It wouldn't be smart to download variables we know before hand we aren't going to use. Here the ADQL command is basically selecting only the paramter names we want for our final table which is the coordinates and magnitudes of the sources.


- `FROM gaiadr2.gaia_source`: gaiadr2.gaia_source is simply the table we're querying from.


- `WHERE CONTAINS(POINT('ICRS',gaiadr2.gaia_source.ra, gaiadr2.gaia_source.dec), CIRCLE('ICRS',10.6846997,41.26874756,3))=1\`: This is the beating heart of our query search. We start with the `WHERE` argument that simply means that the query **must** meet a condition. In this case our condition is `CONTAINS`.


- `WHERE CONTAINS(POINT('coordinate_frame', <gaiaDr2.variable_name:RA> dec), CIRCLE('coordinate_frame', ra, dec, radius))=1`


```python
# Let's make an ADQL cone query centered around m31 coordinates with a 5 deg radius (or smaller)
query = "SELECT ra,dec, parallax, phot_g_mean_mag\
, phot_bp_mean_mag, phot_rp_mean_mag FROM gaiadr2.gaia_source \
WHERE CONTAINS(POINT('ICRS',gaiadr2.gaia_source.ra,gaiadr2.gaia_source.dec), CIRCLE('ICRS',10.6846997, 41.26874756, 3))=1"

```


```python
# It will take a bit 
my = Gaia.launch_job_async(query).get_results() # takes a couple of minutes! hang tight...
```

    INFO: Query finished. [astroquery.utils.tap.core]



```python
ra, dec = my['ra'], my['dec']
```


```python
plt.figure(figsize=(6,5))
plt.hist2d(my['ra'], my['dec'], cmap='bone', bins=0)
plt.colorbar()
plt.scatter(10.67, 40.86, color='yellow')

plt.tight_layout()


```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-114-bb13e1c2cea1> in <module>
          1 plt.figure(figsize=(6,5))
    ----> 2 plt.hist2d(my['ra'], my['dec'], cmap='bone', bins=0)
          3 plt.colorbar()
          4 plt.scatter(10.67, 40.86, color='yellow')
          5 


    ~/anaconda/envs/py36/lib/python3.6/site-packages/matplotlib/pyplot.py in hist2d(x, y, bins, range, density, weights, cmin, cmax, data, **kwargs)
       2651         x, y, bins=bins, range=range, density=density,
       2652         weights=weights, cmin=cmin, cmax=cmax, **({"data": data} if
    -> 2653         data is not None else {}), **kwargs)
       2654     sci(__ret[-1])
       2655     return __ret


    ~/anaconda/envs/py36/lib/python3.6/site-packages/matplotlib/__init__.py in inner(ax, data, *args, **kwargs)
       1599     def inner(ax, *args, data=None, **kwargs):
       1600         if data is None:
    -> 1601             return func(ax, *map(sanitize_sequence, args), **kwargs)
       1602 
       1603         bound = new_sig.bind(ax, *args, **kwargs)


    ~/anaconda/envs/py36/lib/python3.6/site-packages/matplotlib/cbook/deprecation.py in wrapper(*args, **kwargs)
        305                 f"for the old name will be dropped %(removal)s.")
        306             kwargs[new] = kwargs.pop(old)
    --> 307         return func(*args, **kwargs)
        308 
        309     # wrapper() must keep the same documented signature as func(): if we


    ~/anaconda/envs/py36/lib/python3.6/site-packages/matplotlib/axes/_axes.py in hist2d(self, x, y, bins, range, density, weights, cmin, cmax, **kwargs)
       7065 
       7066         h, xedges, yedges = np.histogram2d(x, y, bins=bins, range=range,
    -> 7067                                            normed=density, weights=weights)
       7068 
       7069         if cmin is not None:


    <__array_function__ internals> in histogram2d(*args, **kwargs)


    ~/anaconda/envs/py36/lib/python3.6/site-packages/numpy/lib/twodim_base.py in histogram2d(x, y, bins, range, normed, weights, density)
        713         xedges = yedges = asarray(bins)
        714         bins = [xedges, yedges]
    --> 715     hist, edges = histogramdd([x, y], bins, range, normed, weights, density)
        716     return hist, edges[0], edges[1]
        717 


    <__array_function__ internals> in histogramdd(*args, **kwargs)


    ~/anaconda/envs/py36/lib/python3.6/site-packages/numpy/lib/histograms.py in histogramdd(sample, bins, range, normed, weights, density)
       1049             if bins[i] < 1:
       1050                 raise ValueError(
    -> 1051                     '`bins[{}]` must be positive, when an integer'.format(i))
       1052             smin, smax = _get_outer_edges(sample[:,i], range[i])
       1053             edges[i] = np.linspace(smin, smax, bins[i] + 1)


    ValueError: `bins[0]` must be positive, when an integer



![png](gaia_fun_files/gaia_fun_10_1.png)



```python
from scipy import stats
import numpy as np
```


```python
hist = stats.binned_statistic_2d((my['ra']),
                                 (my['dec']),
                                 ,
                                 bins=150, statistic='median')
```


```python
df = my["phot_bp_mean_mag"]-my["phot_rp_mean_mag"]
```


```python
h = np.histogram2d(my['ra'], my['dec'], bins=850)
```


```python
df = np.array(df)
```


```python
plt.figure(figsize=(12,12))
plt.imshow(np.log(h[0]), origin='lower')
plt.colorbar()
```

    /Users/iraf1/anaconda/envs/py36/lib/python3.6/site-packages/ipykernel_launcher.py:2: RuntimeWarning: divide by zero encountered in log
      





    <matplotlib.colorbar.Colorbar at 0x12b3796d8>




![png](gaia_fun_files/gaia_fun_16_2.png)



```python

```


![png](gaia_fun_files/gaia_fun_17_0.png)



```python
# How to launch query using gaiadr2 -- asynchronous search! 
job = Gaia.launch_job_async("select top 1000 * from gaiadr2.gaia_source order by source_id")
q1 = job.get_results()
```

    WARNING: W35: None:5:0: W35: 'value' attribute required for INFO elements [astropy.io.votable.tree]
    WARNING: W35: None:6:0: W35: 'value' attribute required for INFO elements [astropy.io.votable.tree]
    WARNING: W35: None:7:0: W35: 'value' attribute required for INFO elements [astropy.io.votable.tree]
    WARNING: W35: None:8:0: W35: 'value' attribute required for INFO elements [astropy.io.votable.tree]
    WARNING: W35: None:10:0: W35: 'value' attribute required for INFO elements [astropy.io.votable.tree]
    WARNING: W06: None:47:0: W06: Invalid UCD 'arith.ratio': Secondary word 'arith.ratio' is not valid as a primary word [astropy.io.votable.tree]
    WARNING: W50: None:50:0: W50: Invalid unit string 'mas.yr**-1' [astropy.io.votable.tree]
    WARNING: W50: None:53:0: W50: Invalid unit string 'mas.yr**-1' [astropy.io.votable.tree]
    WARNING: W50: None:56:0: W50: Invalid unit string 'mas.yr**-1' [astropy.io.votable.tree]
    WARNING: W50: None:59:0: W50: Invalid unit string 'mas.yr**-1' [astropy.io.votable.tree]
    WARNING: W50: None:122:0: W50: Invalid unit string 'mas**-2' [astropy.io.votable.tree]
    WARNING: W50: None:125:0: W50: Invalid unit string 'um**-1' [astropy.io.votable.tree]
    WARNING: W06: None:128:0: W06: Invalid UCD 'em.wavenumber;stat.error': Primary word 'stat.error' is not valid as a secondary word [astropy.io.votable.tree]
    WARNING: W50: None:128:0: W50: Invalid unit string 'um**-1' [astropy.io.votable.tree]
    WARNING: W06: None:140:0: W06: Invalid UCD 'pos.errorEllipse;stat.max': Secondary word 'pos.errorEllipse' is not valid as a primary word [astropy.io.votable.tree]
    WARNING: W50: None:155:0: W50: Invalid unit string ''electron'.s**-1' [astropy.io.votable.tree]
    WARNING: W50: None:158:0: W50: Invalid unit string ''electron'.s**-1' [astropy.io.votable.tree]
    WARNING: W06: None:161:0: W06: Invalid UCD 'arith.ratio': Secondary word 'arith.ratio' is not valid as a primary word [astropy.io.votable.tree]
    WARNING: W50: None:170:0: W50: Invalid unit string ''electron'.s**-1' (suppressing further warnings of this type...) [astropy.io.votable.tree]
    WARNING: W06: None:176:0: W06: Invalid UCD 'arith.ratio': Secondary word 'arith.ratio' is not valid as a primary word [astropy.io.votable.tree]
    WARNING: W06: None:191:0: W06: Invalid UCD 'arith.ratio': Secondary word 'arith.ratio' is not valid as a primary word [astropy.io.votable.tree]
    WARNING: W06: None:203:0: W06: Invalid UCD 'phot.color': Unknown word 'phot.color' [astropy.io.votable.tree]
    WARNING: W06: None:206:0: W06: Invalid UCD 'phot.color': Unknown word 'phot.color' [astropy.io.votable.tree]
    WARNING: W06: None:209:0: W06: Invalid UCD 'phot.color': Unknown word 'phot.color' [astropy.io.votable.tree]
    WARNING: W06: None:281:0: W06: Invalid UCD 'phys.size.radius;stat.error': Primary word 'stat.error' is not valid as a secondary word (suppressing further warnings of this type...) [astropy.io.votable.tree]


    INFO: Query finished. [astroquery.utils.tap.core]



```python

```




&lt;MaskedColumn name=&apos;pmdec&apos; dtype=&apos;float64&apos; unit=&apos;mas / yr&apos; description=&apos;Proper motion in declination direction&apos; length=1000&gt;
<table>
<tr><td>-4.7759340851709</td></tr>
<tr><td>20.102047674607906</td></tr>
<tr><td>19.22596279977244</td></tr>
<tr><td>-0.46855864263402947</td></tr>
<tr><td>-1.5922073291150058</td></tr>
<tr><td>-8.081723161708615</td></tr>
<tr><td>-16.297421650379626</td></tr>
<tr><td>-10.492354103767575</td></tr>
<tr><td>--</td></tr>
<tr><td>2.986190212989857</td></tr>
<tr><td>-6.278087886862299</td></tr>
<tr><td>-6.629734193894839</td></tr>
<tr><td>...</td></tr>
<tr><td>-28.642673639479604</td></tr>
<tr><td>-4.11743126541802</td></tr>
<tr><td>1.0002667607833344</td></tr>
<tr><td>-2.746328112973657</td></tr>
<tr><td>-8.169595542301268</td></tr>
<tr><td>-3.4217093831029874</td></tr>
<tr><td>-5.814484155628955</td></tr>
<tr><td>-1.9651534042851382</td></tr>
<tr><td>-2.681710411921118</td></tr>
<tr><td>-16.011233930266602</td></tr>
<tr><td>-12.280376260765037</td></tr>
<tr><td>-0.6962979263963816</td></tr>
</table>


