"""
HackerRank Challenge: Sum and Prod (Python)
https://www.hackerrank.com/challenges/np-sum-and-prod/problem

Perform the sum and prod functions of NumPy on the given 2-D array.
"""

import numpy

N, M = map(int, input().split())

list_array = []
for _ in range(N):
    row = list(map(int, input().split()))
    list_array.append(row)
np_array = numpy.array(list_array)

print(numpy.prod(numpy.sum(np_array, axis=0)))
