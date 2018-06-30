#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 16:02:46 2018

@author: Archi
"""

import pandas as pd
import dwd_parameter as dwdpara

# get climate data from pickle
path = dwdpara.path_use_data + dwdpara.wai_name_climate_final_all_data
df_climate_in = pd.read_pickle(path)
#print(df_climate_in.dtypes)

# get excluded stations
# exclusions were done based on required data availability
# station which do not provide required data become excluded
path = dwdpara.wai_data_excluded_stations_list
df_excluded = pd.read_csv(path)
lst_excluded = df_excluded['STATIONS_ID'].tolist()

#print(lst_excluded)
filter_ex = ~df_climate_in['STATIONS_ID'].isin(lst_excluded)
df_climate_wrk = df_climate_in[filter_ex]
print(df_climate_wrk.shape)

columns = ['STATIONS_ID','MESS_DATUM','TMK','TXK','TNK','RSK','RSKF']
df_climate_wrk = df_climate_wrk[columns]


df_climate_wrk.sort_values(['STATIONS_ID', 'MESS_DATUM'], ascending=[True, True], inplace=True)
#print(df_climate_wrk)

# check if all all dates complete
df_grouped = df_climate_wrk.groupby(['MESS_DATUM'])['STATIONS_ID'].agg(['nunique'])
df_grouped = df_climate_wrk.groupby(['STATIONS_ID'])['MESS_DATUM'].agg(['nunique'])
#df_climate_wrk.to_csv('../data/test/tmp.csv')

# replace occurences of -999 by mean value of adjacent dates

lst_stations = df_climate_wrk['STATIONS_ID'].drop_duplicates().tolist()
print('active stations: ', len(lst_stations))

lst_timescale = df_climate_wrk['MESS_DATUM'].drop_duplicates().tolist()
print('available dates: ', len(lst_timescale), 'from:', min(lst_timescale),'to:',max(lst_timescale))
#lst_timescale.append(20180520)
df_timescale = pd.DataFrame({'MESS_DATUM':lst_timescale})
#print(df_timescale)

df_match = pd.merge(df_timescale,df_climate_wrk,on='MESS_DATUM',how='left')

#f1 = df_match['STATIONS_ID'].isnull()
#print(df_match[f1])
