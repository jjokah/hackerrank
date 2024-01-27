"""
Hackerrank Problem:
https://www.hackerrank.com/challenges/python-string-formatting/problem
"""

def print_formatted(number):
    binary_width = len(f"{number:b}")
    
    for i in range(1, number+1):
        decimal = f"{i}"
        octal = f"{i:o}"
        hexa = f"{i:x}".upper()
        binary = f"{i:b}"
        
        # print the formatted numbers
        print(
            decimal.rjust(binary_width) + " " +
            octal.rjust(binary_width) + " "  +
            hexa.rjust(binary_width) + " " +
            binary.rjust(binary_width)
        )

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)