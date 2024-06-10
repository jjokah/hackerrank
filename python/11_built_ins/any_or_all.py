"""
HackerRank Chanllenge: Any or All (Python)
https://www.hackerrank.com/challenges/any-or-all/problem

Return True, if any of the iterable is true or if all of it is true 
using the any() and all() expressions.
"""

N, integers = int(input()), list(map(int, input().split()))

print(all(x >= 0 for x in integers) and any(str(x) == str(x)[::-1] for x in integers))