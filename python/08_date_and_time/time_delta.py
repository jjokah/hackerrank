"""
HackerRank Chanllenge: Time Delta (Python)
https://www.hackerrank.com/challenges/python-time-delta/problem

Find the absolute time difference.
"""

import os
from datetime import datetime


def time_delta(t1, t2):
    date_format = "%a %d %b %Y %H:%M:%S %z"
    t1 = datetime.strptime(t1, date_format)
    t2 = datetime.strptime(t2, date_format)

    return str(int(abs(t1-t2).total_seconds()))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
