"""
HackerRank Challenge: Dot and Cross (Python)
https://www.hackerrank.com/challenges/np-dot-and-cross/problem

Use NumPy to find the dot and cross products of arrays.
"""

import numpy

N = int(input())

list_array_A = []
for _ in range(N):
    row = list(map(int, input().split()))
    list_array_A.append(row)
np_array_A = numpy.array(list_array_A)

list_array_B = []
for _ in range(N):
    row = list(map(int, input().split()))
    list_array_B.append(row)
np_array_B = numpy.array(list_array_B)

print(numpy.dot(np_array_A, np_array_B))
