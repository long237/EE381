#Authors: Daniel Duong and Long Nguyen
from random import uniform
import random

import numpy as np

numExperiments = 100000
counter = 0
isATriangle = False

for i in range(numExperiments):
    radius = 100
    a = 0
    circumference = 2 * 3.14 * radius

    points = np.random.uniform(0, circumference, size = 3)
    points.sort()

    """print("radius: ", radius)
    print("x: ", x)
    print("y: ", y)
    print("z: ", z)"""

    if (points[2] - points[0] <= circumference / 2):
        counter += 1
    else:
        if (points[1] > circumference / 2):
            if (circumference - points[2] + points[0]) + (points[2] - points[1]) <= circumference / 2:
                counter += 1
        else:
            if (circumference - points[2] + points[0]) + (points[1] - points[0]) <= circumference / 2:
                counter += 1

print("semicircle value: ", (circumference / 2))
print("Counter is at: ", counter)
print("The probability is: ", (counter / numExperiments))






