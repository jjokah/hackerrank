"""
Hackerrank Problem:
https://www.hackerrank.com/challenges/py-set-add/problem
"""

N = int(input())
countries = set()

for _ in range(N):
    country = input()
    countries.add(country)

print(len(countries))
