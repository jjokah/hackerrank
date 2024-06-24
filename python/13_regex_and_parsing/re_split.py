"""
HackerRank Challenge: Re.split() (Python)
https://www.hackerrank.com/challenges/re-split/problem

Split the string by the pattern occurrence using the re.split() expression.
"""

import re

regex_pattern = r"[.,]"
print("\n".join(re.split(regex_pattern, input())))