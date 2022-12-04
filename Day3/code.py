# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 08:50:58 2022

@author: gbald
"""

import numpy as np

#initialize
data = np.loadtxt("input.txt", dtype='str')
split_data = np.zeros((len(data),2), dtype='object')
result = np.zeros(len(data), dtype='str')
priority_sum = 0

#separate input strings in halves
for i in np.arange(0,data.size,1):
    lenght = int(len(data[i]))
    split_data[i,0] = data[i][0:lenght//2]
    split_data[i,1] = data[i][lenght//2:]

#scan halfstrings for equal item
for i in np.arange(0,data.size,1):
    lenght = int(len(data[i])/2)
    for j in np.arange(0,lenght,1):
        for k in np.arange(0,lenght,1):
            if split_data[i,0][j] == split_data[i,1][k]:
                result[i] = split_data[i,0][j]

#initialize dictionary for priority ranking
value_scores = {'a':1, 	'b':2, 	'c':3, 	'd':4, 	'e':5, 	'f':6, 	'g':7, 	'h':8, 	'i':9, 	'j':10, 'k':11,	'l':12,	'm':13,
                'n':14,	'o':15,	'p':16,	'q':17,	'r':18,	's':19,	't':20,	'u':21,	'v':22,	'w':23,	'x':24,	'y':25,	'z':26,
                'A':27,	'B':28,	'C':29,	'D':30,	'E':31,	'F':32,	'G':33,	'H':34,	'I':35,	'J':36,	'K':37, 'L':38, 'M':39, 
                'N':40, 'O':41, 'P':42,	'Q':43, 'R':44, 'S':45, 'T':46, 'U':47, 'V':48, 'W':49, 'X':50, 'Y':51, 'Z':52}

#calculate and show priority ranking
for i in np.arange(0,data.size,1):
    priority_sum = priority_sum + value_scores[result[i]]
print(priority_sum)
