"""
HackerRank Chanllenge: Polar Coordinates
https://www.hackerrank.com/challenges/polar-coordinates/problem

Convert complex numbers to polar coordinates
"""

from cmath import phase

z = complex(input())
r = abs(z)
phi = phase(z)
print(r)
print(phi)