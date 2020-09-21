#Authors: Daniel Duong and Long Nguyen

#Lab 1 Question 1
import numpy as np
import matplotlib.pyplot as plt
import random

N = 100000
sum = 0

sumsArray = np.zeros((N, 1))
numRolls = 0


for i in range(N):
    while sum != 7:
        numRolls += 1
        sum = random.randint(1, 6) + random.randint(1, 6)
        #print("Sum: ", sum)

    sumsArray[i, :] = numRolls
    #print("Number of rolls: ", numRolls)

    sum = 0 #reset the SUM!!!
    numRolls = 0 #reset the number of rolls

print(sumsArray)

#start the 1st graph here

bins = np.arange(1, 60, 1)
#the first parameter is the starting value, 2nd is the max value, 3rd is incrementer
#or bins = np.arange(-0.95, 0.95, 0.1)
plt.hist(sumsArray, bins)
figQuest1 = plt.figure(1)
plt.title("Sum of Rolls")
plt.xlabel("Number of Rolls")
plt.ylabel("Number of Occurences")
figQuest1.savefig("SumofRolls.jpg")
#plt.show()

#start on the 2nd graph here

numsOnxAxis = range(1, 61)
xAxis = np.size(numsOnxAxis)
print("Size of xAxis is: ", xAxis)

#calling histograms

histo1, bin_edges = np.histogram(sumsArray,numsOnxAxis) #calls the histrogram function, passes in sumsArray, and b
#print("Bin Edges are : ", bin_edges)
b1=bin_edges[0:xAxis-1] #set the above the x axis which is 13 bc you subtract 1

print("Histol 0 is: ", histo1[0])
figQuest2 = plt.figure(2)
print("The probability of the first element is: ", histo1[0] / N)
plt.stem(b1, histo1)
plt.title("Sum of Rolls")
plt.xlabel("Sum of Dices")
plt.ylabel("Number of Rolls")
figQuest2.savefig("SumofRolls.jpg")
plt.show()




