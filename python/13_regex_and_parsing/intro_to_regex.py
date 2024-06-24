"""
HackerRank Challenge: Detect Floating Point Number (Python)
https://www.hackerrank.com/challenges/introduction-to-regex/problem

Validate a floating point number using the regular expression module for Python.
"""

import re

T = int(input())
for i in range(T):
    N = input()
    pattern = r'^[+-]?\d*\.\d+$'
    print(bool(re.match(pattern, N)))
