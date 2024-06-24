"""
HackerRank Challenge: Iterables and Iterators (Python)
https://www.hackerrank.com/challenges/iterables-and-iterators/problem

Find the probability using itertools.
"""

from itertools import combinations

N = int(input())
S = input().split(' ')
K = int(input())

comb = list(combinations(S, K))
prob = 0

for combination in comb:
    if 'a' in combination:
        prob += 1

print(prob/len(comb))