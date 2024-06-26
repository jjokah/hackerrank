"""
HackerRank Challenge: Linear Algebra (Python)
https://www.hackerrank.com/challenges/np-linear-algebra/problem

NumPy routines for linear algebra calculations.
"""

import numpy

N = int(input())
array_A = []
for _ in range(N):
    row = list(map(float, input().split()))
    array_A.append(row)

print(round(numpy.linalg.det(array_A), 2))
