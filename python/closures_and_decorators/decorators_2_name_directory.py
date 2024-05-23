"""
HackerRank Chanllenge: Decorators 2 Name Directory (Python)
https://www.hackerrank.com/challenges/decorators-2-name-directory/problem

Use decorators to build a name directory.
"""

def person_lister(f):
    def inner(people):
        people.sort(key=lambda x: (int(x[2])))
        for person in people:
            yield f(person)
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')