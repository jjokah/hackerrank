"""
HackerRank Challenge: Array Mathematics (Python)
https://www.hackerrank.com/challenges/np-array-mathematics/problem

Perform basic mathematical operations on arrays in NumPy.
"""

import numpy


N, M = map(int, input().split())

# create first numpy array
array_A = []
for _ in range(N):
    row = list(map(int, input().split()))
    array_A.append(row)
array_A = numpy.array(array_A, int)

# create second numpy array
array_B = []
for _ in range(N):
    row = list(map(int, input().split()))
    array_B.append(row)
array_B = numpy.array(array_B, int)

# perform math operations
print(array_A + array_B)
print(array_A - array_B)
print(array_A * array_B)
print(array_A // array_B)
print(array_A % array_B)
print(array_A ** array_B)