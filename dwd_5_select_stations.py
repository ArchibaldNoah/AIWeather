#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 19:18:46 2017

<Step 5>
Identify stations which provide the best data quality
Output list of excluded stations
 
@author: Developer
"""

import pandas as pd

import dwd_parameter as dwdpara

#station_list_file = open(dwdpara.wai_data_station_list,'r')

# get raw climate data from download and unzip
path = dwdpara.path_use_data + dwdpara.wai_name_climate_final_all_data
df_climate = pd.read_pickle(path)
print('Number of stations',df_climate['STATIONS_ID'].drop_duplicates().count())

#lst_stations_to_drop = []
"""
idfix = 125

print(df_climate[(df_climate.STATIONS_ID==idfix) & (df_climate.TMK == -999)][['MESS_DATUM','TMK','RSKF']])
print(df_climate[(df_climate.STATIONS_ID==idfix)][['TMK']].min())
print(df_climate[(df_climate.STATIONS_ID==idfix) & (df_climate.TMK != -999)][['TMK']].min())
"""
# get how many readings are there for each station
df_grouped_0 = df_climate.groupby(['STATIONS_ID'])['STATIONS_ID'].agg(['count'])
print('Number of stations with given number of readings')
print(df_grouped_0.sort_values('count'))

# as a first approximation we only take stations into account which provide full number of readings
# get the maximum number of readings over all stations available 
max_readings = df_grouped_0['count'].max()
print('Maximum number of readings over all stations %d:' % max_readings)

# now select all stations which can provide the maximum number of readings
df_stations_select_0 = df_grouped_0[df_grouped_0['count'] >= max_readings-dwdpara.station_data_max_missing_dates]
x = len(df_stations_select_0)
print('Stations providing required number readings selected and remaining %d:' % x)
#print('climate data initial:', df_climate.shape)

df_stations_reject_0 = df_grouped_0[df_grouped_0['count'] < max_readings - dwdpara.station_data_max_missing_dates]
y = len(df_stations_reject_0)
print('Stations not providing required number readings rejected %d:' % y)

lsx = list(df_stations_reject_0.index.values)
print(lsx)

lst_stations_to_drop = lsx
# start with TMK (mittlere Tagestemperatur)
# print('see TMK ... current removals: %d' % len(lst_stations_to_drop))
df_to_group_999 = df_climate[df_climate.TMK == -999][['STATIONS_ID', 'TMK']]
df_grouped_999 = df_to_group_999.groupby(['STATIONS_ID'])['TMK'].agg(['count','mean','max','min'])
#print(df_grouped_999[df_grouped_999['count'] > 5])
ls = list(df_grouped_999[df_grouped_999['count'] > dwdpara.station_data_max_errors].index.values)

lst_stations_to_drop= lst_stations_to_drop + ls
lst_stations_to_drop = list(set(lst_stations_to_drop))
print('Stations to drop after TMK analysis')
print(lst_stations_to_drop)

# now TXK (Tageshöchsttemperatur)
print('see TXK ... current removals: %d' % len(lst_stations_to_drop))
df_to_group_999 = df_climate[df_climate.TXK == -999][['STATIONS_ID', 'TXK']]
df_grouped_999 = df_to_group_999.groupby(['STATIONS_ID'])['TXK'].agg(['count','mean','max','min'])
#print(df_grouped_999[df_grouped_999['count'] > 5])
ls = list(df_grouped_999[df_grouped_999['count'] > dwdpara.station_data_max_errors].index.values)
#print(ls)
#lst_stations_to_drop.append(ls)
lst_stations_to_drop = lst_stations_to_drop + ls
lst_stations_to_drop = list(set(lst_stations_to_drop))
print(lst_stations_to_drop)
print(len(lst_stations_to_drop))


# now TNK
print('see TNK ... current removals: %d' % len(lst_stations_to_drop))
df_to_group_999 = df_climate[df_climate.TNK == -999][['STATIONS_ID', 'TNK']]
df_grouped_999 = df_to_group_999.groupby(['STATIONS_ID'])['TNK'].agg(['count','mean','max','min'])
ls = list(df_grouped_999[df_grouped_999['count'] > dwdpara.station_data_max_errors].index.values)
lst_stations_to_drop = lst_stations_to_drop + ls
lst_stations_to_drop = list(set(lst_stations_to_drop))
print(lst_stations_to_drop)
print(len(lst_stations_to_drop))


# now RSK
print('see RSK ... current removals: %d' % len(lst_stations_to_drop))
df_to_group_999 = df_climate[df_climate.RSK == -999][['STATIONS_ID', 'RSK']]
df_grouped_999 = df_to_group_999.groupby(['STATIONS_ID'])['RSK'].agg(['count','mean','max','min'])
ls = list(df_grouped_999[df_grouped_999['count'] > dwdpara.station_data_max_errors].index.values)
lst_stations_to_drop = lst_stations_to_drop + ls
lst_stations_to_drop = list(set(lst_stations_to_drop))
print(lst_stations_to_drop)
print(len(lst_stations_to_drop))


# now RSKF
print('see RSKF ... current removals: %d' % len(lst_stations_to_drop))
df_to_group_999 = df_climate[df_climate.RSKF == -999][['STATIONS_ID', 'RSKF']]
df_grouped_999 = df_to_group_999.groupby(['STATIONS_ID'])['RSKF'].agg(['count'])
ls = list(df_grouped_999[df_grouped_999['count'] > dwdpara.station_data_max_errors].index.values)
lst_stations_to_drop = lst_stations_to_drop + ls
lst_stations_to_drop = list(set(lst_stations_to_drop))
print(lst_stations_to_drop)
print(len(lst_stations_to_drop))

"""# now UPM
print('see UPM ... current removals: %d' % len(lst_stations_to_drop))
df_to_group_999 = df_climate[df_climate.UPM == -999][['STATIONS_ID', 'UPM']]
df_grouped_999 = df_to_group_999.groupby(['STATIONS_ID'])['UPM'].agg(['count'])
ls = list(df_grouped_999[df_grouped_999['count'] > 5].index.values)
lst_stations_to_drop = lst_stations_to_drop + ls
lst_stations_to_drop = list(set(lst_stations_to_drop))
print(lst_stations_to_drop)
print(len(lst_stations_to_drop))

# now VPM
print('see VPM ... current removals: %d' % len(lst_stations_to_drop))
df_to_group_999 = df_climate[df_climate.VPM == -999][['STATIONS_ID', 'VPM']]
df_grouped_999 = df_to_group_999.groupby(['STATIONS_ID'])['VPM'].agg(['count'])
ls = list(df_grouped_999[df_grouped_999['count'] > 5].index.values)
lst_stations_to_drop = lst_stations_to_drop + ls
lst_stations_to_drop = list(set(lst_stations_to_drop))
print(lst_stations_to_drop)
print(len(lst_stations_to_drop))

# now PM
print('see PM ... current removals: %d' % len(lst_stations_to_drop))
df_to_group_999 = df_climate[df_climate.PM == -999][['STATIONS_ID', 'PM']]
df_grouped_999 = df_to_group_999.groupby(['STATIONS_ID'])['PM'].agg(['count'])
ls = list(df_grouped_999[df_grouped_999['count'] > 5].index.values)
lst_stations_to_drop = lst_stations_to_drop + ls
lst_stations_to_drop = list(set(lst_stations_to_drop))
print(lst_stations_to_drop)
print(len(lst_stations_to_drop))

# now SDK
print('see SDK ... current removals: %d' % len(lst_stations_to_drop))
df_to_group_999 = df_climate[df_climate.SDK == -999][['STATIONS_ID', 'SDK']]
df_grouped_999 = df_to_group_999.groupby(['STATIONS_ID'])['SDK'].agg(['count'])
ls = list(df_grouped_999[df_grouped_999['count'] > 5].index.values)
lst_stations_to_drop = lst_stations_to_drop + ls
lst_stations_to_drop = list(set(lst_stations_to_drop))
print(lst_stations_to_drop)"""

#path = './data/test/df_climate.csv'
#df_climate[(df_climate.STATIONS_ID==idfix)].to_csv(path, sep=';', decimal=',')
#list(df.index.values) 

df_result = df_climate[~df_climate['STATIONS_ID'].isin(lst_stations_to_drop)]
print('climate data remaining:', df_climate.shape)

print(type(df_result))
print(type(df_climate))
print(type(lst_stations_to_drop))
mfilter = ~df_climate['STATIONS_ID'].isin(lst_stations_to_drop)
print(df_climate[mfilter].shape)

# remove stations which do not provide the full set of data
df_grouped = df_climate.groupby(['STATIONS_ID'])['MESS_DATUM'].agg(['nunique'])
ls = list(df_grouped[df_grouped['nunique']<550].index.values)
lst_stations_to_drop = lst_stations_to_drop + ls
lst_stations_to_drop = list(set(lst_stations_to_drop))

#print(df_grouped)

lst_stations_to_drop.sort()
path = dwdpara.wai_data_excluded_stations_list
pd.DataFrame(lst_stations_to_drop, columns=['STATIONS_ID']).to_csv(path, \
            sep=';', index=False)
