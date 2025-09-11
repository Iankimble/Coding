# Function- is a set of code instructions labeld under
# a custom name that the computer will run.

# Function Syntax (rules of how its written)
# functions have 2 phases: function definition and 
# function call

# phase 1: function definition
# we are describing the instruction for our custom code.
# we are adding logic to the computers vocabulary.
# this code does not run- it only give the computer the meaning 
# not the action

def example():
    print('good morning.') # 1 instruction: print good morning

# phase 2: function call
# once we have the definition, we can now run the instructions
# by writing the function name.
 
 # we indent to inform the computer that we are about to write
 # code instructions. if we don't, we will get an error.

def example2():
    print('good day')
    a = input('enter a number: ')
    print(a)

def math():
    a = input("Please enter a number: ")
    b = 30
    print("Here is your result! ")
    print(int(a) + b)

#math()

# create a function for calculating numbers
def calculate(a,b): 
    # a = input("Please enter a number: ")
    # b = input("Please enter another number: ")
    print(int(a) + int(b))
    print(int(a) - int(b))
    print(int(a) * int(b))
    print(int(a) / int(b))

#calculate(10,10)

# functions have a way of passing data without users
# we can pass data through the function parameters
# the round brackets at the end of a function are 
# are called function parameters

# when data is passed in the function definition,
# it is called a parameter. parameters are placeholders for expected
# data
def shoppingCart(items): # items is the parameter /placeholder
    print( "You have " + str(items) + ' items in your cart.')

# when data is passed in the function call,
# it is called an arguement becuase its using real data
shoppingCart(3)