"""
HackerRank Challenge: collections.Counter() (Python)
https://www.hackerrank.com/challenges/collections-counter/problem

Use a counter to sum the amount of money earned by the shoe shop owner.
"""

from collections import Counter

X = int(input())
shoe_sizes = map(int, input().split())
N = int(input())
willing_to_pay = [tuple(map(int, input().split())) for _ in range(N)]
earned = 0

shoe_sizes_counter = Counter(shoe_sizes)

for size, price in willing_to_pay:
    if size not in shoe_sizes_counter: # size not available
        continue
    else:
        if shoe_sizes_counter[size] < 1: # size no longer available
            continue
        else: # available
            earned += price # add price of shoe to the total earned
            shoe_sizes_counter[size] -= 1 # reduce quantity after purchase


print(earned)