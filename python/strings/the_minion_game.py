"""
Hackerrank Problem:
https://www.hackerrank.com/challenges/the-minion-game/problem
"""

def minion_game(string):
    # Define vowels
    vowels = "AEIOU"
    # Initialize scores for Stuart and Kevin
    stuart_score = 0
    kevin_score = 0

    # Iterate through the string
    for i in range(len(string)):
        # Check if the current letter is a vowel
        if string[i] in vowels:
            # If it's a vowel, add the count of remaining substrings to Kevin's score (permutation of remaining substring)
            kevin_score += len(string) - i
        else:
            # If it's a consonant, add the count of remaining substrings to Stuart's score (permutation of remaining substring)
            stuart_score += len(string) - i

    # Compare scores and print the result
    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        # If scores are equal, it's a draw
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)