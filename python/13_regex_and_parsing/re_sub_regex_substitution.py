"""
HackerRank Challenge: Regex Substitution (Python)
https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem

Substitute a string using regex tools.
"""

import re

for line in range(int(input())):
    string = ''
    string = re.sub(r'(?<= )&&(?= )', 'and', input())
    string = re.sub(r'(?<= )\|\|(?= )', 'or', string)
    print(string)
