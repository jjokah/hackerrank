"""
Hackerrank Problem:
https://www.hackerrank.com/challenges/symmetric-difference/problem
"""

M = int(input())
set_a = set(map(int, input().split()))
N = int(input())
set_b = set(map(int, input().split()))

a_diff = set_a.difference(set_b)
b_diff = set_b.difference(set_a)
symmetric_diff = a_diff.union(b_diff)

for i in sorted(symmetric_diff):
    print(i)