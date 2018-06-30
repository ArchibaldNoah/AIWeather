#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 07:17:14 2017

<STEP 1>
Read data from dwd weather stations posted under <climate / recent>
Zip files will be stored in zip folder for further processing
Next step <extract_data>

@author: J&L
"""
import os
import urllib
import dwd_parameter

stations = []

file = open(dwd_parameter.wai_data_station_list,'r')

for line in file:
    #print(line[9:14], line[0:8])
    stations.append(line[9:14])
    print(line[9:14])

# now read data for stations from dwd ftp server and store to data folder
outPath = dwd_parameter.path_download + '/'

fileCounter = 0

for s in stations:
    print('read data from station: %s' % s)
    inFileName = r"tageswerte_KL_" + s + r"_akt.zip"
    print('read file %s' % inFileName)
    theURL = 'ftp://' + dwd_parameter.dwd_ftp_site+ \
                        dwd_parameter.dwd_ftp_directory_climate_kl_recent
                        
    readFile = theURL + inFileName
    outFile = outPath + inFileName
    print('File No.: %d' % fileCounter)
    if os.path.isfile(outFile) == False:
        names, headers = urllib.request.urlretrieve(readFile, outFile)
        print('write file to %s' % outFile)
    else: 
        print('--- File already exists ---')
    fileCounter = fileCounter+1
    if fileCounter >= dwd_parameter.wai_station_count_limit:
        break
 
#names, headers = urllib.request.urlretrieve(theURL)