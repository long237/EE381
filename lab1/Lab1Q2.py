#Authors: Daniel Duong and Long Nguyen

#Lab 1 Question 2
import numpy as np
import matplotlib.pyplot as plt
import random

r = 0.0
N = 1000000 #number of experiments
#r is a random generated number

F = [0, 0.1, 0.25, 0.55, 0.8, 0.85, 1] #F is the culmative probability function
resultsArray = np.zeros((N, 1))

for i in range(N):
    r = round(random.random(), 2) #round function rounds this stuff to 2 decmial places according to the professor

    if r >= F[0] and r < F[1]:
        resultsArray[i, :] = 1
    elif r >= F[1] and r < F[2]:
        resultsArray[i, :] = 2
    elif r >= F[2] and r < F[3]:
        resultsArray[i, :] = 3
    elif r >= F[3] and r < F[4]: #problem here
        resultsArray[i, :] = 4
    elif r >= F[4] and r < F[5]:
        resultsArray[i, :] = 5
    elif r >= F[5] and r < F[6]:#problem here
        resultsArray[i, :] = 6

    #print("r is: ", r)

print("List has: ", resultsArray)
print("F[3] is: ", F[3])
print("F[4] is: ", F[4])
print("F[5] is: ", F[5])
print("F[6] is: ", F[6])

#Start the histrogram function
'''bins = np.arange(1, 6, 1)
plt.hist(resultsArray, bins)
figQuestOne = plt.figure(1)
plt.title("Sum of a Rigged Die")
plt.xlabel("Die Faces")
plt.ylabel("Number of Occurences")
figQuestOne.savefig("UnfairDie.jpg")
plt.show() #show the graph'''

numsOnxAxis = range(1, 8)
xAxis = np.size(numsOnxAxis)

histo1, bin_edges = np.histogram(resultsArray,numsOnxAxis) #calls the histrogram function, passes in sumsArray, and b
print("The hiso1 is a: ", type(histo1))
#print("Bin Edges are : ", bin_edges)
b1=bin_edges[0:xAxis-1] #set the above the x axis which is 8 because the die has 1 - 6 sides inclusively

#first graph
figQuest1 = plt.figure(1)
plt.stem(b1, histo1)
plt.title("Sum of a Rigged Die")
plt.xlabel("Number of Rolls")
plt.ylabel("Number of Occurences")
figQuest1.savefig("UnfairDie.jpg")


# a new second graph
figQuest2 = plt.figure(2)

percentage = histo1 /N
print("The type percentage is a: ", type(percentage))

plt.stem(b1, percentage)
plt.title("Sum of a Rigged Die")
plt.xlabel("Number of Rolls")
plt.ylabel("Percentage")
figQuest2.savefig("UnfairDie.jpg")
plt.show()





