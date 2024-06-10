"""
HackerRank Chanllenge: Triangle Quest 2 (Python)
https://www.hackerrank.com/challenges/triangle-quest-2/problem

Create a palindromic triangle.
"""

# More than 2 lines will result in 0 score. Do not leave a blank line also

for i in range(1,int(input())+1): 
    print(int((10 ** i-1)/9) ** 2)
