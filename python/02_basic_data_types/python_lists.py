"""
Hackerrank problem: 
https://www.hackerrank.com/challenges/python-lists/problem
"""

if __name__ == '__main__':
    N = int(input())
    mylist = []
    
    def execute_command(command):
        command = command.split()
        primary_command = command[0].lower()
        
        # insert command
        if primary_command == "insert":
            position_i = int(command[1])
            integer_e = int(command[2])
            mylist.insert(position_i, integer_e)
            
        # print command
        elif primary_command == "print":
            print(mylist)
            
        # remove command
        elif primary_command == "remove":
            integer_e = int(command[1])
            mylist.remove(integer_e)
            
        # append command
        elif primary_command == "append":
            integer_e = int(command[1])
            mylist.append(integer_e)
            
        # sort command
        elif primary_command == "sort":
            mylist.sort()
            
        # pop command
        elif primary_command == "pop":
            mylist.pop()
            
        # reverse command
        elif primary_command == "reverse":
            mylist.reverse()
            
            
    
    for _ in range(N):
        command = input()
        execute_command(command)