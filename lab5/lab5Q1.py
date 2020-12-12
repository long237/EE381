import math
import random
import statistics
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

def main():
    N = 1_000_000
    MEAN = 100
    sigma = 12
    Z1 = 1.96
    Z2 = 2.58

    population = np.random.normal(MEAN, sigma, N)
    # print(type(population))

    populationList = population.tolist()

    meanList = []
    posInList = []
    negaInList = []
    posInList99 = []
    negaInList99 = []
    n_value = []

    #n = random.randint(1, 100)
    for n in range(1, 201):
        n_value.append(n)
        sample = random.sample(populationList, n)
        sample_mean = statistics.mean(sample)
        meanList.append(sample_mean)

        #Calculate the confidence interval of 95
        interList = calInterval(MEAN, sigma, n, 95)
        #Add the positive and negative interval to approriate list
        posInList.append(interList[0])
        negaInList.append(interList[1])

        #Calculate the confidence interval of 99
        interList99 = calInterval(MEAN, sigma, n, 99)
        #Add the positive and negative interval to approriate list
        posInList99.append(interList99[0])
        negaInList99.append(interList99[1])

        #print("Mean: ", mean)
    print("Meanlist: ", meanList)
    print("MeanList size: ", len(meanList))
    print("PosList: ", posInList)
    print("PosList len: ", len(posInList))
    print("NegaList: ", negaInList)
    print("NegaList len: ", len(negaInList))
    print("n value: ", n_value)

    #95 confidence graph
    figure1 = plt.figure(1)
    plt.plot(n_value, meanList, linestyle=' ', marker="x")
    plt.plot(n_value, posInList, 'r', linestyle='--')
    plt.plot(n_value, negaInList, 'r', linestyle='--')
    plt.axhline(y=100, color="black")
    plt.xlabel("Sample sizes")
    plt.ylabel("x_bar")
    plt.title("Sample means and 95% confidence intervals")

    #99 confidence graph
    figure2 = plt.figure(2)
    plt.plot(n_value, meanList, linestyle=' ', marker="x")
    plt.plot(n_value, posInList99, 'g', linestyle=':')
    plt.plot(n_value, negaInList99, 'g', linestyle=':')
    plt.axhline(y=100, color="black")
    plt.xlabel("Sample sizes")
    plt.ylabel("x_bar")
    plt.title("Sample means and 99% confidence intervals")

    plt.show()

    print("n: ", n)
    print("sample: ", sample)
    #
    # print(population)
    # print("Size: ", population.size)
    # print("list: ", populationList)
    # print("Size: ", len(populationList))

def calInterval(mean, sigma, sample_size, con_level):
    interval = []
    if (con_level == 95):
        result = mean + 1.96 * (sigma / math.sqrt(sample_size))
        resultNegative = mean - 1.96 * (sigma / math.sqrt(sample_size))
        interval.append(result)
        interval.append(resultNegative)
    elif (con_level == 99):
        result = mean + 2.58 * (sigma / math.sqrt(sample_size))
        resultNegative = mean - 2.58 * (sigma / math.sqrt(sample_size))
        interval.append(result)
        interval.append(resultNegative)
    return interval
main()