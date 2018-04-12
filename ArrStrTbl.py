#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 12:01:55 2018

@author: Suma
"""
from datascience import *
import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

abs(-55) #55
max(9,-3) #9
round(5-1.3) #4




'''A few functions are available by default, 
such as abs and round, but most functions that are built into the Python language
 are stored in a collection of functions called a module. An import statement is used to 
 provide access to a module, such as math or operator.'''
import math
import operator
math.sqrt(operator.add(4, 5))

'''Finding type'''

type(abs) #builtin_function_or_method

x = 3
type(x) #int



''''''''''''''''''
'''STRINGS'''
''''''''''''''''''

"data" + " " + "science" #returns 'data science'

''''The str function returns a string representation of any value. 
Using this function, strings can be constructed that have embedded values.'''

"That's " + str(1 + 1) + ' ' + str(True) # returns "That's 2 True"

#String methods
"loud".upper() #returns 'LOUD'

#Perhaps the most important method is replace, which replaces 
#all instances of a substring within the string. The replace method takes two arguments, the text to be replaced and its replacement.
'hitchhiker'.replace('hi', 'ma') #returns 'matchmaker'

'''Boolean'''
3 > 1 + 1 # returns True
3!=2 #returns True

x = 12
y = 5
min(x, y) <= (x+y)/2 <= max(x, y) #returns True

#Strings can also be compared, and their order is alphabetical. 
#A shorter string is less than a longer string that begins with the shorter string.

"Dog" > "Catastrophe" > "Cat" # returns True

''''''''''''''''''
'''ARRAYS'''
''''''''''''''''''
baseline_high = 14.48
highs = make_array(baseline_high - 0.880, baseline_high - 0.093,
                   baseline_high + 0.105, baseline_high + 0.684)
highs #returns array([ 13.6  ,  14.387,  14.585,  15.164])

average = sum(highs)/len(highs)

(9/5) * highs + 32
highs.size #returns 4
highs.sum()
highs.mean()

#For example, the diff function computes the difference between each adjacent 
#pair of elements in an array. 
#The first element of the diff is the second element minus the first.
np.diff(highs) #returns array([ 0.787,  0.198,  0.579])


'''Function	Description
np.prod	Multiply all elements together
np.sum	Add all elements together
np.all	Test whether all elements are true values (non-zero numbers are true)
np.any	Test whether any elements are true values (non-zero numbers are true)
np.count_nonzero	Count the number of non-zero elements'''

np.count_nonzero(highs) #returns 4

#Each of these functions takes an array as an argument and returns an array of values.

np.diff(highs) #	Difference between adjacent elements
np.round(highs)#	Round each number to the nearest integer (whole number)
np.cumprod(highs)#	A cumulative product: for each element, multiply all elements so far
np.cumsum(highs)#		A cumulative sum: for each element, add all elements so far
np.exp(highs)#		Exponentiate each element
np.log(highs)#		Take the natural logarithm of each element
np.sqrt(highs)#		Take the square root of each element
np.sort(highs)#		Sort the elements

#Each of these functions takes an array of strings and returns an array.
flowers = make_array(' Rose', 'Daisy','Sunflower','Poppy','Jasmine')
np.char.lower(flowers)#	Lowercase each element
np.char.upper(flowers)#	Uppercase each element
np.char.strip(flowers)#	Remove spaces at the beginning or end of each element
np.char.isalpha(flowers)#	Whether each element is only letters (no numbers or symbols)
np.char.isnumeric(flowers)#	Whether each element is only numeric (no letters)
#Each of these functions takes both an array of strings and a search string; each returns an array
np.char.count(flowers,'ppy')#	Count the number of times a search string appears among the elements of an array
np.char.find(flowers,'ppy')#	The position within each element that a search string is found first
np.char.rfind(flowers,'ppy')#	The position within each element that a search string is found last
np.char.startswith(flowers,'ppy')#Whether each element starts with the search string

'''A range is an array of numbers in increasing or decreasing order, each separated by a regular interval. Ranges are useful in a surprisingly large number of situations, so it's worthwhile to learn about them.
Ranges are defined using the np.arange function, which takes either one, two, or three arguments: a start, and end, and a 'step'.
If you pass one argument to np.arange, this becomes the end value, with start=0, step=1 assumed. Two arguments give the start and end with step=1 assumed. Three arguments give the start, end and step explicitly.
A range always includes its start value, but does not include its end value. It counts up by step, and it stops before it gets to the end'''


np.arange(5) #array([0, 1, 2, 3, 4])
np.arange(5,18) #array([ 5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17])
np.arange(5,18,2) #array([ 5,  7,  9, 11, 13, 15, 17])


'''LEIBNIZ FORMULA for Pi = 4(1-1/3+1/5-1/7+1/9-1/11........ -1/9999)'''

positive_term_denominators = np.arange(1, 10000, 4)
positive_term_denominators #array([   1,    5,    9, ..., 9989, 9993, 9997])
#The positive terms we actually want to add together are just 1 over these denominators:
positive_terms = 1 / positive_term_denominators
#The negative terms have 3, 7, 11, and so on on in their denominators. This array is just 2 added to positive_term_denominators.
negative_terms = 1 / (positive_term_denominators + 2)
#The overall sum is
4 * ( sum(positive_terms) - sum(negative_terms) ) # returns 3.1413926535917955

New = make_array(2.128,  2.371,  2.874,  3.728)
Old = make_array(1,2,5,3)
Diff = New - Old #returns array([ 1.128,  0.371, -2.126,  0.728])

'''WALLIS FORMULA for Pi π≈2⋅(2/1⋅4/3⋅6/5⋯1,000,000/999999)⋅(2/3⋅4/5⋅6/7⋯1,000,000/1,000,001)'''
even = np.arange(2, 1000001, 2)
one_below_even = even - 1
one_above_even = even + 1
2 * np.prod(even/one_below_even) * np.prod(even/one_above_even) #returns 3.1415910827951143

''''''''''''''''''
'''TABLES'''
''''''''''''''''''
from datascience import *
Table().with_columns('Number of petals', make_array(8, 34, 5,12,5,7,1))
Petals = Table().with_columns(
    'Number of petals', make_array(8, 34, 5,12,5,7,1),
    'Name', make_array('lotus', 'sunflower', 'rose', 'daisy','jasmine','orchid','anthurium')
)
#Fetching table properties
Petals.num_columns
Petals.num_rows
Petals.labels
PetalsNew = Petals.relabeled('Name', 'Flower Name') # Renames one column

#Fetching one column, one item within a column
Petals.column('Name')
Petals.column(1) #same as above
Petals.column(1).item(2) #rose

#Adding another column
Petals = Petals.with_columns('Max Petals',[10,35,7,15,6,10,1])
Petals = Petals.with_columns('Percentage',Petals.column(0)/Petals.column(2))
Petals

#Setting percentage formatting(The set_format method takes Formatter objects, which exist for dates (DateFormatter), currencies (CurrencyFormatter), numbers, and percentages.)
Petals.set_format('Percentage', PercentFormatter)
Petals


#Select vs Column
Petals.select(0) #result is a table
Petals.column(0) #result is an array

#Creating a new table by dropping columns
PetalsNew = Petals.drop(4)
PetalsNew

'''SORTING'''

Petals.sort('Max Petals') #sorts ascending
Petals.sort('Max Petals',descending = 'True')

help (Petals.sort)

Petals.sort(0, distinct = 'True')

#new table with just the single row that we specified.
Petals.take(1)

#We could also get the fourth, fifth, and sixth rows by specifying a range of indices as the argument.
Petals.take(np.arange(3,6))

#If we want a table of the top 3 highest petals, we can first sort the list by No of petals and then take the first 3 rows:
Petals.sort('Number of petals',descending = 'True').take(np.arange(0,3))

#having more then 2 petals
Petals.where('Number of petals',are.above(2))

#sorting those having more than 2 petals in the order of number of petals
Petals.where('Number of petals',are.above(2)).sort('Number of petals')

#Selecting Rose in to another table
Petals.where('Name',are.equal_to('rose'))
Petals.where('Name','rose')#same as above

#Selecting those with 5 petals in to another table
Petals.where('Number of petals',are.equal_to(5))
Petals.where('Number of petals',5) #same as above

#can access rows that have multiple specified features, by using where repeatedly
Petals.where('Number of petals',5).where('Max Petals', are.above(6))

#Petals between 2 and 33
Petals.where('Number of petals',are.between(2,33))


'''
ADDITIONAL OPERATIONS
Predicate	Description
are.equal_to(Z)	Equal to Z
are.above(x)	Greater than x
are.above_or_equal_to(x)	Greater than or equal to x
are.below(x)	Less than x
are.below_or_equal_to(x)	Less than or equal to x
are.between(x, y)	Greater than or equal to x, and less than y
are.strictly_between(x, y)	Greater than x and less than y
are.between_or_equal_to(x, y)	Greater than or equal to x, and less than or equal to y
are.containing(S)	Contains the string S
You can also specify the negation of any of these conditions, by using .not_ before the condition:
Predicate	Description
are.not_equal_to(Z)	Not equal to Z
are.not_above(x)'''


'''''''''''''''''
POPULATION EXAMPLE
'''''''''''''''''
# As of Jan 2017, this census file is online here: 
data = 'http://www2.census.gov/programs-surveys/popest/datasets/2010-2015/national/asrh/nc-est2015-agesex-res.csv'

# A local copy can be accessed here in case census.gov moves the file:
# data = 'nc-est2015-agesex-res.csv'

full_census_table = Table.read_table(data)
full_census_table

#we are only interested in the population changes from 2010 to 2014. Let us select the relevant columns
partial_census_table = full_census_table.select('SEX', 'AGE', 'POPESTIMATE2010', 'POPESTIMATE2014')
partial_census_table

#Simplyfying labels
us_pop = partial_census_table.relabeled('POPESTIMATE2010', '2010').relabeled('POPESTIMATE2014', '2014')
us_pop

#Identifying chnage in populating and finding the percentage
change = us_pop.column('2014') - us_pop.column('2010')
census = us_pop.with_columns(
    'Change', change,
    'Percent Change', change/us_pop.column('2010')
)
census.set_format('Percent Change', PercentFormatter)
census.sort('Change', descending=True)
#Not surprisingly, the top row of the sorted table is the line that corresponds to the entire population: both sexes and all age groups.
#The next two rows correspond to all the men and all the women respectively.