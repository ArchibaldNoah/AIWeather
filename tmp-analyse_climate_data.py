#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 11:41:12 2017

@author: Developer
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import dwd_parameter as dwdpara

# get station list and add positions to map
path = dwdpara.path_use_data + dwdpara.wai_name_climate_final_data
df_climate = pd.read_pickle(path)

#print(df_stations.sort_values(by=['LATITUDE']))
print(df_climate.dtypes)
print(df_climate.shape)

print('Stationen gesamt: %d' % df_climate['STATIONS_ID'].drop_duplicates().shape)
print('Stationen mit Tagesmitteltemperatur: %d' % df_climate[df_climate.TMK>-998]['STATIONS_ID'].drop_duplicates().shape)
print('Stationen mit mittlerem Luftdruck: %d' % df_climate[df_climate.PM>-998]['STATIONS_ID'].drop_duplicates().shape)
print('Stationen mit Tageshöchsttemperatur: %d' % df_climate[df_climate.TXK>-998]['STATIONS_ID'].drop_duplicates().shape)
print('Stationen mit Tagesniedrigsttemperatur: %d' % df_climate[df_climate.TNK>-998]['STATIONS_ID'].drop_duplicates().shape)
print('Stationen mit mittlerem Dampfdruck: %d' % df_climate[df_climate.VPM>-998]['STATIONS_ID'].drop_duplicates().shape)
print('Stationen mit Niederschlagshöhe: %d' % df_climate[df_climate.RSK>-998]['STATIONS_ID'].drop_duplicates().shape)
print('Stationen mit Niederschlagsform: %d' % df_climate[df_climate.RSKF>-998]['STATIONS_ID'].drop_duplicates().shape)
print('Stationen mit Luftfeuchtigkeit: %d' % df_climate[df_climate.UPM>-998]['STATIONS_ID'].drop_duplicates().shape)
print('Stationen mit Abdeckung: %d' % df_climate[df_climate.NM>-998]['STATIONS_ID'].drop_duplicates().shape)
print('Stationen mit Tagesmittel Windgeschw.: %d' % df_climate[df_climate.FM>-998]['STATIONS_ID'].drop_duplicates().shape)

#print(df_climate[df_climate.STATIONS_ID==1078])

x = df_climate[df_climate.STATIONS_ID==1078]['MESS_DATUM']
y = df_climate[df_climate.STATIONS_ID==1078]['TMK']


print(np.histogram(df_climate['RSK'], bins=[0, 1, 10, 20, 30, 100, 1000]))
print('Temperatur')
print(df_climate[df_climate.TMK==-999]['STATIONS_ID'].drop_duplicates())
print('Stationen mit irregulären Höchsttemperaturen %d: ' % df_climate[df_climate.TXK==-999]['STATIONS_ID'].drop_duplicates().shape)
print('Stationen mit irregulären Tiefsttemperaturen %d: ' % df_climate[df_climate.TNK==-999]['STATIONS_ID'].drop_duplicates().shape)
print('Stationen mit irregulären Niederschlagshöhen %d: ' % df_climate[df_climate.RSK==-999]['STATIONS_ID'].drop_duplicates().shape)
print('Stationen mit irregulären Niederschlagsform %d: ' % df_climate[df_climate.RSKF==-999]['STATIONS_ID'].drop_duplicates().shape)
print('Stationen mit irregulären Luftdruck %d: ' % df_climate[df_climate.PM==-999]['STATIONS_ID'].drop_duplicates().shape)

#Dampfdruck
filter_stations_not_eligible =  (df_climate.TMK == -999) | \
                            (df_climate.TXK == -999) | \
                            (df_climate.TNK == -999) | \
                            (df_climate.RSK == -999) | \
                            (df_climate.RSKF == -999) | \
                            (df_climate.UPM > -999) 
                            
print('all something bad stations %d: ' % df_climate[filter_stations_not_eligible]['STATIONS_ID'].drop_duplicates().shape)
#print(x)
#plt.plot(y)
#plt.show()
#print(df_climate[df_climate.TMK==-999]['STATIONS_ID'].drop_duplicates())
#print(df_climate[df_climate.TXK==-999]['STATIONS_ID'].drop_duplicates())
#print(df_climate[df_climate.TNK==-999]['STATIONS_ID'].drop_duplicates())
#print(df_climate[df_climate.VPM==-999]['STATIONS_ID'].drop_duplicates())
#print(df_climate[df_climate.UPM==-999]['STATIONS_ID'].drop_duplicates())
#print(df_climate[df_climate.RSK==-999]['STATIONS_ID'].drop_duplicates())
#print(df_climate[df_climate.RSKF==-999]['STATIONS_ID'].drop_duplicates())

print(df_climate[(df_climate.RSKF==-999) & (df_climate.STATIONS_ID == 73)])

