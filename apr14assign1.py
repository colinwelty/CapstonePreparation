#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 10:34:01 2023

@author: colinwelty
"""

import os
import matplotlib.pyplot as plt

from cartopy import config
import cartopy.crs as ccrs
import cartopy.feature as cfeature


fig = plt.figure(figsize=(12, 12))

# get the path of the file. It can be found in the repo data directory.

plt.rcParams.update({'font.size': 22})


ax = plt.axes(projection=ccrs.PlateCarree())
#ax.set_extent = ([-97.67660000000001, -96.32104523100001, 17.2301484511245, 28.766899999999502])
ax.set_extent([-97.18, -96.75, 27.70, 28.25], crs=ccrs.PlateCarree())
# set a margin around the data
ax.set_xmargin(0.05)
ax.set_ymargin(0.10)

# add the image. Because this image was a tif, the "origin" of the image is in the
# upper left corner
resol = '10m'

land = cfeature.NaturalEarthFeature('physical', 'land', scale=resol, facecolor=cfeature.COLORS['land'])
ax.add_feature(land, facecolor='gray')
ax.coastlines(resolution='10m', color='black', linewidth=2)

ax.text(-97.14, 28.223, 'a. Harvey', weight = 'bold', fontsize = 40)
ax.text(-97, 27.723, '5 km', weight = 'bold', fontsize = 20)
# mark a known place to help us geo-locate ourselves
ax.plot(-97.05, 28.08, 'o', markersize=20, markerfacecolor='maroon', transform=ccrs.Geodetic())
ax.text(-97.035, 28.05, 'Rockport Research', color = 'maroon', transform=ccrs.Geodetic())

ax.plot(-97.05, 28.02, 'o', markersize=20, markerfacecolor='green', transform=ccrs.Geodetic())
ax.text(-97.035, 28.01, 'Rockport', color = 'green', transform=ccrs.Geodetic())

ax.plot(-97.03, 28.122, 'ro', markersize=20, transform=ccrs.Geodetic())
ax.text(-97.01, 28.12, 'Copano East', color = 'red', transform=ccrs.Geodetic())

ax.plot(-97.02, 28.11, 'o', markersize=20, markerfacecolor='purple',transform=ccrs.Geodetic())
ax.text(-97.01, 28.09, 'Copano Bay', color = 'purple', transform=ccrs.Geodetic())

ax.plot(-97.039, 27.856, 'o', markersize=20, markerfacecolor='blue', transform=ccrs.Geodetic())
ax.text(-97.02, 27.84, 'Port Aransas Sent.', color = 'blue', transform=ccrs.Geodetic())

ax.plot(-97.053, 27.829302, 'o', markersize=20, markerfacecolor='orange', transform=ccrs.Geodetic())
ax.text(-97.037, 27.81, 'Port Aransas', color = 'orange', transform=ccrs.Geodetic())

gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=False, linewidth=2, color='gray', alpha=0.5, linestyle='--')
fig.savefig('reproducedfigure.png')
plt.show()

