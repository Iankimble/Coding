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
    
    savingsAccount += paycheck / 4
    retirementAccount += paycheck / 4
    checkingAccount += paycheck * .5

    print('My pay check for working '+ str(daysWorked) + ' day(s) will be $' + str(paycheck))

    print("savings account balance: " + str(savingsAccount))
    print("retirement account balance: " + str(retirementAccount))
    print("checking account balance: " + str(checkingAccount))

# Psychologist 94k - $44.0- $46.00
# Nutritionist 85k - $40.50 - $42.00

payCheckFilter(40.50, 8, 260)
