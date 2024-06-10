"""
Hackerrank Problem:
https://www.hackerrank.com/challenges/py-set-mutations/problem
"""

A_length = int(input())
A = set(map(int, input().split()))
N_other_sets = int(input())

for _ in range(N_other_sets):
    operation, other_set_length = input().split()
    other_set = set(map(int, input().split()))

    if operation == "update":
        A |= other_set
    elif operation == "intersection_update":
        A &= other_set
    elif operation == "difference_update":
        A -= other_set
    elif operation == "symmetric_difference_update":
        A ^= other_set
    else:
        pass

print(sum(A))
