import random

# 1. Create a function that contains a list with 4 words/ strings. - DONE
# 2. Randomly select a word from the list. - DONE
# 3. Shuffle the select word and show it to the user. - DONE
# 4. Allow user to input a guess. if it is correct, they win, 
# else they lose. - DONE

# Create additional code that will give the user 3 attempts to get the correct answer
# this new code should also count the number of attempts and tell the user how many they have


def wordScrambler():
    wordPool = ["latitude",'arithmetic','sophisticated','pyscosis']
    correctWord =''

    print("Welcome to scrambled! ")
    randomSelect = random.randint(0,3)

    if randomSelect == 0:
        correctWord = wordPool[0]
    elif randomSelect == 1:
        correctWord = wordPool[1]
    elif randomSelect == 2:
        correctWord = wordPool[2]
    elif randomSelect == 3:
        correctWord = wordPool[3]
    
    convertedString = list(correctWord)

    random.shuffle(convertedString)
    scrambled = "".join(convertedString)
    print("Please guess the correct word: " + scrambled)
    userGuess = input()

    if userGuess == correctWord:
        print("You Win!")
    else:
        print("Sorry, you lose.")

wordScrambler()

def userLogin_app(username, password):
    # API call to the data -->
    # req validation 
    # res
    # 
    # 
def resetPassword(newpassword, oldpassword, user)
    
def lockaccount(username, password)
def sendUserInfo() 
     