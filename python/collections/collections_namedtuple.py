"""
HackerRank Chanllenge: collections.namedtuple() (Python)
https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

You need to turn tuples into convenient containers using collections.namedtuple().
"""

from collections import namedtuple

N = int(input())
StudentInfo = namedtuple('std_info', ",".join(input().split()))

# Calculating the average marks of the students and printing it with two decimal places
# Calculating the average marks by summing up the marks of all students 
# ...and dividing by the total number of students
# List comprehension to iterate over each student's input and extract their marks
print("{0:2f}".format(sum([int(StudentInfo(*input().split()).MARKS) for _ in range(N)]) / N))