"""
Hackerrank Problem:
https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
"""

n = int(input())
s = set(map(int, input().split()))

N = int(input())

for _ in range(N):
    command = input()
    try:
        command_str, command_value = command.split()
        command_value = int(command_value)
        if command_str == "remove":
            s.remove(command_value)
        elif command_str == "discard":
            s.discard(command_value)
    except ValueError:
        command_str = command
        if command_str == "pop":
            s.pop()


print(sum(s))