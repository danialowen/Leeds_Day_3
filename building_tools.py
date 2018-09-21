# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:07:39 2018

@author: gydwo
"""

import random
import operator
import matplotlib.pyplot


def distance_between(agents_row_a, agents_row_b):
    answer = (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5 
    return answer
    
num_of_agents = 10
num_of_iterations = 100
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

# Move the agents.

# j is the number of iterations, i.e. we flip the coin 100
# times and it moves once in each direction each time. instead of
# flipping the coin once and it moves in one direction 100 paces 

# i is the range of agents, which is 10 coordinates

# the first section is [i][0] which determines the y coords and decides
# whether it moves up or down

# the second section is [i][1] which determines the x coords and decides
# whether it moves left or right

# the %100 divides it by a hundered and ensures the point stays on grid
# e.g. 100x100 grid. point is 103, divided by 100 and remainder is 3
# thus, a valuer of 3 ensures it re-enters the grid on other side 



for j in range(num_of_iterations):
    
    for i in range(num_of_agents):
        
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100
            
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100
            

# Pythagoras code for calculating the distance
# answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
# print(answer)


# testing new function - pythagoras function for distance between any two
# given points. fist is always "agents_row_a" other "..._b"
# this is a function call

distance = distance_between(agents[0], agents[1])
print(distance)

distance = distance_between(agents[3], agents[5])
print(distance)

# now we have to create a for-loop to measure the distance
# between all of the agents against eachother
# this is inefficient as it tests more than double of what needs be
# e.g. test agents[2] vs [8] and then agents[8] vs [2]
# to test all, set letters to all agents e.g. 'k' and 'm'
# tests x and y values of each agent

"""for k in range(num_of_agents):
    for m in range(num_of_agents):
        distance = distance_between(agents[k], agents[m])
        if distance > 0 :
            print(distance)"""
            
            
            
# this is to test all agents against each other without duplicates
# so 'x' (all agents) are tested against all other agents ('z'),
# one value above 'x' so that it is not tested against itself
# 'remove 0s' is also removed as two points may be at same point
# and not necessarily the same agent

for x in range(num_of_agents):
    for z in range(x + 1,num_of_agents):
        distance = distance_between(agents[x], agents[z])
        print(distance)






