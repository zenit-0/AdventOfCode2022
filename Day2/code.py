# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 19:55:09 2022

@author: zenit-0
"""

import numpy as np

#initialize
data = np.loadtxt("data.txt", dtype='str')
score_naive = 0
score_real = 0
real_input = data[:,1]
value_scores = {'X':1, 'Y':2, 'Z':3}
game_scores = {'AX':3, 'BY':3, 'CZ':3, 'AY':6, 'BZ':6, 'CX':6, 'AZ':0, 'BX':0, 'CY':0}
real_scores = {'AX':'Z', 'AY':'X', 'AZ':'Y', 'BX':'X', 'BY':'Y', 'BZ':'Z', 'CX':'Y', 'CY':'Z', 'CZ':'X'}

#calculate and show naive game score
for i in np.arange(0,data[:,0].size,1):
    game = data[i,0]+data[i,1]
    score_naive = score_naive + value_scores[game[1]]+game_scores[game]
print(score_naive)

#calculate and show real game score
for i in np.arange(0,data[:,0].size,1):
    game = data[i,0]+data[i,1]
    real_input = real_scores[game]
    score_real = score_real + game_scores[game[0]+real_input] + value_scores[real_input]
print(score_real)
