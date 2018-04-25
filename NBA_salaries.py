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

#Finding total salary in each position
nba.drop(0).group(['TEAM', 'POSITION'], np.average)
nba.drop(0, 2).group('POSITION', np.average)

starter_salaries = nba.drop(0).group(['TEAM', 'POSITION'], max)
starter_salaries

#Max total salary
starter_salaries.drop(1).group('TEAM', sum).sort(1, descending=True)
nba.group('TEAM', sum) #wrong, attempts to sum all columns

#Average salary in each position
position_and_money = nba.select('POSITION', 'SALARY')
position_and_money.group('POSITION')
position_and_money.group('POSITION', np.average)

#Max salary per team per position
starter_salaries = nba.drop(0).group(['TEAM', 'POSITION'], max)
starter_salaries

#Suma of starter salaries for each team
starter_salaries.drop(1).group('TEAM', sum).sort(1, descending=True)

#Avg salary per position in each team - 2 different ways using pivot and group
nba.drop(0).group(['TEAM', 'POSITION'], np.average)
nba.pivot('POSITION', 'TEAM', 'SALARY', np.average)

#Max salary for each position within a team and adding additional column for the totals
step_1 = nba.pivot('POSITION', 'TEAM', 'SALARY', max)
step_1


totals = step_1.drop(0).apply(sum)
step_1.with_columns('TOTAL', totals).sort(6, descending=True)



    
    
    




