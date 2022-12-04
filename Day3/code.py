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

#scan half strings for equal item
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

#initialize
triple_split_data = np.zeros((len(data)//3,3), dtype='object')
triple_result = np.zeros(len(data)//3, dtype='str')
triple_priority_sum = 0

#generate triples of input strings
for i in np.arange(0,data.size-2,3):
    triple_split_data[int(i/3),0] = data[i][:]
    triple_split_data[int(i/3),1] = data[i+1][:]
    triple_split_data[int(i/3),2] = data[i+2][:]

#scan triple strings for equal item
for i in np.arange(0,triple_split_data[:,0].size,1):
    for j in np.arange(0,int(len(triple_split_data[i,0])),1):
        for k in np.arange(0,int(len(triple_split_data[i,1])),1):
            for l in np.arange(0,int(len(triple_split_data[i,2])),1):
                if triple_split_data[i,0][j] == triple_split_data[i,1][k] == triple_split_data[i,2][l]:
                    triple_result[i] = triple_split_data[i,0][j]

#calculate and show priority ranking
for i in np.arange(0,triple_split_data[:,0].size,1):
    triple_priority_sum = triple_priority_sum + value_scores[triple_result[i]]
print(triple_priority_sum)
