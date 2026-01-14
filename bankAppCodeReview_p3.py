# Run the following code in your terminal. 
# Once you've confirmed the code works, make the following code adjustments:

# 1. Write code that will put 25% of paycheck into the savingsAccount variable
# 2. Wwrite code that will put 25% of paycheck into the retirementAccount variable
# 3. Write code that will put the remaining 50% of the paycheck into the checkingAccount variable
# 4. Print what the user will have in each account. 

def payCheckFilter(payRate, hours, daysWorked):
    checkingAccount = 0
    retirementAccount = 0
    savingsAccount = 0

    paycheck = payRate * hours * daysWorked
    savingsAccount = paycheck / 4
    retirementAccount = paycheck *.25
    checkingAccount = paycheck / 2

    print('My pay check for working '+ str(daysWorked) + ' day(s) will be $' + str(paycheck))
    print("retirement account = "+ str(retirementAccount))
    print("savings account = " + str(savingsAccount ))
    print("checking account = "+ str(checkingAccount))

payCheckFilter(14000.00, .5, 10) 

# Average number of working days for Americans = 260
# Average number of hours for full time employment = 8
# State income tax = 3.0
# Local income tax = 3.4