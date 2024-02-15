"""
Hackerrank Problem:
https://www.hackerrank.com/challenges/no-idea/problem
"""

n, m = map(int, input().split())
array = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = 0

for i in array:
    if i in A:
        happiness += 1
    if i in B:
        happiness -= 1

print(happiness)