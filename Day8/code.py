# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 13:40:38 2022

@author: gbald
"""
import numpy as np

data = np.loadtxt('data.txt', dtype = 'str')
data_array = np.zeros((len(data), len(data[0])), dtype = 'int')
trees_count = len(data)*2+len(data[0])*2-4

for i in np.arange(0, len(data), 1):
    for j in np.arange(0, len(data), 1):
        data_array[i, j] = data[i][j]

for i in np.arange(1, len(data)-1, 1):
    for j in np.arange(1, len(data)-1, 1):
        if i == 1 and j == 1:
            cond_1 = np.max(data_array[1,2:])
            cond_2 = data_array[1,0]
            cond_3 = np.max(data_array[2:,1])
            cond_4 = data_array[0,1]            
        elif i == 1 and j == len(data)-2:
            cond_1 = data_array[i,-1]
            cond_2 = np.max(data_array[i,:j])
            cond_3 = np.max(data_array[i+1:,j])
            cond_4 = data_array[0,j]
        elif i == len(data)-2 and j == 1:
            cond_1 = np.max(data_array[i,j+1:])
            cond_2 = data_array[i,0]
            cond_3 = data_array[-1,j]
            cond_4 = np.max(data_array[:i,j])
        elif i == len(data)-2 and j == len(data)-2:
            cond_1 = data_array[i,-1]
            cond_2 = np.max(data_array[i,:j])
            cond_3 = data_array[-1,j]
            cond_4 = np.max(data_array[:i,j])
        elif i == 1:
            cond_1 = np.max(data_array[i,j+1:])
            cond_2 = np.max(data_array[i,:j])
            cond_3 = np.max(data_array[i+1:,j])
            cond_4 = data_array[0,j]
        elif j == 1:
            cond_1 = np.max(data_array[i,j+1:])
            cond_2 = data_array[i,0]
            cond_3 = np.max(data_array[i+1:,j])
            cond_4 = np.max(data_array[:i,j])
        elif j == len(data)-2:
            cond_1 = data_array[i,-1]
            cond_2 = np.max(data_array[i,:j])
            cond_3 = np.max(data_array[i+1:,j])
            cond_4 = np.max(data_array[:i,j])
        elif i == len(data)-2:
            cond_1 = np.max(data_array[i,j+1:])
            cond_2 = np.max(data_array[i,:j])
            cond_3 = data_array[-1,j]
            cond_4 = np.max(data_array[:i,j])
        else:
            cond_1 = np.max(data_array[i,j+1:])
            cond_2 = np.max(data_array[i,:j])
            cond_3 = np.max(data_array[i+1:,j])
            cond_4 = np.max(data_array[:i,j])
        target_tree = data_array[i,j]
        if target_tree > cond_1 or target_tree > cond_2 or target_tree > cond_3 or target_tree > cond_4:
            trees_count = trees_count + 1

print(trees_count)
score = 0
temp_score = 0
score_E = 0
score_W = 0
score_S = 0
score_N = 0
temp_score_E = 0
temp_score_W = 0
temp_score_S = 0
temp_score_N = 0
data_array[0,:] = 10
data_array[-1,:] = 10
data_array[:,0] = 10
data_array[:,-1] = 10

for i in np.arange(1, len(data)-1, 1):
    for j in np.arange(1, len(data)-1, 1):
        target_tree = data_array[i,j]
        if target_tree == 0:
            temp_score = 0
        if i == 1 and j == 1:
            score_E = np.min(np.where(target_tree <= data_array[i,j+1:]))+1
            score_W = 1
            score_S = np.min(np.where(target_tree <= data_array[i+1:,j]))+1
            score_N = 1
        elif i == 1 and j == len(data)-2:
            score_E = 1
            score_W = np.min(np.where(target_tree <= np.flip(data_array[i,:j])))+1
            score_S = np.min(np.where(target_tree <= data_array[i+1:,j]))+1
            score_N = 1
        elif i == len(data)-2 and j == 1:
            score_E = np.min(np.where(target_tree <= data_array[i,j+1:]))+1
            score_W = 1
            score_S = 1
            score_N = np.min(np.where(target_tree <= np.flip(data_array[:i,j])))+1
        elif i == len(data)-2 and j == len(data)-2:
            score_E = 1
            score_W = np.min(np.where(target_tree <= np.flip(data_array[i,:j])))+1
            score_S = 1
            score_N = np.min(np.where(target_tree <= np.flip(data_array[:i,j])))+1
        elif i == 1:
            score_E = np.min(np.where(target_tree <= data_array[i,j+1:]))+1
            score_W = np.min(np.where(target_tree <= np.flip(data_array[i,:j])))+1
            score_S = np.min(np.where(target_tree <= data_array[i+1:,j]))+1
            score_N = 1
        elif j == 1:
            score_E = np.min(np.where(target_tree <= data_array[i,j+1:]))+1
            score_W = 1
            score_S = np.min(np.where(target_tree <= data_array[i+1:,j]))+1
            score_N = np.min(np.where(target_tree <= np.flip(data_array[:i,j])))+1
        elif j == len(data)-2:
            score_E = 1
            score_W = np.min(np.where(target_tree <= np.flip(data_array[i,:j])))+1
            score_S = np.min(np.where(target_tree <= data_array[i+1:,j]))+1
            score_N = np.min(np.where(target_tree <= np.flip(data_array[:i,j])))+1
        elif i == len(data)-2:
            score_E = np.min(np.where(target_tree <= data_array[i,j+1:]))+1
            score_W = np.min(np.where(target_tree <= np.flip(data_array[i,:j])))+1
            score_S = 1
            score_N = np.min(np.where(target_tree <= np.flip(data_array[:i,j])))+1
        else:
            score_E = np.min(np.where(target_tree <= data_array[i,j+1:]))+1
            score_W = np.min(np.where(target_tree <= np.flip(data_array[i,:j])))+1
            score_S = np.min(np.where(target_tree <= data_array[i+1:,j]))+1
            score_N = np.min(np.where(target_tree <= np.flip(data_array[:i,j])))+1
        temp_score = score_E * score_W * score_S * score_N 
        if temp_score >= score:
            score = temp_score

print(score)
