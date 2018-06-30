#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 18:19:36 2017

<STEP 3>
Create stations file which contains the actual entries of
Stations_id;Stationshoehe;Geogr.Breite;Geogr.Laenge;von_datum;bis_datum;Stationsname

@author: J&L
"""

import dwd_parameter as dwdpara
import pandas as pd

#Stations_id;Stationshoehe;Geogr.Breite;Geogr.Laenge;von_datum;bis_datum;Stationsname
header = ['STATION_ID', 'HEIGHT', 'LATITUDE', 'LONGITUDE', 'NAME']
df_station_data = pd.DataFrame(columns=header)
#df_station_data.set_index('STATION_ID',inplace=True)
#print(df_station_data + '\n')


station_list_file = open(dwdpara.wai_data_station_list,'r')

fileCounter = 0

for line in station_list_file:
    #get id
    s = line[9:14]
    # build file name
    fileName = "Metadaten_Geographie_" + s + ".txt"
    metaFileLocator = dwdpara.path_work_data + fileName
    print('get file: %s' % metaFileLocator)
    metaFile = open(metaFileLocator,'r', encoding = "ISO-8859-1")
    for aLine in metaFile:
        entries = aLine.split(';')
        # identify currently valid entry 
        if entries[5].startswith(' '):  
            # if current valid, add to stations dataframe
            df_add = pd.DataFrame([[entries[0],
                                  entries[1],
                                  entries[2],
                                  entries[3],
                                  entries[6]]],columns=header)
            df_station_data = df_station_data.append(df_add,ignore_index=True)
    metaFile.close()

    fileCounter = fileCounter + 1 
    if fileCounter >= dwdpara.wai_station_count_limit:
        break
    
#print(df_station_data)
path = dwdpara.path_meta_data + 'stations.pickle' 
df_station_data.to_pickle(path)
