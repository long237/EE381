import math
import random
import statistics
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt


def calInterval(mean, sigma, sample_size, zValue):
    interval = []
    upperLim = mean + zValue * (sigma / math.sqrt(sample_size))
    lowerLim = mean - zValue * (sigma / math.sqrt(sample_size))
    interval.append(lowerLim)
    interval.append(upperLim)
    return interval

def calIntervalNormal(mean, sigma, sample_size, con_level):
    interval = []
    if (con_level == 95):
        result = mean + 1.96 * (sigma / math.sqrt(sample_size))
        resultNegative = mean - 1.96 * (sigma / math.sqrt(sample_size))
        interval.append(resultNegative)
        interval.append(result)

    elif (con_level == 99):
        result = mean + 2.58 * (sigma / math.sqrt(sample_size))
        resultNegative = mean - 2.58 * (sigma / math.sqrt(sample_size))
        interval.append(resultNegative)
        interval.append(result)

    return interval

def main():
    N = 1_000_000
    MEAN = 100
    sigma = 12
    Z1 = 1.96
    Z2 = 2.58

    student5_95 = 2.78
    student5_99 = 4.6
    student40_95 = 2.02         #look at 97.5 percent tile for 40 degree of freedom
    student40_99 = 2.70
    student120_95 = 1.98
    student120_99 = 2.62

    population = np.random.normal(MEAN, sigma, N)
    # print(type(population))

    populationList = population.tolist()
    #print(type(populationList))
    pop_mean = statistics.mean(populationList)
    print("Pop mean: ", pop_mean)

    number_run = 10000
    sam_size = 120
    counterT = 0
    counterT_99 = 0
    counterN = 0
    counterN_99 = 0

    for i in range(number_run):
        sample = random.sample(populationList, sam_size)
        sam_mean = statistics.mean(sample)
        sam_dev = statistics.stdev(sample)

        interval_T95 = calInterval(sam_mean, sam_dev, sam_size, student5_95)
        interval_T99 = calInterval(sam_mean, sam_dev, sam_size, student5_99)
        interval_N95 = calIntervalNormal(sam_mean, sam_dev, sam_size, 95)
        interval_N99 = calIntervalNormal(sam_mean, sam_dev, sam_size, 99)

        if (pop_mean >= interval_T95[0] and pop_mean < interval_T95[1]):
            counterT += 1
        if (pop_mean >= interval_T99[0] and pop_mean < interval_T99[1]):
            counterT_99 += 1

        #Normal
        if (pop_mean >= interval_N95[0] and pop_mean < interval_N95[1]):
            counterN += 1
        if (pop_mean >= interval_N99[0] and pop_mean < interval_N99[1]):
            counterN_99 += 1


    successT = counterT / number_run
    successT_99 = counterT_99 / number_run
    successN = counterN / number_run
    successN_99 = counterN_99 / number_run
    print("Sample size: ", sam_size)
    print("Success T: ", successT)
    print("Success T 99% conf: ", successT_99)
    print("Success N: ", successN)
    print("Success N 99% conf: ", successN_99)

main()