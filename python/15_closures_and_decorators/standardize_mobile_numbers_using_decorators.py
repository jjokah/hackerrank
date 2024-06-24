"""
HackerRank Challenge: Standardize Mobile Number Using Decorators (Python)
https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem

Use decorators to standardize mobile numbers.
"""

def wrapper(f):
    def fun(l):
        return f([f'+91 {mobile[-10:-5]} {mobile[-5:]}' for mobile in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 

