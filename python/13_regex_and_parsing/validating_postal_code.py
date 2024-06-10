"""
HackerRank Chanllenge: Validating Postal Code (Python)
https://www.hackerrank.com/challenges/validating-postalcode/problem

Verify whether postal codes are valid or not.
"""

regex_integer_in_range = r"^[1-9]\d{5}$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	


import re

P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)