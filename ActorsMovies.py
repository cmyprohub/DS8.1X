#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 21:56:07 2018

@author: Suma
"""

from datascience import *
import numpy as np

%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

actors = Table.read_table('Actors.csv')
actors

actors = actors.relabeled(5, '#1 Movie Gross')
actors

actors.scatter(2, 1)

actors.labels

actors.select(2, 3, 5).scatter(0)

actors.where(5, are.above(800))

actors

actors.scatter(2, 3)

actors.where(2, are.below(10))

actors.where(2, are.above(60))

#movie data
top = Table.read_table('top_movies.csv')
top

top10 = top.take(np.arange(10))
top10.barh(0, 2)

studios = top.group('Studio')
studios

sum(studios.column(1))

studios.barh(0)

studios.sort(1, descending=True).barh(0)

#binning

top = Table.read_table('top_movies.csv')
top


age = 2017 - top.column('Year')

top = top.with_column('Age', age)
top

min(top.column('Age')), max(top.column('Age'))

my_bins = make_array(0, 5, 10, 15, 25, 40, 65, 100)

top.bin('Age', bins = my_bins)

sum(top.bin('Age', bins = my_bins).column(1))

top.bin('Age', bins = np.arange(0, 101, 25))

top.bin('Age', bins = np.arange(0, 60, 25))

top.where('Age', 50)

#Histograms
my_bins
top.bin('Age', bins = my_bins)
top.hist('Age', bins = my_bins, unit = 'Year')
top.hist('Age', bins = my_bins, unit = 'Year', normed = False)
top.hist('Age', bins = my_bins, unit = 'Year')
top.hist('Age', bins = np.arange(0, 110, 10), unit = 'Year')

#Density
top.bin('Age', bins = my_bins)
top.hist('Age', bins = my_bins, unit = 'Year')

