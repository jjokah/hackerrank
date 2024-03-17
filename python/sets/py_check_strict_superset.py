"""
Hackerrank Problem:
https://www.hackerrank.com/challenges/py-check-strict-superset/problem
"""

A = set(map(int, input().split()))
n = int(input())
sss = "True"

for _ in range(n):
    B = set(map(int, input().split()))

    if not (A >= B):
        sss = "False"
        break

print(sss)
