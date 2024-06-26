"""
HackerRank Challenge: Floor, Ceil, and Rint (Python)
https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem

Use the floor, ceil and rint tools of NumPy on the given array.
"""

import numpy

numpy.set_printoptions(legacy='1.13')

array_A = numpy.array(list(map(float, input().split())))
print(numpy.floor(array_A))
print(numpy.ceil(array_A))
print(numpy.rint(array_A))
