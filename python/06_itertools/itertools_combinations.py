"""
HackerRank Chanllenge: itertools.combinations() (Python)
https://www.hackerrank.com/challenges/itertools-combinations/problem

Print all the combinations of a string using itertools.
"""

from itertools import combinations

S, k = input().split()
S = sorted(S)
k = int(k)

for each_k in range(1, k+1):
    for each_combo in combinations(S, each_k):
        print(''.join(each_combo))
