#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 08:34:13 2017

<STEP 2>
Extract zip archives downloaded from dwd open data site

@author: J&L
"""

import os
import zipfile
from contextlib import closing

import dwd_parameter

#for i in range(100):
#inFile = r"tageswerte_KL_" + str(i).zfill(5) + r"_akt.zip"
#print(inFile)

stations = []
outPath = dwd_parameter.path_work_data

file = open(dwd_parameter.wai_data_station_list,'r')

fileCounter = 0

for line in file:
    s = line[9:14]
    fileName = "tageswerte_KL_" + s + "_akt.zip"
    zipFilePath = dwd_parameter.path_download + fileName
    print('get zip-File:  %s ' % zipFilePath)
    
    #theZipFile = zipfile.ZipFile(zipFilePath)
    
    fileCounter = fileCounter + 1
    with closing(zipfile.ZipFile(zipFilePath)) as zfile:
        for info in zfile.infolist():
            if info.filename.endswith('.txt') and \
                                     (info.filename.startswith('produkt') or \
                                      info.filename.startswith('Metadaten_Geographie')):
                zfile.extract(info, path=outPath)
   
    if fileCounter >= dwd_parameter.wai_station_count_limit:
        break

#rename axtracted files produkt_klima_tag_20160208_20170810_00071.txt
print("Rename data in %s" % outPath)

for filename in os.listdir(outPath):
    if filename.startswith("produkt"):
        os.rename(outPath + filename, outPath + 'dwd_climate_recent_daily' + filename[35:])
        #print(outPath + 'dwd_climate_recent_daily' + filename[35:])
        
