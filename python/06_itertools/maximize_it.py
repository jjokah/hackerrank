"""
HackerRank Challenge: Maximize It! (Python)
https://www.hackerrank.com/challenges/maximize-it/problem

Find the maximum possible value out of the equation provided.
"""

from itertools import product

K, M = map(int, input().split())

# get input of each line, split to a list, and place all in a list
lists = [input().split()[1:] for _ in range(K)]
# unpack the list of list to all possible permutation, as a list of tuple
possibles = product(*lists)
# modules of the sum of the square of each possible combination 
moduli = [sum(int(x) **2 for x in item)%M for item in possibles] 

print(max(moduli))
