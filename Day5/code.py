# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 20:01:09 2022

@author: gbald
"""

import numpy as np

#initialize
#for semplicity, the positions array is transposed compared to the data (allows for .pop() and .append())
#data1 = np.loadtxt("data1.txt", dtype='str')
positions = [['H', 'B', 'V', 'W', 'N', 'M', 'L', 'P'],
             ['M', 'Q', 'H'],
             ['N', 'D', 'B', 'G', 'F', 'Q', 'M', 'L'],
             ['Z', 'T', 'F', 'Q', 'M', 'W', 'G'],
             ['M', 'T', 'H', 'P'],
             ['C', 'B', 'M', 'J', 'D', 'H', 'G', 'T'],
             ['M', 'N', 'B', 'F', 'V', 'R'],
             ['P', 'L', 'H', 'M', 'R', 'G', 'S'],
             ['P', 'D', 'B', 'C', 'N']]

#the instruction data is converted to 'int' to allow for cycles and indexing
data2 = np.loadtxt("data2.txt", dtype='str')
instructions = np.zeros((data2[:,0].size,3), dtype='int')
instructions[:,0] = data2[:,1]
instructions[:,1] = data2[:,3]
instructions[:,2] = data2[:,5]
naive_result = []

"""move crates around naively, when the arranging is complete the top item 
from each stack is stored in naive_result and printed"""
for i in np.arange(0, data2[:,0].size, 1):
    for j in np.arange(0, instructions[i,0], 1):
        crate_to_move = positions[instructions[i,1]-1].pop()
        positions[instructions[i,2]-1].append(crate_to_move)
    if i == data2[:,0].size-1:
        for k in np.arange(0, len(positions), 1):
            top_crate = positions[k][-1]
            naive_result.append(top_crate)      
print(naive_result)
print("".join(naive_result))

positions = [['H', 'B', 'V', 'W', 'N', 'M', 'L', 'P'],
             ['M', 'Q', 'H'],
             ['N', 'D', 'B', 'G', 'F', 'Q', 'M', 'L'],
             ['Z', 'T', 'F', 'Q', 'M', 'W', 'G'],
             ['M', 'T', 'H', 'P'],
             ['C', 'B', 'M', 'J', 'D', 'H', 'G', 'T'],
             ['M', 'N', 'B', 'F', 'V', 'R'],
             ['P', 'L', 'H', 'M', 'R', 'G', 'S'],
             ['P', 'D', 'B', 'C', 'N']]
real_result = []

"""move crates around in stacks, when the arranging is complete the top item 
from each stack is stored in real_result and printed"""
for i in np.arange(0, data2[:,0].size, 1):
    crates_to_move = positions[instructions[i,1]-1][-instructions[i,0]:]
    positions[instructions[i,2]-1] = positions[instructions[i,2]-1] + crates_to_move
    positions[instructions[i,1]-1] = positions[instructions[i,1]-1][0:len(positions[instructions[i,1]-1])-instructions[i,0]]
    if i == data2[:,0].size-1:
        for k in np.arange(0, len(positions), 1):
            top_crate = positions[k][-1]
            real_result.append(top_crate)
print(real_result)
print("".join(real_result))
