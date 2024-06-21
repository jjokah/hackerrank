"""
HackerRank Chanllenge: Zeros and Ones (Python)
https://www.hackerrank.com/challenges/np-zeros-and-ones/problem

Print an array using the zeros and ones tools in the NumPy module.
"""

import numpy

shape = tuple(map(int, input().split()))

print(numpy.zeros(shape, dtype=int))
print(numpy.ones(shape, dtype=int)