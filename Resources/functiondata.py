# How to create a function with data

# Step 1. Function definition
def bnbRefund(accountNumber, refundAmount): # parameters are placeholders 
    print('account number: ' + str(accountNumber))
    print('refund amount: $' + str(refundAmount))

# Step 2. Function call (invocation)
bnbRefund(19389289, 2000) # arguements are real data 

# Class Activity 1
# Create a birthday message function. 
# Your function should have two parameters; 
# 1 for name and the other for birth date. 
# Both parameters should be string data types. 
# Your function should concatenate the parameters 
# with a pre-written strings and form the following message:
# My name is Ian and my birthday is Jan 30.

def name_bday(name, bday):
    print('my name is '+ name + ' my bday is ' + bday)

name_bday('Mary','July 2nd' )