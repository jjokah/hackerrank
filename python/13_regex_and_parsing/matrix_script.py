"""
HackerRank Chanllenge: Matrix Script (Python)
https://www.hackerrank.com/challenges/matrix-script/problem

Decode the Matrix.
"""

import re
from itertools import chain

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

decoded_matrix_script = ""

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

s = "".join(list(chain.from_iterable(zip(*matrix))))
print(re.sub(r"\b\W+\b", " ", s))
