"""
HackerRank Chanllenge: collections.deque() (Python)
https://www.hackerrank.com/challenges/py-collections-deque/problem

Perform multiple operations on a double-ended queue or deque.
"""

from collections import deque

d = deque()

for _ in range(int(input())):
    command = input().split()
    match command[0]:
        case 'append':
            d.append(command[1])
        case 'appendleft':
            d.appendleft(command[1])
        case 'pop':
            d.pop()
        case 'popleft':
            d.popleft()

print(*d)