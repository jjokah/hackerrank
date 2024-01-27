"""
Hackerrank problem: 
https://www.hackerrank.com/challenges/swap-case/problem
"""

def swap_case(s):
    new_string = ""
    for char in s:
        if char.islower():
            new_string += char.upper()
        elif char.isupper():
            new_string += char.lower()
        else:
            new_string += char
    return new_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)