# While Loop Definition - a while loop is a type of construct
# where code instructions will keep on running so 
# long as a condition is TRUE (boolean)

# NOTE - In order to stop a loop (or any program) from running
# in your terminal, click crtl + c at the same time. 

# While Loop Syntax 

def ageCheck():
    ageVerification = 17

    purchaserAge = int(input("Please enter your age: "))

    while ageVerification >= purchaserAge: # 17 >= 15 = TRUE: 17 is larger than 15
        print("Sorry, your not old enough.")
    else:
        print('Enjoy your collectors edition of GTA VI')

def password():
    savePassword = '123abc'
    userPassword = input("please type in your password")
    attempts = 0
    profileMenu = ['messages','pictures','feed']

    while savePassword != userPassword:
        print('Incorrect Password.')
        attempts += 1
        print('number of attempts left: '+ str(attempts) + ' / 3')
        userPassword = input("please try again: ")
        if attempts == 3:
            print('You made too many inccorect attempts. your account has been locked for 5 minutes.')
            break
    else:
        print('Welcome to your account.')

def count():
    number = 0
    while number < 10:
        number += 1  
        print(number)
    else:
        print("done counting")

# create a countdown timer using a while loop. 
# your timer should start at 30 and count down to 0 by 1. 

x = 30
while x != 0: 
    x -= 1
    print(x )
else:
    print('done')










# Using loops to increment and decrement - useful for doing steps while true for a certain number of times
# Password example

# import random

# number = random.randrange(1, 10)

# print(number)

# guess= int(input("guess a number between 1 and 10: "))

# while guess != number:
# 	guess = int(input("guess again: "))
# else:
# 	print("correct!")