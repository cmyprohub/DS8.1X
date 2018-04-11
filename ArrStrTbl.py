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




'''STRINGS'''

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

'''ARRAYS'''
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

Each of these functions takes an array of strings and returns an array.
Function	Description
np.char.lower	Lowercase each element
np.char.upper	Uppercase each element
np.char.strip	Remove spaces at the beginning or end of each element
np.char.isalpha	Whether each element is only letters (no numbers or symbols)
np.char.isnumeric	Whether each element is only numeric (no letters)
Each of these functions takes both an array of strings and a search string; each returns an array.
Function	Description
np.char.count	Count the number of times a search string appears among the elements of an array
np.char.find	The position within each element that a search string is found first
np.char.rfind	The position within each element that a search string is found last
np.char.startswith	Whether each element starts with the search string
