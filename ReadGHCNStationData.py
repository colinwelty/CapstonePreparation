#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 22:22:33 2023

@author: kpegion
"""

#!/usr/bin/env python
# coding: utf-8

# ## NOAA National Center for Environmental Information (NCEI) Station Database
# The purpose of this Jupyter Notebook is to demonstrate how to read NCEI Station Data
#
# ## Where did the data come from?
# https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C00861
# * Click: NCEI Direct Download
# * Download: ghcnd_all.tar.gz (all the data)
# * Download: ghcnd-stations.txt (metadata)
# * `gunzip ghcnd_all.tar.gz`
# * `tar -xvf ghcnd_all.tar`
#
# ## Where is the data located on SoM Computers?
# `/data/class_data/GHCNv3/`
#
# ## What Files are there?
#
# ghcnd-stations.txt: this is a Fixed Width File, meaning that each column has a specified width.
#
#
# |Variable     | Columns |  Type      |
# |-------------|---------|------------|
# |ID           |  1-11   | Character  |
# |LATITUDE     | 13-20   | Real       |
# |LONGITUDE    | 22-30   | Real       |
# |ELEVATION    | 32-37   | Real       |
# |STATE        | 39-40   | Character  |
# |NAME         | 42-71   | Character  |
# |GSN FLAG     | 73-75   | Character  |
# |HCN/CRN FLAG | 77-79   | Character  |
# |WMO ID       | 81-85   | Character  |
#
#
# III. FORMAT OF DATA FILES (".dly" FILES)
#
# Each ".dly" file contains data for one station.  The name of the file
# corresponds to a station's identification code.  For example, "USC00026481.dly"
# contains the data for the station with the identification code USC00026481).
#
# Each record in a file contains one month of daily data.  The variables on each
# line include the following:
#
# ------------------------------
# Variable   Columns   Type
# ------------------------------
# ID            1-11   Character
# YEAR         12-15   Integer
# MONTH        16-17   Integer
# ELEMENT      18-21   Character
# VALUE1       22-26   Integer
# MFLAG1       27-27   Character
# QFLAG1       28-28   Character
# SFLAG1       29-29   Character
# VALUE2       30-34   Integer
# MFLAG2       35-35   Character
# QFLAG2       36-36   Character
# SFLAG2       37-37   Character
#   .           .          .
#   .           .          .
#   .           .          .
# VALUE31    262-266   Integer
# MFLAG31    267-267   Character
# QFLAG31    268-268   Character
# SFLAG31    269-269   Character
# ------------------------------
#
import pandas as pd
import numpy as np
import seaborn as sns


# ---------- Define Some functions to make our code easier to read ----------------


def get_ghcnd_stations_info():
    widths=[11,9,10,8,2,30,5,5,8]
    cols=['ID', 'Latitude', 'Longitude', 'Elevation','State','Name','GSN Flag','HCN/CRN Flag','WMO ID']
    return widths,cols

def get_ghcnd_stations_data():
    widths= [11,4,2,4,
             5,1,1,1,
             5,1,1,1,
             5,1,1,1,
             5,1,1,1,
             5,1,1,1,
             5,1,1,1,
             5,1,1,1,
             5,1,1,1,
             5,1,1,1,
             5,1,1,1,
             5,1,1,1,
             5,1,1,1,
             5,1,1,1,
             5,1,1,1,
             5,1,1,1,
             5,1,1,1,
             5,1,1,1,
             5,1,1,1,
             5,1,1,1,
             5,1,1,1,
             5,1,1,1,
             5,1,1,1,
             5,1,1,1,
             5,1,1,1,
             5,1,1,1,
             5,1,1,1,
             5,1,1,1,
             5,1,1,1,
             5,1,1,1,
             5,1,1,1,
             5,1,1,1]
    cols=['ID','Year','Month','Element',
           '1','MFlag1','QFlag1','SFFlag1',
           '2','MFlag2','QFlag2','SFFlag2',
           '3','MFlag3','QFlag3','SFFlag3',
           '4','MFlag4','QFlag4','SFFlag4',
           '5','MFlag5','QFlag5','SFFlag5',
           '6','MFlag6','QFlag6','SFFlag6',
           '7','MFlag7','QFlag7','SFFlag7',
           '8','MFlag8','QFlag8','SFFlag8',
           '9','MFlag9','QFlag9','SFFlag9',
           '10','MFlag10','QFlag10','SFFlag10',
           '11','MFlag11','QFlag11','SFFlag11',
           '12','MFlag12','QFlag12','SFFlag12',
           '13','MFlag13','QFlag13','SFFlag13',
           '14','MFlag14','QFlag14','SFFlag14',
           '15','MFlag15','QFlag15','SFFlag15',
           '16','MFlag16','QFlag16','SFFlag16',
           '17','MFlag17','QFlag17','SFFlag17',
           '18','MFlag18','QFlag18','SFFlag18',
           '19','MFlag19','QFlag19','SFFlag19',
           '20','MFlag20','QFlag20','SFFlag20',
           '21','MFlag21','QFlag21','SFFlag21',
           '22','MFlag22','QFlag22','SFFlag22',
           '23','MFlag23','QFlag23','SFFlag23',
           '24','MFlag24','QFlag24','SFFlag24',
           '25','MFlag25','QFlag25','SFFlag25',
           '26','MFlag26','QFlag26','SFFlag26',
           '27','MFlag27','QFlag27','SFFlag27',
           '28','MFlag28','QFlag28','SFFlag28',
           '29','MFlag29','QFlag29','SFFlag29',
           '30','MFlag30','QFlag30','SFFlag30',
           '31','MFlag31','QFlag31','SFFlag31']
    return widths, cols

def feettometers(x_feet):
    return x_feet/3.281 
    
#----------------------   Main Program Starts Here ----------------------------------
#  1. Find the station ID(s) for the station(s) we want to work with

# Read in the file telling us about all the stations and their IDs
station_fname='/Users/colinwelty/Desktop/Python/ghcnd-stations.txt'

# Get the info about the column width and names for the stations information file
station_info_widths,station_info_cols=get_ghcnd_stations_info()

# Read the Station Information File
station_names_df=pd.read_fwf(station_fname,header=None,widths=station_info_widths)
print(station_names_df.head())

# Assign the column names for this file
station_names_df.columns =station_info_cols

# We now have a pandas.DataFrame of the station information, including station IDs
print(station_names_df.head())

# Now extractinformation from this DataFrame to get the station ID(s) for the stations we are interested in
# Example: Find stations in CO with elevation above 12000 ft
high_elevation=feettometers(12000)
co_mtn_stations_df=station_names_df.loc[(station_names_df['State']=='CO') & (station_names_df['Elevation']>=high_elevation)]
print(co_mtn_stations_df)

# Get the station ID for this station
station_id=co_mtn_stations_df['ID'].values[0]
print(station_id)

# 2. Now that we have the station Id, we  know which file to open and read for this station
fname='/Users/colinwelty/Desktop/Python/'+station_id+'.dly'
print(fname)

# Get the width and column information for the station data file
station_data_widths,station_data_cols=get_ghcnd_stations_data()

# Read the station data file and assign column names
station_df=pd.read_fwf(fname,header=None,widths=station_data_widths)
station_df.columns=station_data_cols
print(station_df.head())

# 3. Now we can extract whatever data we want from the station data
# Example: Extract the TMAX data for this station over all times and plot as a time series


# Extract the TMAX data as a time series
ts_df=station_df.loc[station_df['Element']=='TMAX'][np.arange(1,32).astype(str)]
print(ts_df.head())

# The data format is challenging with a column for each month of data.  It will be difficult to tell a plotting function
# what goes on the x-axis and what goes on the y-axis.  We want the x-axis to be DATE and the y-axis to be TMAX, so 
# we need to re-arrange this data where the columns are [ DATE, TMAX] and each row representes a different date.  
# This will make it easier for us to tell a plotting program that df['DATE'] is the x-axis and df['TMAX'] is the y-axis

df_list=[]
new_data=[]
monthlystrs=[]

for i,y in enumerate(range(len(ts_df))): # Loop over all rows
    for j,d in enumerate(ts_df.columns): # Loop over all columns
    
        # Create a date string to go in the first column
        monthlystr=str(station_df['Year'][i])+'-'+str(station_df['Month'][i])+'-'+d
        monthlystrs.append(monthlystr)
        
        # Get the data values that go in the second colunn
        new_data.append(ts_df.iloc[i,j]) 

# Rows and Colunns are reversed, so fix this        
new_df=pd.DataFrame([monthlystrs,new_data]).transpose()

# Assign the column names now that we have the right columns
new_df.columns=['Date','TMAX']

# Take care of missing data coded as 9999 and replace it with not a number (nan).
new_df=new_df.replace(-9999, np.nan)

# Drop all rows with TMAX == nan
new_df=new_df.dropna(axis='rows')

# Convert data from 10th of a degree C to degrees C
new_df['TMAX']=new_df['TMAX']*0.1
print(new_df.head())


# Plot the data using the seaborn lineplot
# Seaborn is a package for plotting pandas.DataFrame objects
# The difference from matplotlib is that it knows how to interpret a DataFrame, so 
# it is often easier 
sns.lineplot(data =new_df)









