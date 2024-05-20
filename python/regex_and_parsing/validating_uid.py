"""
HackerRank Chanllenge: Detect HTML Tags, Attributes and Attribute Values (Python)
https://www.hackerrank.com/challenges/validating-uid/problem

Validate all the randomly generated user identification numbers according to the constraints.
"""

import re

T = int(input())

for _ in range(T):
    UID = input()
    rgx = r'^(?=(?:.*[A-Z]){2,})(?=(?:.*\d){3,})(?!.*(.).*\1)[A-Za-z0-9]{10}$'
    regex_match = re.match(rgx, UID)
    print("Valid") if regex_match else print("Invalid")
