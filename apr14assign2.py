#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 15:32:50 2023

@author: colinwelty
"""
import matplotlib.pyplot as plt
from cartopy import config
import cartopy.crs as ccrs
import cartopy.feature as cfeature


fig = plt.figure(figsize=(12, 12))

plt.rcParams.update({'font.size': 22})


bx = plt.axes(projection=ccrs.PlateCarree())

#now for figure 2
#ax.set_extent = ([-97.67660000000001, -96.32104523100001, 17.2301484511245, 28.766899999999502])
bx.set_extent([-80.4, -79.45, 26.20, 27.6], crs=ccrs.PlateCarree())
# set a margin around the data
bx.set_xmargin(0.05)
bx.set_ymargin(0.10)

# add the image. Because this image was a tif, the "origin" of the image is in the
# upper left corner
resol = '10m'

land = cfeature.NaturalEarthFeature('physical', 'land', scale=resol, facecolor=cfeature.COLORS['land'])
bx.add_feature(land, facecolor='gray')
bx.coastlines(resolution='10m', color='black', linewidth=2)

bx.text(-80, 27.523, 'b. Irma', weight = 'bold', fontsize = 40)
bx.text(-80.3, 26.22, '10 km', weight = 'bold', fontsize = 20)
# mark a known place to help us geo-locate ourselves
bx.plot(-80.36, 27.49, 'o', markersize=20, markerfacecolor='maroon', transform=ccrs.Geodetic())
bx.text(-80.31, 27.49, 'Fort Pierce', color = 'maroon', transform=ccrs.Geodetic())

bx.plot(-80.09, 26.68, 'o', markersize=20, markerfacecolor='green', transform=ccrs.Geodetic())
bx.text(-80.05, 26.68, 'West Palm Beach', color = 'green', transform=ccrs.Geodetic())

bx.plot(-80.24, 27.35, 'ro', markersize=20, transform=ccrs.Geodetic())
bx.text(-80.2, 27.35,'St. Lucie Power Plant', color = 'red', transform=ccrs.Geodetic())

bx.plot(-80.06, 26.89, 'o', markersize=20, markerfacecolor='purple',transform=ccrs.Geodetic())
bx.text(-80.02, 26.89, 'Juno Beach', color = 'purple', transform=ccrs.Geodetic())

bx.plot(-80.03, 26.61, 'o', markersize=20, markerfacecolor='blue', transform=ccrs.Geodetic())
bx.text(-80.0, 26.61, 'Lake Worth', color = 'blue', transform=ccrs.Geodetic())

bx.plot(-80.12, 26.29, 'o', markersize=20, markerfacecolor='orange', transform=ccrs.Geodetic())
bx.text(-80.08, 26.29, 'Deerfield Beach', color = 'orange', transform=ccrs.Geodetic())

gl = bx.gridlines(crs=ccrs.PlateCarree(), draw_labels=False, linewidth=2, color='gray', alpha=0.5, linestyle='--')



fig.savefig('reproducedfigure2.png')
plt.show()
