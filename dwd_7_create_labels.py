#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 08:10:59 2017

@author: Developer
"""

import numpy as np
import pandas as pd

import dwd_parameter as dwdpara

# read station meta data
path = dwdpara.path_meta_data + 'stations.pickle'
df_stations = pd.read_pickle(path)

# fix possible type deviations in station meta file
df_stations['STATIONS_ID'] = df_stations['STATION_ID'].astype(int)
df_stations['LATITUDE'] = df_stations['LATITUDE'].astype(float)
df_stations['LONGITUDE'] = df_stations['LONGITUDE'].astype(float)
df_stations['HEIGHT'] = df_stations['HEIGHT'].astype(float)
df_stations['LATITUDE_R'] = df_stations['LATITUDE'].round(1)
df_stations['LONGITUDE_R'] = df_stations['LONGITUDE'].round(1)

# read clean weather data
path = dwdpara.path_use_data + dwdpara.wai_name_climate_clean_data
df_weather = pd.read_pickle(path)

print(df_stations[df_stations.STATIONS_ID==6305])
print("\nSTATIONS")
print(df_stations.dtypes)
print("\nWEATHER DATA")
print(df_weather.dtypes)
print("\nSample Data")
print(df_weather.head(10))

df_weather['LT_'] = 0
df_weather['LN_'] = 0
df_weather['L'] = 0

"""
for i in range(25):
    label = 'L%s' % (i+1)
    print(label)
    df_weather[label] = 0
"""    
print(df_weather.dtypes)

# Temperaturklassen
df_weather.loc[df_weather.TMK < 0.0,'LT_'] = 1
df_weather.loc[(df_weather.TMK >=0.0) & (df_weather.TMK < 10.0),'LT_'] = 2
df_weather.loc[(df_weather.TMK >=10.0) & (df_weather.TMK < 20.0),'LT_'] = 3
df_weather.loc[(df_weather.TMK >=20.0) & (df_weather.TMK < 30.0),'LT_'] = 4
df_weather.loc[df_weather.TMK >= 30.0,'LT_'] = 5

# Niederschlagsklassen
df_weather.loc[df_weather.RSK < 0.0,'LN_'] = 1
df_weather.loc[(df_weather.RSK >=0.0) & (df_weather.RSK < 10.0),'LN_'] = 2
df_weather.loc[(df_weather.RSK >=10.0) & (df_weather.RSK < 50.0),'LN_'] = 3
df_weather.loc[(df_weather.RSK >=50.0) & (df_weather.RSK < 100.0),'LN_'] = 4
df_weather.loc[df_weather.RSK >= 100.0,'LN_'] = 5

# now create a 25 value label which describes the weather and will serve as 
# label in the learning phase
df_weather['L'] = 1 + (df_weather['LT_']-1) + 5*(df_weather['LN_']-1)

print('\nData')
#print(df_weather.head(10))
#print(df_weather.shape)

# now merge station data on Station ID
df_wrk = df_weather.merge(df_stations,on='STATIONS_ID',how='inner')
df_wrk.sort_values(['MESS_DATUM','LATITUDE_R','LONGITUDE_R','LATITUDE','LONGITUDE','STATIONS_ID'], ascending=True, inplace=True)
df_wrk.drop(['NAME','LATITUDE','LONGITUDE','LT_','LN_'],axis=1,inplace=True)
# sort by date and station
#df_weather.sort_values(['MESS_DATUM','STATIONS_ID'],ascending=True,inplace=True )

print('\nData Sorted')
print(df_wrk.head(20))

# in a first step learning will focus on predicting the weather label for 
# a station x n days after the observation

#arr_data = df_weather[['TMK','TXK','TNK','RSK','RSKF']].as_matrix()
#arr_labels = df_weather[['L0','L1','L2','L3','L4','L5','L6','L7','L8','L9']].as_matrix()

#print(type(arr_labels))
#print(arr_data)
print(df_weather[['L']].drop_duplicates())

