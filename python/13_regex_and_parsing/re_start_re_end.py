"""
HackerRank Challenge: Re.start() & Re.end() (Python)
https://www.hackerrank.com/challenges/re-start-re-end/problem

Find the indices of the start and end of the substring matched by the group.
"""

import re

S = input()
k = input()

pattern = re.compile(f'(?=({k}))')

matches = list(re.finditer(pattern, S))

if matches:
    for match in matches:
        print((match.start(), match.end() + len(k) -1))
else:
    print((-1, -1))
