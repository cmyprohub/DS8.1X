#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 15:32:28 2018

@author: Suma
"""
#Importing libraries
from datascience import *
from matplotlib import pyplot as plots
import numpy as np
import urllib.request
from pandas import *

#Loading data into a table

data = 'http://www2.census.gov/programs-surveys/popest/datasets/2010-2015/national/asrh/nc-est2015-agesex-res.csv'

# A copy can be accessed here in case census.gov moves the file:
# data = 'http://inferentialthinking.com/notebooks/nc-est2015-agesex-res.csv'

# Documentation is online here:
# https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2010-2015/nc-est2015-agesex-res.pdf

full = Table.read_table(data)
full

#Selecting only required columns from the table into a new table
partial = full.select('SEX', 'AGE', 4, 9)
partial

#Relabelling last 2 columns
us_pop = partial.relabeled(2, '2010').relabeled(3, '2015')
us_pop


#Formatting the number columns
us_pop.set_format([2,3],NumberFormatter)

#Population difference between 2015 and 2010
us_pop.column(3) - us_pop.column(2)

#Calculating change %
change = us_pop.column('2015') - us_pop.column('2010')
census = us_pop.with_columns(
    'Change', change,
    'Total Growth', change / us_pop.column('2010')
)
census.set_format('Change', NumberFormatter)
census.set_format('Total Growth', PercentFormatter)
census.sort('Change', descending=True)

#Adding up 2010 population
sum(census.column('2010')) 


#If sorted descending by 'Change' column, First row will be the total population
everyone = census.sort('Change', descending = 'True').row(0)
everyone
type(everyone)

#After dropping 2010 row from the us_pop table,create a 2015 only table, having only ages below 999
#(means total pop rows are removed) and valid gender values (not 0)
us_pop_2015 = us_pop.drop('2010').where('AGE', are.below(999)).where('SEX', are.above(0))
us_pop_2015

#Creating separate array for 2015 males
#creating separate array for 2015 females, relabelling it to 'Females' colimn and adding the males column to it
#Sex column is not needed and is being dropped
males = us_pop_2015.where('SEX', 1).column('2015')
by_sex = us_pop_2015.where('SEX', 2).drop('SEX').relabeled('2015', 'Females').with_column('Males', males)
by_sex.set_format('Males', NumberFormatter)

#Visualizing
by_sex.plot(0)

by_age = census.where('SEX', 0).drop('SEX').where('AGE', are.between(0, 100))
by_age

by_age.plot(0, 2)

by_age.plot(0, 3)

by_age.select(0, 1, 2).plot(0)

by_age.select(0, 1, 2).plot(0, overlay=False)

#column names
by_age.labels

by_age.plot(0, 3)

by_age.sort(3, descending=True)

2010 - 68

2015 - 68
