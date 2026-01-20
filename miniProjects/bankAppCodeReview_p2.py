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

#payCheckFilter(40.50, 8, 260)



# Run the following code in your terminal. 
# Once you've confirmed the code works, make the following code adjustments:

# * NOTE= You may need to create new parameters, arguments
# - DO NOT replace the existing code. You are to create NEW Additional code

# 1. Surge pricing - If surge pricing is true, the base fare is increased by .75
# * Hint: create a new surgePrice parameter

# 2. Ride Discount - if the user has a discount, reduce the total/ final ride 
# price by 15%
    
# 3. Long distance rate - if the miles exceed 10, the cost 
# per mile increases to 3.50

def rideShareCalculator(miles, surgePrice, discount):
    base_fare = 3.00
    surge_fare = 3.75
    cost_per_mile = 2.00

    total = base_fare + miles * cost_per_mile

    if surgePrice == True:
        print ('The final price for this ride is $' + str(surge_fare + (miles * cost_per_mile)))
    else:
        print ('The final price for this ride is $' + str(base_fare + (miles * cost_per_mile)))
    
    if discount == True:
        discount = total *.15
        total -= discount
        print ('The final price for this ride is $' + str(total))
    else:
        print ('The final price for this ride is $' + str(total))

rideShareCalculator(3, False, True)