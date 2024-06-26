"""
HackerRank Challenge: Inner and Outer (Python)
https://www.hackerrank.com/challenges/np-inner-and-outer/problem

Use NumPy to find the inner and outer product of arrays.
"""

import numpy

array_A = numpy.array(list(map(int, input().split())))
array_B = numpy.array(list(map(int, input().split())))

print(numpy.inner(array_A, array_B))
print(numpy.outer(array_A, array_B))
