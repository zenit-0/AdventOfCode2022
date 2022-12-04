# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 08:50:58 2022

@author: gbald
"""

import numpy as np

#initialize
data = np.loadtxt("input.txt", dtype='str')
split_data = np.zeros((len(data),2), dtype='object')

for i in np.arange(0,data.size,1):
    lenght = int(len(data[i]))
    split_data[i,0] = data[i][0:lenght//2]
    split_data[i,1] = data[i][lenght//2:]
