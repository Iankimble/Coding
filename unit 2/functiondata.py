# How to create a function that passes data

# Step 1. Create a function definition/ instruction to follow
def bnbRefund(username, refundAmount):
    print('Sorry '+ username + ' for your cancellation.')
    print(' We will refund $'+ str(refundAmount) +' to your bank.')    

# Step 2. Call the function / execute instructions
# bnbRefund('Mary', 5)

# Class Activity 1
# Create a birthday message function. 
# Your function should have two parameters; 
# 1 for name and the other for birth date. 
# Both parameters should be string data types. 
# Your function should concatenate the parameters 
# with a pre-written strings and form the following message:
# print: My name is {Ian} and my birthday is {Jan 30}.

def bdayMsg(name, bday):
    print(" My name is " + name + " and my bday is " + bday)

bdayMsg('Ian','November 2nd')

# Class Activity 2 
# Create a function that will convert dollars into pennies. 
# Your function should take the dollar amount in as a parameter
# and calculate the dollar amount into pennies. 
# Your function should print out the following message:
# My {13} dollar(s) is equal to {1300} pennies.

def dollarConverter(dollar):
    pennies = dollar * 100
    print('My ' + str(dollar) +' dollar(s) is equal to ' + str(pennies) + ' pennies.')

dollarConverter(300)

# Activity 3
# Create a function that will calculate the area of a triangle. 
# Your function should take in 3 parameters. One will represent the length, 
 # the other width, and the last one will be the height of the triangle. 
# length = 20
# width  = 15
# height = 23

# Hint: to calculate the area of a triangle you must calculate the 
# length * width * height

# Activity 4




# Create a function that  will multiply two integer data types together
# Your function should take in one of the numbers as a parameter. 
# The second number should be passed in by the user from the terminal. 









# Create a function that adds two integer values together. 
# Your function should have 2 parameters that will represent 
# the numbers in your function.

def add(number1, number2):
    sum = number2 + number1
    print(str(number1) + '+ ' + str(number2) + '= ' + str(sum))

add(1,2)


# Create a function that  will multiply two integer data 
# types together. Your function should take in one of the
# numbers as a parameter. The second number should be passed in
# by the user from the terminal. 

def multiply(num1):
    num2 = input('please type in a number: ')
    sum = num1 * int(num2)
    print(sum)
    print(str(num1) + "* " + num2 + "= " + str(sum))

multiply(10)