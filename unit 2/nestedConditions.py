def atm():
    balance = 5000
    pin = 1234
    checking= 0 
    savings= 0
    investment = 0
     
    print("Welcome, please type in your pin number: ")
    userPin=  int(input())

    if (userPin == pin):
        print("wWelcome what would you like to do? ")
        print("1. Withdraw money") 
        print("2. Deposit money")
        print("3. Check balance")
        print("4. transfer checking ")
        select= int(input("please selct an option: ")) 
        if select == 1:
            print('How much would you like to withdraw? ')
            amount = int(input())
            if amount > balance:
                print("Overdraft alert")
            else:
                newBalance = balance - amount
                print("you are taking out: " + str(amount))
                print("you have this amount left: " + str(newBalance))
        
        elif select == 2:
            print("How much do you want to deposit? ")
            amount = int(input())
            newBalance = balance + amount
            print("you are adding: " + str(amount))
            print("your new balance is : " + str(newBalance))

        elif select == 3:
            print("This is your current balance:  " + str(balance))

        else:
            print("Sorry dont understand your selection") 
    else: 
        print("Pin is incorrect.")
        atm()       
atm()
