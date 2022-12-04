# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 14:40:58 2022

@author: zenit-0
"""

import numpy as np
import regex as re

#initialize
data = np.loadtxt("data.txt", dtype='str')
areas = np.zeros((data.size,4), dtype='int')
count_wrong = 0
count_full_wrong = 0

"""scan all assignments for the following patterns:
        n_1---------n_2
    N_1--------------------N_2
    
    or
    
    n_1-------------------------n_2
            N_1------------N_2
    
    N_1 can overlap with n_1 and N_2 can overlap with n_2
    
    Every time a pattern like this is found, count_wrong is increased."""

for i in np.arange(0,data.size,1):
    areas[i,:] = re.split('[\(\)\,\-\*\/]', data[i])
    if areas[i,0] >= areas[i,2] and areas[i,1] <= areas[i,3]:
        count_wrong = count_wrong + 1
    elif areas[i,0] <= areas[i,2] and areas[i,1] >= areas[i,3]:
        count_wrong = count_wrong + 1
print(count_wrong)


"""scan all assignments for the following patterns, in addition to the previous ones:
        n_1---------n_2
                N_1---------N_2
    
    or
    
                n_1-------------n_2
    N_1---------------N_2
    
    N_1 can overlap with n_2 in the first one and N_2 can overlap with n_1 in the second one
    
    Every time a pattern like this is found, count_full_wrong is increased."""

for i in np.arange(0,data.size,1):
    areas[i,:] = re.split('[\(\)\,\-\*\/]', data[i])
    if areas[i,0] >= areas[i,2] and areas[i,1] <= areas[i,3]:
        count_full_wrong = count_full_wrong + 1
    elif areas[i,0] <= areas[i,2] and areas[i,1] >= areas[i,3]:
        count_full_wrong = count_full_wrong + 1
    elif areas[i,1] >= areas[i,2] and areas[i,0] <= areas[i,2] and areas[i,3] >= areas[i,1]:
        count_full_wrong = count_full_wrong + 1
    elif areas[i,3] >= areas[i,0] and areas[i,2] <= areas[i,0] and areas[i,1] >= areas[i,3]:
        count_full_wrong = count_full_wrong + 1
print(count_full_wrong)
