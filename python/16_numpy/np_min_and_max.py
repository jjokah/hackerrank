"""
HackerRank Challenge: Min and Max (Python)
https://www.hackerrank.com/challenges/np-min-and-max/problem

Use the min and max tools of NumPy on the given 2-D array.
"""

import numpy

N, M = map(int, input().split())

list_array = []
for _ in range(N):
    row = list(map(int, input().split()))
    list_array.append(row)
np_array = numpy.array(list_array)

print(numpy.max(numpy.min(np_array, axis=1)))
