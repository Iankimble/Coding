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

#numberLoop()     

# to stop your loop hit crtl + c

# Activity 2
# Create a function that will continue to take in a number, 
# and when a user confirms they are done entering a number 
# add the numbers up and print out the result. Your function 
# should use a while loop where so long as the user does 
# not enter “quit”, it should continue adding numbers. 
# When they enter “quit” add the sum of numbers up.
  
# Hint: you will need to use the sum() function- check w3schools   
 
# Activity 3 
# Make a number guessing function. 
# Your function should be able to take in a number as user input. 
# Your function should then evaluate if the user guessed the correct number. 
# If the user enters a number that is above the correct number, 
# it should output a message saying its to high and loop back to asking them to
# enter a number. If it's below the correct number, it should output a message 
# saying its too low and loop again. If they guess correct it should 
# congratulate them and end the loop.


def guessTheNumber():
    correctumber = 8
    userGuess= int(input('Guess the correct number'))
    while userGuess != correctumber: 
            if userGuess > correctumber:
                print('number too high')
                userGuess= int(input('Guess the correct number'))
            else:
                print('number too low')
                userGuess= int(input('Guess the correct number'))    
    else:
        print("Congrats you guessed correct! ")

guessTheNumber()
          









