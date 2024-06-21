"""
HackerRank Chanllenge: Concatenate (Python)
https://www.hackerrank.com/challenges/np-concatenate/problem

Use the concatenate function on 2 arrays.
"""

import numpy

N, M, P = map(int, input().split())

list_1 = []
for _ in range(N):
    row = list(map(int, input().split()))
    list_1.append(row)

array_1 = numpy.array(list_1)

list_2 = []
for _ in range(M):
    row = list(map(int, input().split()))
    list_2.append(row)
array_2 = numpy.array(list_2)

print(numpy.concatenate((array_1, array_2), axis=0))
