"""
Hackerrank problem: 
https://www.hackerrank.com/challenges/string-validators/problem
"""

if __name__ == '__main__':
    s = input()
    alnum = False
    alpha = False
    digit = False
    lowercase = False
    uppercase = False
    
    for i in s:
        if i.isalnum():
            alnum = True
        if i.isalpha():
            alpha = True
        if i.isdigit():
            digit = True
        if i.islower():
            lowercase = True
        if i.isupper():
            uppercase = True
            
print("True") if alnum else print("False")
print("True") if alpha else print("False")
print("True") if digit else print("False")
print("True") if lowercase else print("False")
print("True") if uppercase else print("False")
