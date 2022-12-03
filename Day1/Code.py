# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 20:48:20 2022

@author: gbald
"""

import numpy as np

#initialize (loadfile has been changed to have zeroes instead of empty spaces)
input = np.loadtxt("input.txt", unpack=True)
temp = 0
final = np.zeros(1)

#scan array for zero-interrupted sum
for i in np.arange(0,input.size,1):
    if input[i] == 0:
        final = np.append(final, temp)
        temp = 0
    else:
        temp = temp + input[i]
        i = i+1
        
#find highest value in array
highest_value = np.max(final)

#sort array
sorted_final = np.sort(final)

#sum top elements
top = 3
result = np.sum(sorted_final[sorted_final.size-(top):])