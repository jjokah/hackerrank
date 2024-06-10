"""
HackerRank Chanllenge: Compress the String! (Python)
https://www.hackerrank.com/challenges/compress-the-string/problem

groupby()
"""

from itertools import groupby

S = input()

[print((len(list(group)), int(key)), end=' ') for key, group in groupby(S)]
