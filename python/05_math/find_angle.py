"""
HackerRank Challenge: Find Angle MBC (Python)
https://www.hackerrank.com/challenges/find-angle/problem

Find the desired angle in the right triangle.
"""

# the solution works for angle ACB not angle MBC

import math

AB = int(input())
BC = int(input())

angle_ACB = math.atan(AB/BC)

angle_ACB = math.degrees(angle_ACB)

angle_ACB = round(angle_ACB)

print(f"{angle_ACB}{chr(176)}")
