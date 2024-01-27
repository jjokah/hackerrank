"""
Hackerrank problem: 
https://www.hackerrank.com/challenges/find-a-string/problem
"""

def count_substring(string, sub_string):
    count = 0
    substring_length = len(sub_string)
    string_length = len(string)
    length_to_check = string_length - substring_length + 1
    for i in range(length_to_check):
        each_sub_string = string[i:i+substring_length]
        if sub_string == each_sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)