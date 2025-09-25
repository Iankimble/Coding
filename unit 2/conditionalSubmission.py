# Activity 1
# Create a function that will check whether a student is old 
# enough to get there drivers permit. Your function should accept 
# 1 parameter. If the user is 16 and older, your function should
# return a message saying they can begin the process of getting 
# their driver's permit. Otherwise, your function should 
# inform the user they are not old enough.

def permitAgeCheck(age):
    if age >= 16:
        print("Congrats! You are eligible to get your driver permit.")
    else:
        print("Sorry, you are too young at this time.")

permitAgeCheck(16)

# Activity 2
# Create a function that will determine if a number is positive of negative.
# if a number is positive, it should print a message saying "this is positive".
# otherwise, the number must be negative. 

# Activity 3
# Create a grade score checker function that allows a student to enter
# their numerical grade, and show them the letter grade. Your function 
# should be able to process the grades as followed. If a grade number is 
# below a 70, it is an F. if a grade is above 70 and below 80, it is a C.
# if a grade is above 80 and below 90, it is a B.  
# and lastly is a grade is above 90, its an A.

