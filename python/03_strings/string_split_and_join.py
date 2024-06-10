"""
Hackerrank problem: 
https://www.hackerrank.com/challenges/python-string-split-and-join/problem
"""

def split_and_join(line):
    line_in_list = line.split()
    joined_with_dashes = "-".join(line_in_list)
    return joined_with_dashes

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)