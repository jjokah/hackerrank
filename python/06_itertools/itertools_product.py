"""
HackerRank Challenge: itertools.products() (Python)
https://www.hackerrank.com/challenges/itertools-product/problem

Find the cartesian product of two lists.
"""

from itertools import product

A = map(int, input().split())
B = map(int, input().split())

cp = list(product(A, B))

for i in cp:
    print(i, end=' ')