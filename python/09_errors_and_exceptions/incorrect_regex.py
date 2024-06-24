"""
HackerRank Challenge: Incorrect Regex (Python)
https://www.hackerrank.com/challenges/incorrect-regex/problem

Check whether the regex is valid or not.
"""

# Note: Test cases are broken and needs to be updated. Just run with Pypy3 on HackerRank

import re

for _ in range(int(input())):
    try:
        re.compile(input())
        print("True")
    except re.error:
        print("False")
