"""
Hackerrank Problem:
https://www.hackerrank.com/challenges/alphabet-rangoli/problem
"""

def print_rangoli(size):
    import string
    
    # Create a list of alphabets
    alphabets = string.ascii_lowercase
    
    # Create a list to store each line of the rangoli
    rangoli_lines = []

    # Calculate line length
    line_length = size * 4 - 3
    
    # Build the top of rangoli
    for i in reversed(range(size)):
        # Create the letters for each line of the rangoli, joined by '-'
        letters = '-'.join(alphabets[size-1:i:-1] + alphabets[i:size])
        
        # Center the letters and fill the remaining space with '-'
        line = letters.center(line_length, '-')
        
        # Append the line to the list
        rangoli_lines.append(line)

    # Build the bottom of rangoli
    for i in range(size):
        # Avoid duplicating the middle line
        if i == 0:
            continue

        # Create the letters for each line of the rangoli, joined by '-'
        letters = '-'.join(alphabets[size-1:i:-1] + alphabets[i:size])
        
        # Center the letters and fill the remaining space with '-'
        line = letters.center(line_length, '-')
        
        # Append the line to the list
        rangoli_lines.append(line)
    
    # Print the rangoli to complete the pattern
    print('\n'.join(rangoli_lines[::]))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)