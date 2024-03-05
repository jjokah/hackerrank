"""
Hackerrank Problem:
https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
"""

english_total = int(input())
english_list = set(map(int, input().split()))
french_total = int(input())
french_list = set(map(int, input().split()))

print(len(english_list & french_list))
