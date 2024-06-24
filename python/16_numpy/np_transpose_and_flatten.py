"""
HackerRank Challenge: Transpose and Flatten (Python)
https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem

Use the transpose and flatten tools in the NumPy module to manipulate an array.
"""

import numpy


N, M = map(int, input().strip().split())
my_list = []
for _ in range(N):
    row_list = list(map(int, input().strip().split()))
    my_list.append(row_list)

my_array = numpy.array(my_list)
print(numpy.transpose(my_array))
print(my_array.flatten())
