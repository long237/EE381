#Authors: Daniel Duong and Long Nguyen

#Lab 1 Question 3

import numpy as np
import random

total_flips = 100000
#total_flips = 1000000 #(debug)
numCoinTosses = 100
totalNumHeads = 0
#heads=np.zeros((total_flips,1))
headCounter = 0 #let heads be the head counter
for i in range(total_flips):
    for j in range(numCoinTosses): #tosses 100 times
        result = round(random.random()) #either going to be in heads or tails

        if result == 0:
            headCounter += 1 #increment your heads by 1 every time that the coin lands on a head

    if headCounter == 35: #once you toss 100 per experiment, if you get the total number of heads to be 35
        totalNumHeads += 1 #increment the total number of heads and log it

    #print("The number of heads is: ", headCounter)
    headCounter = 0 #reset the heads to 0

print("The probability of getting 35 heads is: ", (totalNumHeads/total_flips))

