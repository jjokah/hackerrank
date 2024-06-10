"""
HackerRank Chanllenge: itertools.combinations_with_replacement() (Python)
https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

Find all the combinations of a string with replacements.
"""

from itertools import combinations_with_replacement

S, k = input().split()
S = sorted(S)
k = int(k)

for i in combinations_with_replacement(S, k):
    print(''.join(i))