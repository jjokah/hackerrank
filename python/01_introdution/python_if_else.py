"""
Hackerrank problem: Python If-Else

𝗧𝗮𝘀𝗸
Given an integer, 𝑛, perform the following conditional actions:
・ If 𝑛 is odd, print 𝚆𝚎𝚒𝚛𝚍
・ If 𝑛 is even and in the inclusive range of 𝟐 to 𝟓, print Not Weird
・ If 𝑛 is even and in the inclusive range of 𝟔 to 𝟐𝟎, print 𝚆𝚎𝚒𝚛𝚍
・ If 𝑛 is even and greater than 𝟐𝟎, print Not Weird

𝗜𝗻𝗽𝘂𝘁 𝗙𝗼𝗿𝗺𝗮𝘁
A single line containing a positive integer, 𝑛.

𝗖𝗼𝗻𝘀𝘁𝗿𝗮𝗶𝗻𝘁𝘀
・ 

𝗢𝘂𝘁𝗽𝘂𝘁 𝗙𝗼𝗿𝗺𝗮𝘁
Print Weird if the number is weird. Otherwise, print Not Weird.

𝗦𝗮𝗺𝗽𝗹𝗲 𝗜𝗻𝗽𝘂𝘁 𝟬
```
3
```

𝗦𝗮𝗺𝗽𝗹𝗲 𝗢𝘂𝘁𝗽𝘂𝘁 𝟬
```
𝚆𝚎𝚒𝚛𝚍
```

𝗘𝘅𝗽𝗹𝗮𝗻𝗮𝘁𝗶𝗼𝗻 𝟬
 is odd and odd numbers are weird, so print Weird.

Sample Input 1

24
Sample Output 1

Not Weird
Explanation 1


 and  is even, so it is not weird.

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
