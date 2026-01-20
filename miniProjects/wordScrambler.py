import random

# Function needs to have a list of 4 words/ strings - DONE
# Function needs to take 1 word from list randomly - DONE
# Selected word needs to be randomized/ shuffled - DONE
# Allow user to guess the original / correct word. - DONE
# IF it is correct, they ELSE they lose - DONE

# Add logic that will allow the user to make 3 guessing attempts
# and show the user the number of attempts they have
 
def scrambleWordGame():
  
    wordPool = ["pennsylvania", "north carolina", "congregate", "function"]
    print("Welcome to Word Scramble!")
    
    randomWordSelect = random.randint(0, 3)
    correctWord = ''

    if randomWordSelect == 0:
        correctWord = wordPool[0]
    elif randomWordSelect == 1:
        correctWord = wordPool[1]
    elif randomWordSelect == 2:
        correctWord = wordPool[2]
    elif randomWordSelect == 3:
        correctWord = wordPool[3]

    convertedSelction = list(correctWord) 
    random.shuffle(convertedSelction)
    scrambled = "".join(convertedSelction)

# While Loop solution
    guess = 1
    while guess !=4:
        print("Guess the correct word: " + scrambled)    
        userGuess = input()
       
        if userGuess == correctWord:
            print("Congrats! that is correct")
            print("number of guesses "+ str(guess))
            guess = 4
        else: 
            print("Sorry, that is incorrect.")
            print("number of guesses "+ str(guess))
            guess += 1

# For loop Solution 
    # for guess in range(1,4):
    #     print("Guess the correct word: " + scrambled)    
    #     userGuess = input()
       
    #     if userGuess == correctWord:
    #         print("Congrats! that is correct")
    #         print("number of guesses "+ str(guess))
    #         break
    #     else: 
    #         print("Sorry, that is incorrect.")
    #         print("number of guesses "+ str(guess))

scrambleWordGame()
 