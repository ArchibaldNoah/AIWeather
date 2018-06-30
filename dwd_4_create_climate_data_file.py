#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 21:32:42 2017
<Step 4>

@author: Developer
"""

import dwd_parameter as dwdpara
import pandas as pd

station_list_file = open(dwdpara.wai_data_station_list,'r')

# STATIONS_ID; MESS_DATUM; QN_3; FX; FM; QN_4; RSK; RSKF; SDK  \
# SHK_TAG; NM; VPM; PM; TMK; UPM; TXK; TNK; TGK; eor

header = ['STATIONS_ID','MESS_DATUM','QN_3','FX','FM','QN_4','RSK','RSKF','SDK', \
'SHK_TAG','NM','VPM','PM','TMK','UPM','TXK','TNK','TGK','eor']

# create empty dataframe
df_dwd_climate_data = pd.DataFrame(columns=header)
#print(df_dwd_climate_data.dtypes)
fileCounter = 0


for line in station_list_file:
    #get id
    s = line[9:14]
    # build file name
    try:
        fileName = dwdpara.wai_name_climate_use_data + s + ".txt"
        dataFileLocator = dwdpara.path_work_data + fileName
        df_input = pd.read_csv(dataFileLocator,sep=';')
        #df_input.columns=header
        #df.rename(columns={'oldName1': 'newName1', 'oldName2': 'newName2'}, inplace=True)
        df_input.rename(columns = {'  FX':'FX','  FM':'FM',' RSK':'RSK', \
                                   ' SDK':'SDK','  NM':'NM',' VPM':'VPM', \
                                   '  PM':'PM',' TMK':'TMK',' UPM':'UPM', \
                                   ' TXK':'TXK',' TNK':'TNK',' TGK':'TGK'}, inplace=True)
        #print(df_input.dtypes)
        
        df_dwd_climate_data = df_dwd_climate_data.append(df_input,ignore_index=True)
        #print(df_dwd_climate_data)
        #print(df_dwd_climate_data.dtypes)

        fileCounter = fileCounter + 1 
        if fileCounter >= dwdpara.wai_station_count_limit:
            break
    except Exception as e:
        print('Failed to open climate data file: ' + str(e))
        pass
    
#print(df_dwd_climate_data[df_dwd_climate_data.PM > -990]['STATIONS_ID'].drop_duplicates())
#print(df_dwd_climate_data.shape)
# fix data
# transform RSKF to integer
df_dwd_climate_data['RSKF'] = df_dwd_climate_data['RSKF'].astype(str).astype(int)
#print(df_dwd_climate_data.dtypes)
df_dwd_climate_data.to_pickle(dwdpara.path_use_data + \
                              dwdpara.wai_name_climate_final_data)

print(df_dwd_climate_data.dtypes)