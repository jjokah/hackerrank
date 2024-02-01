"""
Hackerrank Problem:
https://www.hackerrank.com/challenges/designer-door-mat/problem
"""

def print_welcome_pattern(M, N):
    pattern = ".|."
    welcome_message = "WELCOME"

    # Print the top part of the pattern
    for i in range(M // 2):
        line = (pattern * (2 * i + 1)).center(N, '-')
        print(line)

    # Print the welcome message
    print(welcome_message.center(N, '-'))

    # Print the bottom part of the pattern
    for i in range(M // 2 - 1, -1, -1):
        line = (pattern * (2 * i + 1)).center(N, '-')
        print(line)

# Example usage for a 7 x 21 pattern
print_welcome_pattern(11, 33)