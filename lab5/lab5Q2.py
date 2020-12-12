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
        interval.append(result)
        interval.append(resultNegative)
    elif (con_level == 99):
        result = mean + 2.58 * (sigma / math.sqrt(sample_size))
        resultNegative = mean - 2.58 * (sigma / math.sqrt(sample_size))
        interval.append(result)
        interval.append(resultNegative)
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
    counter5 = 0
    counter5_99 = 0
    counter40 = 0
    counter40_99 = 0
    counter120 = 0
    counter120_99 = 0
    for i in range(number_run):
        sample5 = random.sample(populationList, 5)
        sample40 = random.sample(populationList, 40)
        sample120 = random.sample(populationList, 120)

        sam_mean5 = statistics.mean(sample5)
        sam_dev5 = statistics.stdev(sample5)
        sam_mean40 = statistics.mean(sample40)
        sam_dev40 = statistics.stdev(sample40)
        sam_mean120 = statistics.mean(sample120)
        sam_dev120 = statistics.stdev(sample120)

        interval5 = calInterval(sam_mean5, sam_dev5, 5, student5_95)
        interval40 = calInterval(sam_mean40, sam_dev40, 40, student40_95)
        interval120 = calInterval(sam_mean120, sam_dev120, 120, student120_95)
        interval5_99 = calInterval(sam_mean5, sam_dev5, 5, student5_99)
        interval40_99 = calInterval(sam_mean40, sam_dev40, 40, student40_99)
        interval120_99 = calInterval(sam_mean120, sam_dev120, 120, student120_99)

        #Counter for sample size of 5
        if (pop_mean >= interval5[0] and pop_mean < interval5[1]):
            counter5 += 1
        if (pop_mean >= interval5_99[0] and pop_mean < interval5_99[1]):
            counter5_99 += 1

        #Counter for sample size of 40
        if (pop_mean >= interval40[0] and pop_mean < interval40[1]):
            counter40 += 1
        if (pop_mean >= interval40_99[0] and pop_mean < interval40_99[1]):
            counter40_99 += 1

        # Counter for sample size of 120
        if (pop_mean >= interval120[0] and pop_mean < interval120[1]):
            counter120 += 1
        if (pop_mean >= interval120_99[0] and pop_mean < interval120_99[1]):
            counter120_99 += 1

    print("Mean 5 : ", sam_mean5)
    print("Deviation 5 ", sam_dev5)
    print("Mean 40: ", sam_mean40)
    print("Deviation 40 ", sam_dev40)
    print("Mean 120: ", sam_mean120)
    print("Deviation 120:", sam_dev120)
    print("Interval 5: ", interval5)
    print("Interval 40: ", interval40)
    print("Interval 120: ", interval120)

    print("Counter 5: ", counter5)
    print("Counter 40 ", counter40)
    print("Counter 120: ", counter120)

    success5 = counter5 / number_run
    success40 = counter40 / number_run
    success120 = counter120 / number_run
    success5_99 = counter5_99 / number_run
    success40_99 = counter40_99 / number_run
    success120_99 = counter120_99 / number_run
    print("Success 5: ", success5)
    print("Success 5 99% conf: ", success5_99)
    print("Success 40: ", success40)
    print("Success 40 99% conf: ", success40_99)
    print("Success 120: ", success120)
    print("Success 120 99% conf: ", success120_99)

    # print(len(sample5))
    # print(len(sample40))
    # print(len(sample120))

main()