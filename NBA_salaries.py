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

#Loading to a table and renaming a column
nba = Table.read_table('nba_salaries.csv').relabel(3, 'SALARY')
nba

#Selecting only 2 fields to a new table & grouping by 'team' ; adding up salaries by team and sorting
teams_and_money = nba.select('TEAM', 'SALARY')
teams_and_money.group('TEAM', sum).sort(1, descending=True)

#Attempts to sum all columns
nba.group('TEAM', sum)

#Finding total number of players who play in each position
position_and_money = nba.select('POSITION', 'SALARY')
position_and_money.group('POSITION')

position_and_money.group('POSITION', np.average)

nba.drop(0).group(['TEAM', 'POSITION'], np.average)
nba.drop(0, 2).group('POSITION', np.average)

starter_salaries = nba.drop(0).group(['TEAM', 'POSITION'], max)
starter_salaries

starter_salaries.drop(1).group('TEAM', sum).sort(1, descending=True)


