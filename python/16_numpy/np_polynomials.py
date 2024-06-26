"""
HackerRank Challenge: Polynomials (Python)
https://www.hackerrank.com/challenges/np-polynomials/problem

Given the coefficients, use polynomials in NumPy.
"""

import numpy

P = list(map(float, input().split()))
x = int(input())
print(numpy.polyval(P, x))
