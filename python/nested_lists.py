"""
Hackerrank problem: 
https://www.hackerrank.com/challenges/nested-list/problem
"""

if __name__ == '__main__':
    pystudent = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        pystudent.append(list((name, score)))
    
    lowest_grade = 9999
    for record in pystudent:
        student_score = record[1]
        
        if student_score < lowest_grade:
            lowest_grade = student_score
    
    second_lowest = 9999
    for record in pystudent:
        student_score = record[1]
        
        if student_score < second_lowest and student_score > lowest_grade:
            second_lowest = student_score
    
    second_lowest_names = []
    for record in pystudent:
        student_score = record[1]
        
        if student_score == second_lowest:
            second_lowest_names.append(record[0])
            
    second_lowest_names.sort()
    for name in second_lowest_names:
        print(name)
        
