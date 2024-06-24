"""
HackerRank Challenge: Company Logo (Python)
https://www.hackerrank.com/challenges/most-commons/problem

Print the number of character occurrences in descending order.
"""

from collections import Counter

s = Counter(sorted(input()))

for letter, occurence in s.most_common(3):
    print(letter, occurence)