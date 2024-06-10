"""
Hackerrank Problem:
https://www.hackerrank.com/challenges/py-set-union/problem
"""

en_num = int(input())
en_students = set(map(int, input().split()))
fr_num = int(input())
fr_students = set(map(int, input().split()))

print(len(en_students.union(fr_students)))
