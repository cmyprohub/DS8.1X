#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 15:19:27 2018

@author: Suma
"""
from datascience import *
import numpy as np

%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

all_cones = Table.read_table('cones.csv')
cones = all_cones.drop('Color').exclude(5)
cones

#Grouping by one column to get total counts
cones.group('Flavor')

#returns price list
cones.group('Flavor', list)

cones.group('Flavor', len)

cones.group('Flavor', min)

min(cones.where('Flavor', 'chocolate').column('Price'))

cones.group('Flavor', np.average)

#Function
def data_range(x):
    return max(x) - min(x)

cones.group('Flavor', data_range)

#Cross Classification
all_cones
all_cones.group('Flavor')

all_cones.group(['Flavor', 'Color'])

all_cones.group(['Flavor', 'Color'], max)

#Pivot tables
all_cones.group(['Flavor', 'Color'])

all_cones.pivot('Flavor', 'Color')   # pivot table, contingency table Col,row

all_cones.pivot('Color', 'Flavor')

all_cones.pivot('Color', 'Flavor', values = 'Price', collect = max) #max price in each category


