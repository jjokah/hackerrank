"""
Hackerrank problem: 
https://www.hackerrank.com/challenges/text-wrap/problem
"""

import textwrap

def wrap(string, max_width):
    wrap_list = textwrap.wrap(width=max_width, text=string)
    wrapped_string = '\n'.join(wrap_list)

    return wrapped_string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)