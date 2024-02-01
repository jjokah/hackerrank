"""
Hackerrank Problem:
https://www.hackerrank.com/challenges/capitalize/problem
"""

# Complete the solve function below.
def solve(s):
    return ' '.join([name.capitalize() for name in s.split(' ')])

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)