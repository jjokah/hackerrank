"""
HackerRank Chanllenge: Arrays (Python)
https://www.hackerrank.com/challenges/np-arrays/problem

Convert a list to an array using the NumPy package.
"""

import numpy


def arrays(arr):
    arr = arr[::-1]
    return numpy.array((arr), float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
