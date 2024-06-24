"""
HackerRank Challenge: Re.findall() & Re.finditer() (Python)
https://www.hackerrank.com/challenges/re-findall-re-finditer/problem

Find all the pattern matches using the expressions re.findall() and re.finditer().
"""

import re

S = input()
pattern = r'(?<=[^aeiouAEIOU])[aeiouAEIOU]{2,}(?=[^aeiouAEIOU])'

vowels_list = re.findall(pattern, S)

if vowels_list:
    print(*vowels_list, sep="\n")
else:
    print(-1)



