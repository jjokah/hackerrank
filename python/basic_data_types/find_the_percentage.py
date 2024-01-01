"""
Hackerrank problem: 
https://www.hackerrank.com/challenges/finding-the-percentage/problem
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    selected_scores = student_marks[query_name]
    average = sum(selected_scores)/len(selected_scores)
    average_2dp = f"{average:.2f}"
    print(average_2dp)
