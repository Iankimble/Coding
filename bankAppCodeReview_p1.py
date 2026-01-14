# Run the following code in your terminal. 
# Once you've confirmed the code works, make the following code adjustments:

# 1. write code that will put 25% of paycheck into the savingsAccount variable
# 2. write code that will put 25% of paycheck into the retirementAccount variable
# 3. write code that will put the remaining 50% of the paycheck into the checkingAccount variable
# 4. Print what the user will have in each account. 

def payCheckFilter(payRate, hours, daysWorked):
    checkingAccount = 0
    retirementAccount = 0
    savingsAccount = 0
    paycheck = payRate * hours * daysWorked
    
    savingsAccount += paycheck *.25
    retirementAccount += paycheck / 4
    checkingAccount += paycheck *.5
    print('My pay check for working '+ str(daysWorked) + ' day(s) will be $' + str(paycheck))
    print('savings balance: ' + str(savingsAccount))
    print('retirement balance: '+ str(retirementAccount))
    print('checking balance: ' + str(checkingAccount))
    
payCheckFilter(45.00, 8, 5)

# Run the following code in your terminal. 
# Once you've confirmed the code works, make the following code adjustments:

# * NOTE= You may need to create new parameters, arguments
# - DO NOT replace the existing code. You are to create NEW Additional code

# 1. Surge pricing - If surge pricing is true, the base fare is increased by .75
# 2. Ride Discount - if the user has a discount, reduce the total/ final ride price by 15%
# 3. Long distance rate - if the miles exceed 10, the cost per mile increases to 3.50

def rideShareCalculator(miles):
    base_fare = 3.00
    cost_per_mile = 2.00
    return base_fare + (miles * cost_per_mile)
    

