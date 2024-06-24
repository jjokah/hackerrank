"""
HackerRank Challenge: Exceptions (Python)
https://www.hackerrank.com/challenges/exceptions/problem

Handle errors detected during execution.
"""

T = int(input())

for _ in range(T):
    try:
        a, b = map(int, input().split())
        print(a // b)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)
