#Authors: Daniel Duong and Long Nguyen

#Professors Result: 0.24763

import random

numExperiments = 100000

'''random.sample is a new module for the probability function
2nd parameter is the number of children you want to include
and the 2nd parameter is to return the number of random elements
will return a list
'''
children = random.sample(range(40), 20)
#print(children)
#print(len(children))

''' 
odds and evens

ODDS - Girls
EVENS - Boys
'''

counter = 0

for i in range(numExperiments):
    randomList = random.sample(range(40), 20)

    numBoys = 0
    numGirls = 0

    for j in range(len(randomList)):
        if randomList[j] % 2 == 0: #Even numbers are boys
            numBoys += 1

        elif randomList[j] % 2 != 0: #odds are girls
            numGirls += 1

    if numBoys == numGirls:
        counter += 1

    #print(randomList)
    #print("Number of Boys is: ",  numBoys)
    #print("Number of Girls is: ",  numGirls)
    #print("Counter: ", counter)
    #print()

print("Number of Expeiremnts is: ", numExperiments)
print("The probability of getting an equal number of girls is: ", counter / numExperiments)
print()

counter2 = 0

for k in range(numExperiments):
    randomList = random.sample(range(200), 100)

    numBoys = 0
    numGirls = 0

    for l in range(len(randomList)):
        if randomList[l] % 2 == 0: #Even numbers are boys
            numBoys += 1

        elif randomList[l] % 2 != 0: #odds are girls
            numGirls += 1

    if numBoys == numGirls:
        counter2 += 1

    #print(randomList)
    #print("Number of Boys is: ",  numBoys)
    #print("Number of Girls is: ",  numGirls)
    #print("Counter: ", counter)
    #print()

print("Number of Expeiremnts is: ", numExperiments)
print("The probability of getting an equal number of girls is: ", counter2 / numExperiments)


#totalChildren = set() # empty set

#totalChildren.append(children)
#for i in range(20):
    #children = random.sample(0, 39)
    #totalChildren.add(children)

#print(totalChildren)
#print(len(totalChildren))



