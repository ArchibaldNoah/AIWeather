#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 06:17:34 2017

DEPRECATED
Weather prediction with machine learning

Read data from url

@author: J&L
"""

import urllib
from contextlib import closing

import dwd_parameter

#for i in range(100):
#inFile = r"tageswerte_KL_" + str(i).zfill(5) + r"_akt.zip"
#print(inFile)

theURL = dwd_parameter.dwd_ftp_site+dwd_parameter.dwd_ftp_directory_climate_kl_recent

outPath = r"/Users/Developer/Development/Python/Data/"
theFile = outPath # + inFile
 
names, headers = urllib.request.urlretrieve(theURL)

for s in headers:
    print(s)
# unzip archive
#theZipFile = zipfile.ZipFile(theFile, mode="r")



#MiB = 2**20 # mebibyte
"""
with closing(zipfile.ZipFile(theFile)) as zfile:
    for info in zfile.infolist():
        #if info.filename.endswith('.txt') and 0 < info.file_size <= 3*MiB:
        #Metadaten_Geographie_00044
        if info.filename.endswith('.txt') and \
                                 (info.filename.startswith('produkt') or \
                                  info.filename.startswith('Metadaten_Geographie')):
            zfile.extract(info, path=outPath)
"""         
            
"""
theZipFile.extractall()
theZipFile.close()

#f.close()
"""