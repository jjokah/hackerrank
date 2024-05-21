"""
HackerRank Chanllenge: Validating Credit Card Numbers (Python)
https://www.hackerrank.com/challenges/validating-credit-card-number/problem

Verify whether credit card numbers are valid or not.
"""

import re

for _ in range(int(input())):
    cc_number = input()
    pattern = r'^(?!.*(\d)(-?\1){3,})[4-6]\d{3}(-?\d{4}){3}$'
    regex_match = re.match(pattern, cc_number)
    print('Valid') if regex_match else print('Invalid')
