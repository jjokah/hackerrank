"""
Hackerrank Problem:
https://www.hackerrank.com/challenges/py-the-captains-room/problem
"""

k = int(input())
l = list(map(int, input().split()))
s = set(l)

for i in s:
    l.remove(i)
    if i not in l:
        print(i)