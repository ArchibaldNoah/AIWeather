#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 14:43:24 2017

@author: Developer
"""
data_date = '20180518'

#ftp://ftp-cdc.dwd.de/pub/CDC/observations_germany/climate/daily/kl/recent/
dwd_ftp_site = 'ftp-cdc.dwd.de'
dwd_ftp_directory_climate_kl_recent = '/pub/CDC/observations_germany/climate/daily/kl/recent/'

# Path
path_root = '../data/' + data_date + '/'
path_meta_data = path_root + 'meta_data/'
path_work_data = path_root + 'work_data/'
path_use_data = path_root + 'use_data/'
path_download = path_root + 'download/'

# Weather AI data
wai_data_station_list = path_meta_data + '/station_id_list.txt'
wai_data_excluded_stations_list = path_meta_data + '/station_excluded_id_list.csv'
#wai_data_station_meta = '../data/' + data_date + '/meta/'
#wai_data_use_data = '../data/' + data_date + '/use_data/'
wai_station_count_limit = 507

# Weather AI names
wai_name_climate_use_data = 'dwd_climate_recent_daily_'
wai_name_climate_final_data = 'dwd_climate_recent_daily_0_all.pickle'
wai_name_climate_final_all_data = 'dwd_climate_recent_daily_1_all_combined.pickle'
wai_name_climate_clean_data = 'dwd_climate_recent_daily_2_all_clean.pickle'

# Target Station
wai_target_station = 6305

# Station rejection measurement deficiency limit
station_data_max_errors = 5
station_data_max_missing_dates = 10