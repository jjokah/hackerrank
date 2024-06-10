"""
HackerRank Chanllenge: DefaultDict Tutorial (Python)
https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

Create dictionary value fields with predefined data types.
"""

# Importing defaultdict from collections module
from collections import defaultdict

# Taking input for the values of n and m separated by spaces, 
# ...then mapping them to integers
n, m = map(int, input().split())

# Creating a defaultdict where the default value is an empty list
A = defaultdict(list)

# Using list comprehensions to iterate over the range of n and m respectively
# For each index i in the range of n, input a value and append i+1 
# ...to the list associated with that value in the dictionary A
[A[input()].append(i+1) for i in range(n)]

# For each index in the range of m, input a value
# Use the input value as a key to retrieve the corresponding list 
# ...from dictionary A using get() method
# If the key is not found in dictionary A, return [-1] (default value) and print it
# Otherwise, print the elements of the list associated with the key, separated by spaces
[print(*A.get(input(),[-1])) for _ in range(m)]
