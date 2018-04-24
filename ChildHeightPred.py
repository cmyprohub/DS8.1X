#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 22:15:22 2018

@author: Suma
"""

from datascience import *
import numpy as np

%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

height = Table.read_table('galtonchildheight.csv').select(1, 2, 7).relabeled(2, 'child')
height.show(6)

#Histograms
height.hist('father', unit='inch')
height.hist('child', unit='inch')
height.hist(unit='inch', bins=np.arange(55, 80, 2))

#Table Manipulation
height

height.scatter(2)

height = height.with_column(
    'parent average', (height.column('mother') + height.column('father')) / 2
)
height


height.scatter('parent average', 'child')


height.scatter('parent average', 'child')
_ = plots.plot([67.5, 67.5], [50, 85], color='red', lw=2)
_ = plots.plot([68.5, 68.5], [50, 85], color='red', lw=2)


close_to_68 = height.where('parent average', are.between(67.5, 68.5))
close_to_68

close_to_68.column('child').mean()

#Functions
def predict_child(pa):
    close_points = height.where('parent average', are.between(pa - 0.5, pa + 0.5))
    return close_points.column('child').mean()   


predict_child(68)

predict_child(62)

# Apply predict_child to all the midparent heights

height.with_column(
    'prediction', height.apply(predict_child, 'parent average')
).select(2, 3, 4).scatter('parent average')


help(predict_child) #details about function predict_child

type(predict_child) #returns - function
