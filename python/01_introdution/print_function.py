"""
Hackerrank problem: 
https://www.hackerrank.com/challenges/python-print/problem
"""

if __name__ == '__main__':
    n = int(input())
    combinedstr = ""
    
    for i in range(1, n+1):
        newstr = str(i)
        combinedstr = combinedstr + newstr
    
    print(int(combinedstr))
