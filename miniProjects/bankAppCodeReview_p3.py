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

# payCheckFilter(14000.00, .5, 10) 

# Average number of working days for Americans = 260
# Average number of hours for full time employment = 8
# State income tax = 3.0
# Local income tax = 3.4


# Run the following code in your terminal. 
# Once you've confirmed the code works, make the following code adjustments:

# * NOTE= You may need to create new parameters, arguments
# - DO NOT replace the existing code. You are to create NEW Additional code

# 1. Surge pricing - If surge pricing is TRUE, the base fare is increased by .75
# * Hint: create a new surgePrice parameter

# 2. Ride Discount - if the user has a discount, reduce the total/ final ride 
# price by 15%

# 3. Long distance rate - if the miles exceed 10, the cost 
# per mile increases to 3.50

def rideShareCalculator(miles, surgePrice, discount):
    base_fare = 3.00
    surge_fare = 3.75

    cost_per_mile = 2.00
    

    if surgePrice == True:
        print ('The final price for this ride is $' + str(surge_fare + (miles * cost_per_mile)))
        total = surge_fare + miles * cost_per_mile
        discount = .15
        saved = total - discount
        total -= saved
        if discount == True:
            print ('You have discount here is your new price $' + str(total))
        
    elif surgePrice== False:
        print ('The final price for this ride is $' + str(base_fare + (miles * cost_per_mile)))
        total = base_fare + miles * cost_per_mile
        discount = .15
        saved = total - discount
        total -= saved
        if discount == True:
            print ('You have discount here is your new price $' + str(total))

rideShareCalculator(2, True, False)





total  = 7.75
discount = .15
savings= total * discount
total -= savings
print(total)



