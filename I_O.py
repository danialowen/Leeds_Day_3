# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 14:54:28 2018

@author: gydwo
"""

import csv
import matplotlib.pyplot
import random
import operator
import agentframework



f = open('in.txt', newline='')

#create the big, empty file i.e. 'environment
environment = []

#read in the csv data 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

#create sublists within the environment called rowlist
#append the sublist values to the sublists
#append the sublists to the environment

for row in reader:
    rowlist=[]
    for value in row:
        rowlist.append(value)
        print(value)
    environment.append(rowlist)
f.close()


#import agent data from last prac

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) + 
        ((agents_row_a.y - agents_row_b.y)**2))**0.5
            
num_of_agents = 10
num_of_iterations = 100
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment))

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):

        agents[i].move()
        agents[i].eat()


"""#plot values
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()"""

matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()


