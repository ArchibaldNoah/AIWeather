#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 10:59:11 2017

@author: Developer
"""

import pandas as pd
import dwd_parameter as dwdpara

# get station list and add positions to map
path = dwdpara.path_meta_data + 'stations.pickle'
df_stations = pd.read_pickle(path)

#print(df_stations.sort_values(by=['LATITUDE']))
print(df_stations[df_stations['NAME'].str.contains('Berlin')])

df_stations.mean()