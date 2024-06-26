"""
HackerRank Challenge: Mean, Var, and Std (Python)
https://www.hackerrank.com/challenges/np-mean-var-and-std/problem

Use the mean, var and std tools in NumPy on the given 2-D array.
"""

import numpy

N, M = map(int, input().split())

list_array = []
for _ in range(N):
    row = list(map(int, input().split()))
    list_array.append(row)
np_array = numpy.array(list_array)

print(numpy.mean(np_array, axis=1))
print(numpy.var(np_array, axis=0))
print(round(numpy.std(np_array), 11))

# Note: to pass the test std value has to be rounded to 11 decimal placess