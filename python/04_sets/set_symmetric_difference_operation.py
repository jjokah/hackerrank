"""
Hackerrank Problem:
https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
"""

english_total = int(input())
english_studs = set(map(int, input().split()))
french_total = int(input())
french_studs = set(map(int, input().split()))

print(len(english_studs ^ french_studs))
