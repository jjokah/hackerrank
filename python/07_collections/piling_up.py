"""
HackerRank Challenge: Piling Up! (Python)
https://www.hackerrank.com/challenges/piling-up/problem

Create a vertical pile of cubes.
"""

from collections import deque

for _ in range(int(input())):
    tower = deque()

    # Taking input for the size of the tower (which is not used), 
    # ...and creating a deque from the input numbers
    _, d = input(), deque(map(int, input().split()))

    # Looping over the length of the deque
    for _ in range(len(d)):
        # Checking whether the first or the last element of the deque is larger
        if [d[0], d[-1]].index(max([d[0], d[-1]])):
            # If the last element is larger, it's appended to the left of the 'tower'
            tower.appendleft(d.pop())
        else:
            # Otherwise, the first element is appended to the left of the 'tower'
            tower.appendleft(d.popleft())

    # Checking if the 'tower' is sorted in ascending order
    # ...and printing "Yes" or "No" accordingly
    print("Yes" if list(tower) == sorted(tower) else "No")
