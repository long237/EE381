#Authors: Daniel Duong and Long Nguyen
from math import factorial
import random

'''
Here the combination formula without repetition is: C(n, r) = n! / (n - r)! r!

translated into python: math.factorial(n) / math.factorial(n - r) * math.factorial(r) 

Permutation Formula: P(n, r) = n! / (n - r)!

Ex: 1 #x = factorial(6)
#print("The factorial of 6 is: ", x)

this prints 24.

Ex: 2 We are taking the C(5, 3) = 10
y = factorial(5) / (factorial(5 - 3) * factorial(3))

print(y)

this prints 10.

'''


numPeople = 1000
numExperiments = 1000000

partyA = 0
partyB = 501
partyC = 801

randomNum = 0

counter = 0
sameParty = [0, 0, 0]       #Keep the total number all four support same party
                            # party A is index 0, party B is index 1, C is index 2
for i in range(numExperiments):
    peopleList = [] # for every experiment, you reset the list of people and the same party list
    partyCounter = [0, 0, 0] #index 0 is party A, index 1 is party B and index 2 is party C

    for j in range(4): #generating 4 random numbers to have a group of 4 random people
        randomNum = random.randint(1, numPeople)
        #print(randomNum)
        peopleList.append(randomNum)

    for k in range(len(peopleList)):

        if peopleList[k] >= partyC:
            partyCounter[2] += 1 # you want to index the list where you keep of which people support party C
            #print("supports party C")

        elif peopleList[k] >= partyB:
            partyCounter[1] += 1 # you want to index the list where you keep of which people support party C
            #print("supports party B")

        else:
            partyCounter[0] += 1 # you want to index the list where you keep of which people support party C
            #print("supports party A")

    for l in range(len(partyCounter)):
        if partyCounter[l] == 4:
            sameParty[l] += 1

    # print(partyCounter)
    # print(peopleList)
    # print()

print("Same party list: ", sameParty)
print("Probability of all support A: ", sameParty[0] / numExperiments)
print("Probability of all support B: ", sameParty[1] / numExperiments)
print("Probability of all support C: ", sameParty[2] / numExperiments)

#print("List: ", peopleList)
#print(len(peopleList))

# if peopleList[k] <= partyA:
#     sameParty[0] += 1
#     print(peopleList[k])
#
# elif peopleList[k] > partyA and peopleList[k] <= partyB:
#     sameParty[1] += 1
#     print(peopleList[k])
#
# elif peopleList[k] > partyB and peopleList[k] <= partyC:
#     sameParty[2] += 1

