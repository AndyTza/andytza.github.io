---
title: "Jupyter Notebook Test"
date: 2020-02-03
tags: [astronomy, gaiadr2]
excerpt: "Jupyter Notebook Gaia DR2"
---

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
WHERE CONTAINS(POINT('ICRS',gaiadr2.gaia_source.ra,gaiadr2.gaia_source.dec), CIRCLE('ICRS',10.091885, 41.685413, 0.05))=1"

```


```python
# It will take a bit
my = Gaia.launch_job_async(query).get_results() # takes a couple of minutes! hang tight...
```

    INFO: Query finished. [astroquery.utils.tap.core]



```python
plt.figure(figsize=(6,5))
plt.hist2d(my['ra'], my['dec'], cmap='bone', bins=50)
plt.colorbar()
plt.scatter(10.67, 40.86, color='yellow')

plt.tight_layout()


```


![png](Gaia%20DR2%20Galaxies%20in%20the%20Local%20Group%20-%20fun%20data-viz%20-%20Blog%20Tutorial_files/Gaia%20DR2%20Galaxies%20in%20the%20Local%20Group%20-%20fun%20data-viz%20-%20Blog%20Tutorial_8_0.png)



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




![png](Gaia%20DR2%20Galaxies%20in%20the%20Local%20Group%20-%20fun%20data-viz%20-%20Blog%20Tutorial_files/Gaia%20DR2%20Galaxies%20in%20the%20Local%20Group%20-%20fun%20data-viz%20-%20Blog%20Tutorial_14_2.png)



```python

```


![png](Gaia%20DR2%20Galaxies%20in%20the%20Local%20Group%20-%20fun%20data-viz%20-%20Blog%20Tutorial_files/Gaia%20DR2%20Galaxies%20in%20the%20Local%20Group%20-%20fun%20data-viz%20-%20Blog%20Tutorial_15_0.png)



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
# Okay now let's make a more sophisticated coordinate search using ADQL
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




```python
from astroquery.gaia import Gaia
>>> tables = Gaia.load_tables(only_names=True)
>>> for table in (tables):
>>>   print(table.get_qualified_name())
```

    INFO: Retrieving tables... [astroquery.utils.tap.core]
    INFO: Parsing tables... [astroquery.utils.tap.core]
    INFO: Done. [astroquery.utils.tap.core]
    external.external.apassdr9
    external.external.gaiadr2_geometric_distance
    external.external.ravedr5_com
    external.external.ravedr5_dr5
    external.external.ravedr5_gra
    external.external.ravedr5_on
    external.external.sdssdr13_photoprimary
    external.external.skymapperdr1_master
    external.external.tmass_xsc
    public.public.hipparcos
    public.public.hipparcos_newreduction
    public.public.hubble_sc
    public.public.igsl_source
    public.public.igsl_source_catalog_ids
    public.public.tycho2
    public.public.dual
    tap_config.tap_config.coord_sys
    tap_schema.tap_schema.columns
    tap_schema.tap_schema.key_columns
    tap_schema.tap_schema.keys
    tap_schema.tap_schema.schemas
    tap_schema.tap_schema.tables
    gaiadr1.gaiadr1.aux_qso_icrf2_match
    gaiadr1.gaiadr1.ext_phot_zero_point
    gaiadr1.gaiadr1.allwise_best_neighbour
    gaiadr1.gaiadr1.allwise_neighbourhood
    gaiadr1.gaiadr1.gsc23_best_neighbour
    gaiadr1.gaiadr1.gsc23_neighbourhood
    gaiadr1.gaiadr1.ppmxl_best_neighbour
    gaiadr1.gaiadr1.ppmxl_neighbourhood
    gaiadr1.gaiadr1.sdss_dr9_best_neighbour
    gaiadr1.gaiadr1.sdss_dr9_neighbourhood
    gaiadr1.gaiadr1.tmass_best_neighbour
    gaiadr1.gaiadr1.tmass_neighbourhood
    gaiadr1.gaiadr1.ucac4_best_neighbour
    gaiadr1.gaiadr1.ucac4_neighbourhood
    gaiadr1.gaiadr1.urat1_best_neighbour
    gaiadr1.gaiadr1.urat1_neighbourhood
    gaiadr1.gaiadr1.cepheid
    gaiadr1.gaiadr1.phot_variable_time_series_gfov
    gaiadr1.gaiadr1.phot_variable_time_series_gfov_statistical_parameters
    gaiadr1.gaiadr1.rrlyrae
    gaiadr1.gaiadr1.variable_summary
    gaiadr1.gaiadr1.allwise_original_valid
    gaiadr1.gaiadr1.gsc23_original_valid
    gaiadr1.gaiadr1.ppmxl_original_valid
    gaiadr1.gaiadr1.sdssdr9_original_valid
    gaiadr1.gaiadr1.tmass_original_valid
    gaiadr1.gaiadr1.ucac4_original_valid
    gaiadr1.gaiadr1.urat1_original_valid
    gaiadr1.gaiadr1.gaia_source
    gaiadr1.gaiadr1.tgas_source
    gaiadr2.gaiadr2.aux_allwise_agn_gdr2_cross_id
    gaiadr2.gaiadr2.aux_iers_gdr2_cross_id
    gaiadr2.gaiadr2.aux_sso_orbit_residuals
    gaiadr2.gaiadr2.aux_sso_orbits
    gaiadr2.gaiadr2.dr1_neighbourhood
    gaiadr2.gaiadr2.allwise_best_neighbour
    gaiadr2.gaiadr2.allwise_neighbourhood
    gaiadr2.gaiadr2.apassdr9_best_neighbour
    gaiadr2.gaiadr2.apassdr9_neighbourhood
    gaiadr2.gaiadr2.gsc23_best_neighbour
    gaiadr2.gaiadr2.gsc23_neighbourhood
    gaiadr2.gaiadr2.hipparcos2_best_neighbour
    gaiadr2.gaiadr2.hipparcos2_neighbourhood
    gaiadr2.gaiadr2.panstarrs1_best_neighbour
    gaiadr2.gaiadr2.panstarrs1_neighbourhood
    gaiadr2.gaiadr2.ppmxl_best_neighbour
    gaiadr2.gaiadr2.ppmxl_neighbourhood
    gaiadr2.gaiadr2.ravedr5_best_neighbour
    gaiadr2.gaiadr2.ravedr5_neighbourhood
    gaiadr2.gaiadr2.sdssdr9_best_neighbour
    gaiadr2.gaiadr2.sdssdr9_neighbourhood
    gaiadr2.gaiadr2.tmass_best_neighbour
    gaiadr2.gaiadr2.tmass_neighbourhood
    gaiadr2.gaiadr2.tycho2_best_neighbour
    gaiadr2.gaiadr2.tycho2_neighbourhood
    gaiadr2.gaiadr2.urat1_best_neighbour
    gaiadr2.gaiadr2.urat1_neighbourhood
    gaiadr2.gaiadr2.sso_observation
    gaiadr2.gaiadr2.sso_source
    gaiadr2.gaiadr2.vari_cepheid
    gaiadr2.gaiadr2.vari_classifier_class_definition
    gaiadr2.gaiadr2.vari_classifier_definition
    gaiadr2.gaiadr2.vari_classifier_result
    gaiadr2.gaiadr2.vari_long_period_variable
    gaiadr2.gaiadr2.vari_rotation_modulation
    gaiadr2.gaiadr2.vari_rrlyrae
    gaiadr2.gaiadr2.vari_short_timescale
    gaiadr2.gaiadr2.vari_time_series_statistics
    gaiadr2.gaiadr2.panstarrs1_original_valid
    gaiadr2.gaiadr2.gaia_source
    gaiadr2.gaiadr2.ruwe
