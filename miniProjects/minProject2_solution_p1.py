# GPA calculator
# 1. need to take in user input for subject- can be any school subject
# 2. need to take in a grade 17 times. each grade representing each week in the 
# semester.
# 3. once I have all 17 grades, I need to add them up, and then divide by 17
# 4. once I have the number grade, I need to write some code to transform
# it into a letter grade

def gpaCalculator():
    print(' What subject is this GPA for? ')
    subject = input()
    print("the user entered: "+ subject)
    week = 1
    sum = 0
    while week != 10:
        print('Please enter the grade for week : '+ str(week))
        grade = int(input())
        sum += grade
        week += 1
        gpa = sum / 10
    if gpa > 70 and gpa < 80:
        print('C')
    elif gpa > 80  and gpa < 90:
        print('B')
    elif gpa > 90  and gpa <100:
        print('A')
    else:
        print('F')
    print('your gpa for '+ subject + ' is ' + str(gpa))

gpaCalculator()