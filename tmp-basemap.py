#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 12:14:49 2017

@author: Developer
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
#import numpy as np
 
# make sure the value of resolution is a lowercase L,
#  for 'low', not a numeral 1
my_map = Basemap(projection='merc', lat_0=52, lon_0=12,
              resolution='l', area_thresh=1000.0,
    llcrnrlon= 0, llcrnrlat=42,
    urcrnrlon= 24, urcrnrlat=62)

 
my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color='coral')
my_map.drawmapboundary()


my_map.drawmeridians(np.arange(0, 360, 30))
my_map.drawparallels(np.arange(-90, 90, 30))

lon = 8.2370
lat = 52.9335
x,y = my_map(lon, lat)
my_map.plot(x, y, 'bo', markersize=12)

 
plt.show()