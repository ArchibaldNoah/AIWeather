#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 14:28:23 2018

@author: Developer
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

import dwd_parameter as dwdpara

print('plot station data')
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
print(df_stations[df_stations.NAME.str.contains('Freiburg')])

# get cleaned station data
path = dwdpara.path_use_data + dwdpara.wai_name_climate_final_all_data
#path = dwdpara.path_use_data + dwdpara.wai_name_climate_final_data
df_climate_in = pd.read_pickle(path)
#plt.scatter(df_climate_in.loc[df_climate_in.STATIONS_ID == 1078,['MESS_DATUM']],df_climate_in.loc[df_climate_in.STATIONS_ID == 1078,['TMK']])
sid = 5792
#df_plt = df_climate_in.loc[df_climate_in.STATIONS_ID == sid,['RSK']]
#plt.plot(df_plt)

#df_plt = df_climate_in.loc[df_climate_in.STATIONS_ID == sid,['TXK']]
#plt.plot(df_plt)


df_plt_2 = df_climate_in.loc[df_climate_in.STATIONS_ID == sid,['FX']]
df_plt_2.reset_index(inplace=True, drop=True)
#plt.plot(df_plt_2)

df_plt_s = df_climate_in.loc[df_climate_in.STATIONS_ID == sid,['RSK','SDK','TMK']]
df_plt_s.reset_index(inplace=True, drop=True)

# Köln > 2667, Düsseldorf > 1078, Berlin > 430, Sylt > 3032
# Aachen > 15000, München > 1262, Hamburg > 1975, Freiburg > 1443

df_D = df_climate_in.loc[df_climate_in.STATIONS_ID == 1078,['MESS_DATUM','RSK','SDK','TMK','RSKF']]
df_Dx = df_D[df_D.MESS_DATUM != 20160405]
print(df_Dx.shape)

df_C = df_climate_in.loc[df_climate_in.STATIONS_ID == 15000,['MESS_DATUM','RSK','SDK','TMK','RSKF']]
df_Cx = df_C[df_C.MESS_DATUM != 20160405]
print(df_Cx.shape)

x = df_Dx['SDK']
y = df_Cx['SDK']
#plt.scatter(x,y)
#print(lst_excluded)
#filter_ex = ~df_stations['STATIONS_ID'].isin(lst_excluded)
#df_stations = df_stations[filter_ex]
#print(df_stations.head())
#print(df_climate_in.MESS_DATUM.max())
#path = dwdpara.path_use_data + "x.csv"
#df_plt.to_csv(path)

#df_j = df_D.merge(df_C, on='MESS_DATUM', how='left')
print(df_D.dtypes)
#print(df_C.head())
#print(df_j.head())


"""
==============================
Create 3D histogram of 2D data
==============================

Demo of a histogram for 2 dimensional data as a bar graph in 3D.
"""

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#x, y = np.random.rand(2, 100) * 4
hist, xedges, yedges = np.histogram2d(x, y, bins=8, range=[[0, 8], [0, 8]])

# Construct arrays for the anchor positions of the 16 bars.
# Note: np.meshgrid gives arrays in (ny, nx) so we use 'F' to flatten xpos,
# ypos in column-major order. For numpy >= 1.7, we could instead call meshgrid
# with indexing='ij'.
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25)
xpos = xpos.flatten('F')
ypos = ypos.flatten('F')
zpos = np.zeros_like(xpos)

# Construct arrays with the dimensions for the 16 bars.
dx = 0.5 * np.ones_like(zpos)
dy = dx.copy()
dz = hist.flatten()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', zsort='average')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')

plt.show()