#Authors: Daniel Duong and Long Nguyen

''' There is no replacements at all '''

# Theoretical Result: 0.0002064

import random

numExperiments = 1_000_000

#for i in range(20):
    #print("i is: ", i)

numWinLottery = 0

for i in range(numExperiments):
    counterLottery = 0 # if you declare counterLottery when comparing every index, then you will reset it every time you compare your numbers to the winning numbers
    myNumList = random.sample(range(1, 21), 4)
    #print("This is my numbers for the lottery: ", myNumList)

    drawingList = random.sample(range(1, 21), 4)
    #print("Winning lottery list: ", drawingList)

    for j in range(len(myNumList)):

        if myNumList[j] in drawingList:
            counterLottery += 1

    print("Number of matches found: ", counterLottery)
    if counterLottery == 4:
        numWinLottery += 1

    print("Won lottery: ", numWinLottery, "\n")

print("The probability of winning the lottery is: ", numWinLottery / numExperiments)

