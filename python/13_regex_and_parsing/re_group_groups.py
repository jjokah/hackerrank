"""
HackerRank Challenge: Group(), Groups() & Groupdict() (Python)
https://www.hackerrank.com/challenges/re-group-groups/problem

Using group(), groups(), and groupdict(), find the subgroup(s) of the match.
"""

import re

S = input()
m = re.search(r'([A-Za-z0-9])\1', S)
result = m.group(1) if m else -1
print(result)
