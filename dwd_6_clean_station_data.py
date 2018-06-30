#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 08:48:25 2017

<Step 6>


@author: Developer
"""

import pandas as pd
import dwd_parameter as dwdpara

# get climate data from pickle
path = dwdpara.path_use_data + dwdpara.wai_name_climate_final_all_data
df_climate_in = pd.read_pickle(path)
print(df_climate_in.dtypes)

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

# replace occurrances of -999 by mean value of adjacent dates

lst_stations = df_climate_wrk['STATIONS_ID'].drop_duplicates().tolist()
print('active stations: ', len(lst_stations))

# fix TMK
for i in sorted(lst_stations):
    df_station = df_climate_wrk[df_climate_wrk.STATIONS_ID==i]

    #TMK
    pval = -999
    for index, row in df_station.iterrows():
        if row['TMK'] == -999:
            print(i, row['MESS_DATUM'],index)
            df_climate_wrk.loc[index,'TMK'] = pval
            #print(df_station.iloc[index])
        else:
            pval = row['TMK']
    
    #TXK
    pval = -999
    for index, row in df_station.iterrows():
        if row['TXK'] == -999:
            print(i, row['MESS_DATUM'],index)
            df_climate_wrk.loc[index,'TXK'] = pval
            #print(df_station.iloc[index])
        else:
            pval = row['TXK']    

    #TNK
    pval = -999
    for index, row in df_station.iterrows():
        if row['TNK'] == -999:
            print(i, row['MESS_DATUM'],index)
            df_climate_wrk.loc[index,'TNK'] = pval
            #print(df_station.iloc[index])
        else:
            pval = row['TNK']

    #RSK
    pval = -999
    for index, row in df_station.iterrows():
        if row['RSK'] == -999:
            print(i, row['MESS_DATUM'],index)
            df_climate_wrk.loc[index,'RSK'] = pval
            #print(df_station.iloc[index])
        else:
            pval = row['RSK']

    #RSKF
    pval = -999
    for index, row in df_station.iterrows():
        if row['RSKF'] == -999:
            print(i, row['MESS_DATUM'],index)
            df_climate_wrk.loc[index,'RSKF'] = pval
            #print(df_station.iloc[index])
        else:
            pval = row['RSKF']     
            
path = dwdpara.path_use_data + dwdpara.wai_name_climate_clean_data
df_climate_wrk.to_pickle(path)
