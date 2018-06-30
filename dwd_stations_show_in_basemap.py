#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 11:27:09 2017

@author: Developer
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import dwd_parameter as dwdpara
#import numpy as np
 
# make sure the value of resolution is a lowercase L,
#  for 'low', not a numeral 1
my_map = Basemap(projection='merc', lat_0=52, lon_0=12,
              resolution='h', area_thresh=100.0,
    llcrnrlon= 2, llcrnrlat=46,
    urcrnrlon= 18, urcrnrlat=56)

 
my_map.drawcoastlines()
my_map.drawcountries()
#my_map.fillcontinents(color='coral')
#my_map.drawmapboundary()


my_map.drawmeridians(np.arange(0, 360, 30))
my_map.drawparallels(np.arange(-90, 90, 30))

# get excluded stations
# exclusions are performed based on required data availability
# station which do not provide required data are excluded
path = dwdpara.wai_data_excluded_stations_list
df_excluded = pd.read_csv(path)
lst_excluded = df_excluded['STATIONS_ID'].tolist()
 
# get station list and add positions to map
path = dwdpara.path_meta_data + 'stations.pickle'
df_stations = pd.read_pickle(path)
df_stations['STATIONS_ID'] = df_stations['STATION_ID'].astype(str).astype(int)

print(lst_excluded)
filter_ex = ~df_stations['STATIONS_ID'].isin(lst_excluded)
df_stations = df_stations[filter_ex]

print('plot stations ... number submitted: %d', df_stations.shape[0])
lons = []
lats = []
labels = []
for idx, rows in df_stations.iterrows():
    print(idx, rows[0], float(rows[2]), float(rows[3]))
    lats.append(float(rows[2]))
    lons.append(float(rows[3]))
    labels.append(rows[0])

x,y = my_map(lons, lats)
x0,y0 = my_map([10.4], [51.0])

my_map.plot(x, y, 'ro', markersize=2)
my_map.plot(x0,y0, 'b+', markersize=3)

#for label, xpt, ypt in zip(labels, x, y):
#    plt.text(xpt-25000, ypt+5000, label)

plt.show()