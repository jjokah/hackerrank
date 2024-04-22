"""
HackerRank Chanllenge: Validating and Parsing Email Addresses (Python)
https://www.hackerrank.com/challenges/validating-named-email-addresses/problem

Print valid email addresses according to the constraints.
"""

import re
from email.utils import formataddr, parseaddr

pattern = r"^[a-zA-Z][\w_\-\.]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$"

n = int(input())
for _ in range(n):
    name_email = input()
    name_email = parseaddr(name_email)
    email = name_email[1]

    if bool(re.match(pattern, email)):
        print(formataddr(name_email))
