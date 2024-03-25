"""
HackerRank Chanllenge: Word Order (Python)
https://www.hackerrank.com/challenges/word-order/problem

List the number of occurrences of the words in order.
"""

from collections import Counter

c = Counter()

for _ in range(int(input())):
    c.update(input().split())

print(len(c.keys()))
print(*c.values())