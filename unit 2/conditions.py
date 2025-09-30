# Conditional Statements - code instructions that
# have different outcomes based on the inputted data. 
# input --> condition --> output

# Conditional Statement Syntax
# if keyword - Controls the condition we want to satisfy.

# elif keyword - same thing as the if keyword. 

# else keyword - Our default outcome. The thing that
# happens when our conditions are NOT satisfied. 

def weather():
    weather = input('what is the weather like today? ')
    if weather == 'sunny':
        print(" It is beautfiul outside. Bring sunglasses.")
    elif weather =='rainy':
        print(" Remember to bring an umbrella.")
    elif weather == 'windy':
        print("Wear heavy boots.")
    elif weather == 'chilly':
        print("bring a jacket.")
    else:
        print("I cant tell you the weather, but have a good day.")

vanilla = 20 # number of ice cream bar in stock.
chocolate = 10 
strawberry = 10

def iceCreamShop(flavor):
    if flavor > 1:
        print("we have vanilla in stock.")
    elif flavor > 1:
        print('we have chocolate in stock')
    elif flavor > 1:
        print('we have strawberry in stock')
    else:
        print('we dont have that ice cream')

# Tell me what to do on each down based on the yards.
# down = input('What down is it? ')
# yards = input('How man yards do you need to get another first down? ')

# if down == 1 and yards <= 5:
#     print("run it.")
# elif down == 2 and yards <= 5:
#     print("run it")
# elif down == 3 and yards <= 5:
#     print("play action")
# else: # this is the exit; assumes it is 4th down. 
#     print("punt")



# Create a conditional block of code that acts as a 
# password checker. The user should be able to input a 
# password. if it is correct, they should get a message 
# saying "welcome, you are logged in". Otherwise, they 
# should get a message saying "try again". 

# password = input("Please enter a password: ")

# if password == 'abc123':
#     print("Welcome! You are logged in!")
# else:
#     print("Sorry, incorrect password. Please try again.")

# studentCredit = input("Please enter the number of credits you have: ")

# if (int(studentCredit) >= 50):
#     print("Congrats! you are eligible to graduate.")
# else:
#     print("Sorry, you have not satisfied the required credit points.")



# Activity 1
# Create a function that will check whether a student is old 
# enough to get there drivers permit. Your function should accept 
# 1 parameter. If the user is 16 and older, your function should
# return a message saying they can begin the process of getting 
# their driver's permit. Otherwise, your function should 
# inform the user they are not old enough.

def testTakerPermit(age):
    if age >= 16:
        print("You may take your permit test.")
    else:
        print('you are not old enough')

testTakerPermit(18)

# Activity 2
# Create a function that will determine if a number is positive or negative.
# if a number is positive, it should print a message saying "this is positive".
# otherwise, it should print the number is negative. 

# Activity 3
# Create a grade score checker function that allows a student to enter
# their numerical grade, and show them the letter grade. Your function 
# should be able to process the grades as followed. If a grade number is 
# below a 70, it is an F. if a grade is above 70 and below 80, it is a C.
# if a grade is above 80 and below 90, it is a B.  
# and lastly is a grade is above 90, its an A.
