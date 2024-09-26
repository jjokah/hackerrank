"""
Hackerrank problem: Find the Runner-Up Score!

Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given 𝑛 scores. Store them in a list and find the score of the runner-up.

𝗜𝗻𝗽𝘂𝘁 𝗙𝗼𝗿𝗺𝗮𝘁
The first line contains 𝑛. The second line contains an array 𝐴[] of 𝑛 of  integers each separated by a space.

𝗖𝗼𝗻𝘀𝘁𝗿𝗮𝗶𝗻𝘁𝘀
・ 2 ≤ 𝑛 ≤ 10
・ -100 ≤ 𝐴[𝑖] ≤ 100

𝗢𝘂𝘁𝗽𝘂𝘁 𝗙𝗼𝗿𝗺𝗮𝘁
Print the runner-up score.

𝗦𝗮𝗺𝗽𝗹𝗲 𝗜𝗻𝗽𝘂𝘁 𝟬
```
5
2 3 6 6 5
```

𝗦𝗮𝗺𝗽𝗹𝗲 𝗢𝘂𝘁𝗽𝘂𝘁 𝟬
```
5
```

𝗘𝘅𝗽𝗹𝗮𝗻𝗮𝘁𝗶𝗼𝗻 𝟬
Given list is [𝟐,𝟑,𝟔,𝟔,𝟓]. The maximum score is 𝟔, second maximum is 𝟓. Hence, we print  as the runner-up score.

_
Source:
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
        
