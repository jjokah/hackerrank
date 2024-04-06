"""
HackerRank Chanllenge: Map and Lambda Function (Python)
https://www.hackerrank.com/challenges/map-and-lambda-expression/problem

This challenge covers the basic concept of maps and lambda expressions.
"""

# cube list
cube = lambda x: x**3


# list of fibonacci numbers
def fibonacci(n):
    fib_list = []
    a, b = 0, 1
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
