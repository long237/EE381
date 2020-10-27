#Authors: Daniel Duong and Long Nguyen
from random import uniform
import random

import numpy as np

numExperiments = 100000
counter = 0

for i in range(numExperiments):
    radius = 5
    #radius = random.uniform(1, 100);
    a = 0
    circumference = 2 * 3.14 * radius

    x = random.uniform(a, circumference)
    y = random.uniform(a, circumference)
    z = random.uniform(a, circumference)

    points = []
    points.append(x)
    points.append(y)
    points.append(z)
    points.sort()
    #print("Arrays:", points)
    '''print("radius: ", radius)
    print("x: ", x)
    print("y: ", y)
    print("z: ", z) '''

    #biggest = max(x, y, z)
    #print("largest: ", biggest)
    #smallest = min(x, y, z)
    #print("smallest: ", smallest)

    difference1 = points[2] - points[0]             #when c is biggest and b is sandwich between a and c
    difference2 = points[2] - points[1]
    difference3 = points[1] - points[0]
    #print("difference: ", difference)
    #print("semicircle value: ", (circumference / 2))
    semi_c = circumference / 2
    # if c - a is less than circumference semicircle with b sandwiched between a and c increase counter
    if difference1 <= semi_c:
        counter += 1
    elif (difference1 > semi_c):
        #if(difference3 <= semi_c):
        if (points[1] < semi_c):        #check to see which semicircle point[1](second smallest) is.
            if(circumference - difference2 <= semi_c):
                counter += 1
        else:
            if (circumference - difference3) <= semi_c:
                counter += 1

    #elif difference >= (circumference / 2):

print("radius: ", radius)
print("circumference: ", circumference)
#print("x: ", x)
#print("y: ", y)
#print("z: ", z)
#print("largest: ", biggest)
#print("smallest: ", smallest)
#print("difference: ", difference)
#print("semicircle value: ", (circumference / 2))
print("Counter is at: ", counter)
print("The probability is: ", (counter / numExperiments))






