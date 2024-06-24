"""
HackerRank Challenge: Eye and Identity (Python)
https://www.hackerrank.com/challenges/np-eye-and-identity/problem

Create an array using the identity or eye tools from the NumPy module.
"""

import numpy

numpy.set_printoptions(legacy='1.13')

N, M = map(int, input().split())
print(numpy.eye(N, M))
