# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 19:55:09 2022

@author: gbald
"""

import numpy as np

#initialize
input = np.loadtxt("input.txt", dtype='str')
score = 0
i = 0

value_scores = {'X':1, 'Y':2, 'Z':3}
game_scores = {'AX':3, 'BY':3, 'CZ':3, 'AY':6, 'BZ':6, 'CX':6, 'AZ':0, 'BX':0, 'CY':0}

for i in np.arange(0,input[:,0].size,1):
    game = input[i,0]+input[i,1]
    score = score + value_scores[game[1]]+game_scores[game]
    i = i+1
    
print(score)
