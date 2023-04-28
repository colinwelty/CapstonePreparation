#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 20:35:11 2023

@author: colinwelty
"""
import wradlib as wrl
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt 
import netCDF4 as nc
import xarray as xr
import pyart as py


fn = '/Users/colinwelty/Desktop/Python/sr2/rhi/cfrad.20170825_210417.660_to_20170825_210502.743_CPOLRVP_MATT_RHI_RHI.nc'
ds = xr.open_dataset(fn)

outdict = wrl.io.read_generic_netcdf(ds)




















#print(ds)
print(ds.variables.keys())

# var_names = ds.variables.keys()
# print("Variable Names:")
# for var_name in var_names:
#     print(var_name)
    
# print(ds['DBZ'])


# Zdr= (ds['ZDR'])
# print(Zdr)
#create the plot using matplotlib
# fig,ax = plt.subplots()
# mpl.rcParams['font.size'] = 12
# plt.contour(ds['ZDR'][0,:])
# plt.xlabel('X Label')
# plt.ylabel('Y Label')
# plt.title('Radar Reflectivity Contour Plot')
# plt.colorbar(label='Radar Reflectivity (dBZ)')


# fig.savefig('testradar.png')
# plt.clf()