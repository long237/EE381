#Authors: Daniel Duong and Long Nguyen
import math
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

'''pi will be 3.14, e will be 2.718'''
e = 2.7182818284590452353602874713527
pi = 3.14159265359

def probabilityFunction(x, expectation, sigma):
    exponentEquation = -(pow((x - expectation), 2) / (2 * sigma))
    probX = (1 / math.sqrt(2 * pi * sigma)) * (pow(e, exponentEquation))
    #print(probX)
    return probX

def distributionFunction(x, expectation, sigma):
    distribX = 0.5 * (math.erf((x - expectation) / math.sqrt(2 * sigma))) + 0.5

    return distribX

def main():
    print("Part A")
    probFunc = probabilityFunction(0.5, 0.5, 0.5)

    print("The probabilty function is: ", probFunc)

    disFunc = distributionFunction(0.5, 0.5, 0.5)

    print("The distribution function is: ", disFunc)
    print()

    print("Part B")
    probFuncList = []
    probFuncList2 = []
    probFuncList3 = []
    probFuncList4 = []
    probFuncList5 = []
    probFuncList6 = []

    cdfFuncList = []
    cdfFuncList2 = []
    cdfFuncList3 = []
    cdfFuncList4 = []
    cdfFuncList5 = []
    cdfFuncList6 = []

    xValues = np.arange(-6, 6, 0.1)
    print(np.size(xValues))
    for i in range(0, np.size(xValues)): #second paramter is excluded from the range, so by having 7 as the range, we include 6
        #print(i)

        probFuncList.append(probabilityFunction(xValues[i], 0, 1))
        cdfFuncList.append(distributionFunction(xValues[i], 0, 1))


        probFuncList2.append(probabilityFunction(xValues[i], 0, 0.1))
        cdfFuncList2.append(distributionFunction(xValues[i], 0, 0.1))


        probFuncList3.append(probabilityFunction(xValues[i], 0, 0.01))
        cdfFuncList3.append(distributionFunction(xValues[i], 0, 0.01))


        probFuncList4.append(probabilityFunction(xValues[i], -3, 1))
        cdfFuncList4.append(distributionFunction(xValues[i], -3, 1))


        probFuncList5.append(probabilityFunction(xValues[i], -3, 0.1))
        cdfFuncList5.append(distributionFunction(xValues[i], -3, 0.1))


        probFuncList6.append(probabilityFunction(xValues[i], -3, 0.01))
        cdfFuncList6.append(distributionFunction(xValues[i], -3, 0.01))

        '''probFuncList.append(probabilityFunction(xValues[i], 0, 1))
        #print(probabilityFunction(i, 0, 1))
        probFuncList.append(probabilityFunction(xValues[i], 0, 0.1))
        probFuncList.append(probabilityFunction(xValues[i], 0, 0.01))
        probFuncList.append(probabilityFunction(xValues[i], -3, 1))
        probFuncList.append(probabilityFunction(xValues[i], -3, 0.1))
        probFuncList.append(probabilityFunction(xValues[i], -3, 0.01))


        cdfFuncList.append(distributionFunction(xValues[i], 0, 1))
        cdfFuncList.append(distributionFunction(xValues[i], 0, 0.1))
        cdfFuncList.append(distributionFunction(xValues[i], 0, 0.01))
        cdfFuncList.append(distributionFunction(xValues[i], -3, 1))
        cdfFuncList.append(distributionFunction(xValues[i], -3, 0.1))
        cdfFuncList.append(distributionFunction(xValues[i], -3, 0.01)'''

    print("probFunctionList: ", probFuncList)
    print("size of probFunctionList: ", len(probFuncList))
    print("cdfFuncList: ", cdfFuncList)
    print("size of cdfFuncList: ", len(cdfFuncList))
    print("probFunctionList2: ", probFuncList2)
    print("size of probFunctionList2: ", len(probFuncList2))
    print("cdfFuncList2: ", cdfFuncList2)
    print("size of cdfFuncList2: ", len(cdfFuncList2))
    print("probFunctionList3: ", probFuncList3)
    print("size of probFunctionList3: ", len(probFuncList3))
    print("cdfFuncList3: ", cdfFuncList3)
    print("size of cdfFuncList3: ", len(cdfFuncList3))

    #plt.subplot(221)
    figure1 = plt.figure(1)
    plt.plot(xValues,probFuncList, 'b') #pass in the xValues and list of probabilities given by the x values
    plt.plot(xValues, probFuncList2, 'r')
    plt.plot(xValues, probFuncList3, 'g')
    plt.plot(xValues, probFuncList4, 'c')
    plt.plot(xValues, probFuncList5, 'm')
    plt.plot(xValues, probFuncList6, 'y')
    plt.title("PDF Curves")
    plt.xlabel("X values")
    plt.ylabel("f(x)")

    figure2 = plt.figure(2)
    plt.plot(xValues, cdfFuncList, 'b')
    plt.plot(xValues, cdfFuncList2, 'r')
    plt.plot(xValues, cdfFuncList3, 'g')
    plt.plot(xValues, cdfFuncList4, 'c')
    plt.plot(xValues, cdfFuncList5, 'm')
    plt.plot(xValues, cdfFuncList6, 'y')
    plt.title("CDF Curves")
    plt.xlabel("X values")
    plt.ylabel("F(x)")

    print("The expectation affects normal pdf and cdf graphs by "
          "shifting the origin to the left of the x-axis"
          "sigma squared changes the slope/steepness of the graph"
          "The smaller the sigma squared, the more steep it is"
          "The bigger the sigma squared, the less steep it is ")

    plt.show()



main()