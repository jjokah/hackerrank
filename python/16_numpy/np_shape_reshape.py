"""
HackerRank Challenge: Shape and Reshape (Python)
https://www.hackerrank.com/challenges/np-shape-reshape/problem

Using the shape and reshape tools available in the NumPy module, configure a list according to the guidelines.
"""

import numpy


my_array = list(map(int, input().strip().split()))
my_numpy_array = numpy.array(my_array)

print(numpy.reshape(my_numpy_array, (3, 3)))