#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 15:19:27 2018

@author: $?^^@
"""
from datascience import *
import numpy as np

%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

#importing from csv to table and selecting only certain rows
full_table = Table.read_table('educ_inc.csv')
ca_2014 = full_table.where('Year', are.equal_to('1/1/14 0:00')).where('Age', are.not_equal_to('00 to 17')).drop(0).sort('Population Count')
ca_2014

#Dropping Age column
no_ages = ca_2014.drop(0)
no_ages

#Grouping based on other 3 columns ecluding salary and then summing up salaries for wach groupno_ages.group([0, 1, 2], sum)
educ_income = ca_2014.pivot(2, 3, 4, sum)
educ_income

#Defining a function to calculate percentages
def percent(x):
    """Convert an array of counts into percents"""
    return np.round((x / sum(x)) * 100, 2)

#creating another table and using function to calculate percentages for each age group and salary bandeducation category
distributions = educ_income.select(0).with_columns(
    'Bachelors or Higher', percent(educ_income.column(1)),
    'High School', percent(educ_income.column(2))
)
distributions

sum(distributions.column(1)) #check - should be 100%

#Draw barchart
distributions.barh(0)