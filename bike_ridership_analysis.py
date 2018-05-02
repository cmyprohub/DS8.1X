#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 08:58:11 2018

@author: $?^^@
"""

from datascience import *
import numpy as np

#%matplotlib inline


import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

#Loading trip data to a table 
data = "https://s3.amazonaws.com/fordgobike-data/2017-fordgobike-tripdata.csv"
trip = Table.read_table(data)
trip.labels


#Filtering out trips below 30 mins
commute = trip.where('duration_sec', are.below(1800))
commute.hist('duration_sec', unit='Second') #histogram

#Binning
commute.hist('duration_sec', bins=60, unit='Second')

#Using group to identify the most highly used Start Station
starts = commute.group('start_station_name').sort('count', descending=True)
starts

#group/pivot methods to classify the rentals by both Start Station and End Station

commute.group(['start_station_name', 'end_station_name'])

commute.pivot('start_station_name', 'end_station_name')

'''use pivot to find the shortest time of the rides between Start and End Stations.
 Here pivot has been given Duration as the optional values argument, and min as the 
 function for values in each cell.
'''
commute.pivot('start_station_name', 'end_station_name', 'duration_sec', min)

'''The table stations contains geographical information about each bike station,
 including latitude, longitude, and a "landmark" which is the name of the city where 
 the station is located.
'''
stations = Table.read_table('station.csv')
stations


#Station locations in a map
Marker.map_table(stations.select('lat', 'long', 'name'))

#Only SF station, representy by green circles
sf = stations.where('landmark', are.equal_to('San Francisco'))
sf_map_data = sf.select('lat', 'long', 'name')
Circle.map_table(sf_map_data, color='green', radius=200)

#Different cities by color
cities = stations.group('landmark').relabeled('landmark', 'city')
cities

colors = cities.with_column('color', make_array('blue', 'red', 'green', 'orange', 'purple'))
colors

#join stations and colors by landmark, and then select the columns we need to draw a map
joined = stations.join('landmark', colors, 'city')
colored = joined.select('lat', 'long', 'name', 'color')
Marker.map_table(colored)

#To see where most of the bike rentals originate, let's identify the start stations:
starts = commute.group('start_station_name').sort('count', descending=True)
starts


#include the geographical data needed to map these stations, by first joining starts with stations:
station_starts = stations.join('name', starts, 'start_station_name')
station_starts

'''
extract just the data needed for drawing our map,
 adding a color and an area to each station. The area is 1000 times the count of 
 the number of rentals starting at each station, where the constant 1000 was chosen 
 so that the circles would appear at an appropriate scale on the map.
'''
starts_map_data = station_starts.select('lat', 'long', 'name').with_columns(
    'color', 'blue',
    'area', station_starts.column('count') * 1000
)
starts_map_data.show(3)
Circle.map_table(starts_map_data)




