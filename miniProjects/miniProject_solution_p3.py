# GPA calculator
# 1. function needs to take in a subject for the GPA - math, history, etc
# 2. function needs to take in a grade 17 times - 1 grade for each of the 17 weeks
# 3. function needs to add all the grades up and divide by 17
# 4. function needs to tell the user the letter grade based on number
# 70-80 = c
# 80-90 = b
# 90-100 = a 

def gpaCalculator():
    print('What subject is this GPA for? ')
    subject=  input()
    print('the user typed in: ' + subject)

    sum = 0
    weekcount= 1
    # while weekcount != 17: # Change this line of code from using a WHILE loop into using a FOR loop
    for weekcount in range(1,17): 
        print('what is the grade for week '+ str(weekcount))
        grade = int(input())
        sum += grade
        weekcount += 1
        gpa = sum / weekcount
        print('your gpa is :' + str(gpa))
        if gpa > 70 and gpa < 80:
            print("C")
        elif gpa > 80 and gpa < 90:
            print("B")
        elif gpa > 90 and gpa < 100:
            print("A")  
gpaCalculator()

    # wk1 = int(input("please type the grade for week 1: "))
    # wk2 = int(input("please type the grade for week 2: "))
    # wk3 = int(input("please type the grade for week 3: "))
    # wk4 = int(input("please type the grade for week 4: "))
    # sum = wk1 +wk2+ wk3+ wk4
    # gpa = sum/4
    # print(sum)
    # print(gpa)