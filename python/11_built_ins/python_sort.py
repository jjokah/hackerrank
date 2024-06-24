"""
HackerRank Challenge: Athlete Sort (Python)
https://www.hackerrank.com/challenges/python-sort-sort/problem

Sort the table on the kth attribute.
"""

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    arr.sort(key=lambda x: x[k])

    for athlete in arr:
        print(*athlete)
