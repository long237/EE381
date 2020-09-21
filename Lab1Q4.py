#Authors: Daniel Duong and Long Nguyen

import random
from collections import Counter

#NOTE: List index starts at 0, NOT 1

numExperiments = 1000000
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
#print(len(ranks))
groupOf4 = 0

for i in range(numExperiments):
    deck = []
    hand = []
    for i in range(4):
        for j in range(len(ranks)):
            deck.append(ranks[j]) #adding cards to the deck

#print(deck)
    random.shuffle(deck) #shuffle the deck
#print(deck)
#print("The size of the deck is: ", len(deck))

    deckSize = 51

    for j in range(0, 6):
        hand.append(deck.pop())

    #print("The size of the deck right now is: ", len(deck))

    #print(hand)
    #print(deck)
    #print("The hand has: ", len(hand), " cards")
    #print("The deck has: ", len(deck), " cards")

    handDups = Counter(hand)
    #print("The data type of handdups is: ", type(handDups))
    #print("Hand Dupes:  ", handDups)

    #print(Counter(handDups).values())

    numberOfDuplicates = Counter(handDups).values()

    for i in numberOfDuplicates:
        if i == 4:
            groupOf4 += 1
            print("Hand: ", hand)

print("Number of groups of 4:", groupOf4)
print("Probability of 4 of a kind: ", groupOf4 / numExperiments)

