#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 18:17:01 2018

@author: $?^^@
"""

from datascience import *
import numpy as np

%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

#Creating table with cafe details
drinks = Table(['Drink', 'Cafe', 'Price']).with_rows([
    ['Milk Tea', 'Tea One', 4],
    ['Espresso', 'Nefeli',  2],
    ['Latte',    'Nefeli',  3],
    ['Espresso', "Abe's",   2]
])
drinks

#Another table with coupon details
discounts = Table().with_columns(
    'Coupon % off', make_array(25, 50, 5),
    'Location', make_array('Tea One', 'Nefeli', 'Tea One')
)
discounts

#joining tables on cafe/location columns that have same values in both tabless
t = drinks.join('Cafe', discounts, 'Location')
t

#Adding new discounted prices
t.with_column('Discounted', t.column(2) * (1 - t.column(3)/ 100))

#Self join
two = drinks.join('Cafe', drinks)
two


two.with_column('Total', two.column('Price') + two.column('Price_2'))

