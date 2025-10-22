# Activity 1
# Create a function that will print out a list of numbers based on 
# what the user inputs. Your function should take in a user input, 
# add the input to a list and then print it out in the terminal. 
# If the user enters the word “quit”, the function loop 
# should stop. 

# create a function
# print out a list of numbers in terminal
# take in a user input over and over again and add to list
# stop the loop when they type "quit"

def numberLoop():
    numbers = []
    userNumber = input("Please type in a number: ")
    while userNumber != 'quit':
        transformNumber = int(userNumber)
        numbers.append(transformNumber)
        print(numbers)
        userNumber = input("Please type in a number: ")
    else:
        print("Loop has stopped. ")

numberLoop()     

# to stop your loop hit crtl + c



# Activity 2
# Create a function that will continue to take in a number, 
# and when a user confirms they are done entering a number 
# add the numbers up and print out the result. Your function 
# should use a while loop where so long as the user does 
# not enter “quit”, it should continue adding numbers. 
# When they enter “quit” add the sum of numbers up.
  
# Hint: you will need to use the sum() function- check w3schools   
 