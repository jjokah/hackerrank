"""
Hackerrank problem: 
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
"""

if __name__ == '__main__':
    n = int(input())
    # convert input to list of integers
    scores = list(map(int, input().split()))
    
    # sort the scores in descending order
    scores.sort(reverse=True)
    
    # finding runner up score
    # loop through and check for score less than the highest
    maxscore = scores[0]
    for score in scores:
        if score < maxscore:
            print(score)
            break
        
