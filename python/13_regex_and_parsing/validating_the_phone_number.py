"""
HackerRank Chanllenge: Validating Phone Numbers (Python)
https://www.hackerrank.com/challenges/validating-the-phone-number/problem

Check whether the given phone number is valid or not.
"""

import re

for _ in range(int(input())):
    print("YES") if (bool(re.match(r'^[789]\d{9}$', input()))) else print("NO")