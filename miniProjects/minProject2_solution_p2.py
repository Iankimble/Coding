# 1. need to have function take in a subject
# 2. need the function to take in 17 numbers - 1 for each week
# 3. need to add up all 17 numbers and then divide by 17
# 4. need to turn the number grade into a letter grade and show the use both

def gpaCalculator():
    subject= input('What subject is this GPA for? ')
    print('The subject the user typed is :' + subject)
    finalSum = 0
    weekCount = 1
    while weekCount != 17: # Change this block from using a while into a FOR loop
        print('what is the grade  or week ' + str(weekCount))
        grade = int(input())
        finalSum += grade
        print(finalSum)
        weekCount += 1    
    finalGPA = finalSum/ 17
    print('Your GPA is: '+ str(finalGPA)) 
    if finalGPA > 70 and finalGPA < 80:
        print('C')
    elif finalGPA >80 and finalGPA < 90:
        print('B')
    elif finalGPA > 90 and finalGPA < 100:
        print('A')

gpaCalculator()