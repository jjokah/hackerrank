"""
Hackerrank problem: Python If-Else


𝗧𝗮𝘀𝗸
Given an integer, 𝑛, perform the following conditional actions:
・ If 𝑛 is odd, print 𝚆𝚎𝚒𝚛𝚍
・ If 𝑛 is even and in the inclusive range of 𝟐 to 𝟓, print 𝙽𝚘𝚝 𝚆𝚎𝚒𝚛𝚍
・ If 𝑛 is even and in the inclusive range of 𝟔 to 𝟐𝟎, print 𝚆𝚎𝚒𝚛𝚍
・ If 𝑛 is even and greater than 𝟐𝟎, print 𝙽𝚘𝚝 𝚆𝚎𝚒𝚛𝚍


𝗜𝗻𝗽𝘂𝘁 𝗙𝗼𝗿𝗺𝗮𝘁
A single line containing a positive integer, 𝑛.
𝗖𝗼𝗻𝘀𝘁𝗿𝗮𝗶𝗻𝘁𝘀
・ 𝟏 ≤ 𝑛 ≤ 𝟏𝟎𝟎
𝗢𝘂𝘁𝗽𝘂𝘁 𝗙𝗼𝗿𝗺𝗮𝘁
Print 𝚆𝚎𝚒𝚛𝚍 if the number is weird. Otherwise, print Not Weird.


𝗦𝗮𝗺𝗽𝗹𝗲 𝗜𝗻𝗽𝘂𝘁 𝟬
```
3
```
𝗦𝗮𝗺𝗽𝗹𝗲 𝗢𝘂𝘁𝗽𝘂𝘁 𝟬
```
𝚆𝚎𝚒𝚛𝚍
```
𝗘𝘅𝗽𝗹𝗮𝗻𝗮𝘁𝗶𝗼𝗻 𝟬
𝑛 = 𝟑
𝑛 is odd and odd numbers are weird, so print 𝚆𝚎𝚒𝚛𝚍.


𝗦𝗮𝗺𝗽𝗹𝗲 𝗜𝗻𝗽𝘂𝘁 𝟏
```
24
```
𝗦𝗮𝗺𝗽𝗹𝗲 𝗢𝘂𝘁𝗽𝘂𝘁 𝟏
```
Not Weird
```
𝗘𝘅𝗽𝗹𝗮𝗻𝗮𝘁𝗶𝗼𝗻 𝟏
𝑛 = 𝟐𝟒
𝑛 > 𝟐𝟎 and 𝑛 is even, so it is not weird.
 
_
Source:
https://www.hackerrank.com/challenges/py-if-else/problem
"""


if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    else:
        if n in range(2, 6):
            print("Not Weird")
        if n in range(6, 21):
            print("Weird")
        if n > 20:
            print("Not Weird")
