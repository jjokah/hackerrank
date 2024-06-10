"""
HackerRank Chanllenge: ginortS(Python)
https://www.hackerrank.com/challenges/ginorts/problem

An uneasy sort.
"""

S = input()

sorted_S = []
lower_S = []
upper_S = []
odd_S = []
even_S = []

for character in S:
    if character.islower():
        lower_S.append(character)
    if character.isupper():
        upper_S.append(character)
    if character.isdigit() and int(character) % 2 != 0:
        odd_S.append(character)
    if character.isdigit() and int(character) % 2 == 0:
        even_S.append(character)

sorted_S = sorted(lower_S) + sorted(upper_S) + sorted(odd_S) + sorted(even_S)

print("".join(sorted_S))
