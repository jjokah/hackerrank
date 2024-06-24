"""
HackerRank Challenge: Triangle Quest (Python)
https://www.hackerrank.com/challenges/python-quest-1/problem

Print a numeric triangle of height N-1 using only 2 lines.
"""

# More than 2 lines will result in 0 score. Do not leave a blank line also

for i in range(1,int(input())):
    print(((10 ** i-1) // 9) * i)
