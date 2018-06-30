#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 12:49:46 2018

@author: Developer
"""

import pandas as pd

import dwd_parameter as para

imports = ['20180518','20180330','20171008']
starts = [20160331, 20160926, 20161116]

locator = '../data/' + '20171008' + '/use_data/' + para.wai_name_climate_final_data
df_in = pd.read_pickle(locator)
print(df_in.dtypes, df_in.shape)
print(df_in.MESS_DATUM.min(), df_in.MESS_DATUM.max())
df_all = df_in[df_in.MESS_DATUM < starts[1]]
print('all:', df_all.MESS_DATUM.min(), df_all.MESS_DATUM.max())

locator = '../data/' + '20180330' + '/use_data/' + para.wai_name_climate_final_data
df_in = pd.read_pickle(locator)
print(df_in.dtypes, df_in.shape)
print(df_in.MESS_DATUM.min(), df_in.MESS_DATUM.max())

df_all = pd.concat([df_all, df_in[df_in.MESS_DATUM < starts[2]]])
print('all:',df_all.MESS_DATUM.min(), df_all.MESS_DATUM.max())

locator = '../data/' + '20180518' + '/use_data/' + para.wai_name_climate_final_data
df_in = pd.read_pickle(locator)
print(df_in.dtypes, df_in.shape)
print(df_in.MESS_DATUM.min(), df_in.MESS_DATUM.max())

df_all = pd.concat([df_all, df_in])
print(df_all.MESS_DATUM.min(), df_all.MESS_DATUM.max())
df_all.reset_index()
df_all.to_pickle(para.path_use_data + \
                              para.wai_name_climate_final_all_data)

print(df_all.head())