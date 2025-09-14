# Function - Instructions for executing code.

# to create a function, we start with the "def" keyboard.
# this is the function definition.
# this describe the steps/ instuctions that we want our 
# code to do.

def pbj():
    print("step 1. get 2 slices of bread.")
    print('step 2. spread peanutbutter on 1 slice of bread.')
    print('step 3. spread jelly/ jam on the other slice.')
    print('step 4. put slices together with spreads facing eachother.')
    print('step 5. sandwich is done. Enjoy.')

# to actually run and execute a function, you need to write its name.
# this called a function call, or function invocation. 

def hamburger():
    print('hamburger coming right up!')

def math_add():
    a = input('enter a number: ')
    b = 20
    print(int(a) + b)

def math_sub():
    a = input("enter a number: ")
    b = 10
    print(int(a)- b)

def math_mult():
    a = input("enter a number: ")
    b = 10
    print(int(a)* b)

def math_div():
    a = input("enter a number: ")
    b = 10
    print(int(a)/ b)



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
example()

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
    
    def calculate():
        numx = input('Please enter a number: ')
        numy = input('Please enter another number: ')
        print(numx, numy)
    
    calculate()

math()




# create a function that will calculate 2 numbers
# with different arithmetic operators













# # create a function for calculating numbers
# def calculate(a,b): 
#     # a = input("Please enter a number: ")
#     # b = input("Please enter another number: ")
#     print(int(a) + int(b))
#     print(int(a) - int(b))
#     print(int(a) * int(b))
#     print(int(a) / int(b))

# #calculate(10,10)

# # functions have a way of passing data without users
# # we can pass data through the function parameters
# # the round brackets at the end of a function are 
# # are called function parameters

# # when data is passed in the function definition,
# # it is called a parameter. parameters are placeholders for expected
# # data
# def shoppingCart(items): # items is the parameter /placeholder
#     print( "You have " + str(items) + ' items in your cart.')

# when data is passed in the function call,
# it is called an arguement becuase its using real data
# shoppingCart(3)