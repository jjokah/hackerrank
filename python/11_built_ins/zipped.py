"""
HackerRank Challenge: Zipped!(Python)
https://www.hackerrank.com/challenges/zipped/problem

Compute the average by zipping data.
"""


record = [tuple(map(float, input().split())) for _ in range(int(input().split()[1]))]
record = zip(*record)
[print(round(sum(i)/len(i), 1)) for i in record]


# This is another solution to the challenge.

# N, X = map(int, input().split())
# record = []
# for _ in range(X):
#     subject = tuple(map(float, input().split()))
#     record.append(subject)

# record = zip(*record)

# for i in record:
#     average = sum(i)/len(i)
#     print(round(average, 1))
