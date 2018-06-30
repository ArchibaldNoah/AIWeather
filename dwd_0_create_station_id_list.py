#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 14:06:49 2017

<STEP 0>
Generate station list from all files available at relevant dwd ftp folder
see: dwd_ftp_directory_climate_kl_recent

@author: Developer
"""

import ftplib
import datetime

import dwd_parameter as para


files = []
ids = []
sep = ";"
today = datetime.datetime.now()

#inPath = r"ftp://ftp-cdc.dwd.de/pub/CDC/observations_germany/climate/daily/kl/recent/"
ftp = ftplib.FTP(para.dwd_ftp_site)
ftp.login("anonymous", "")

try:
    files = ftp.nlst(para.dwd_ftp_directory_climate_kl_recent)
except:
    raise


for f in files:
    if 'tageswerte' in f:
        ids.append(f[68:-8])
        #print(today.strftime('%Y%m%d') + sep + f[68:-8],file=outfile)

print('Data files read: %d' % len(ids))  
outfile = open(para.wai_data_station_list, 'w')


for id in sorted(ids):
    print(today.strftime('%Y%m%d') + sep + id,file=outfile)
    
outfile.close()   
