"""
HackerRank Challenge: Input() (Python)
https://www.hackerrank.com/challenges/input/problem

A Python 2 challenge: Input() is equivalent to eval(raw_input(prompt)).
"""

x, k = map(int, input().split())
result = eval(input().format(x=x))
print(k == result)
