"""
HackerRank Chanllenge: Calendar Module (Python)
https://www.hackerrank.com/challenges/calendar-module/problem

Print the day of a given date.
"""

import calendar

m, d, y = map(int, input().split())
n = calendar.weekday(y, m, d)
day = calendar.day_name[n]
print(day.upper())