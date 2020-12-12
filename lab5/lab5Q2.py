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