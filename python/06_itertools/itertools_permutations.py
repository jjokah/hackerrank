"""
HackerRank Challenge: itertools.permutations() (Python)
https://www.hackerrank.com/challenges/itertools-permutations/problem

Find all permutations of a given size in a given string.
"""

from itertools import permutations

S, k = input().split()
k = int(k)

for i in sorted(permutations(S, k)):
    print("".join(i))
