import random

def scrambler():
    wordPool = ["pennsylvania","representative","detartrated", "peculiar"]
    selectedWord =''

    wordIndex= random.randrange(0, 3)
    if wordIndex == 0:
        selectedWord = wordPool[0]    
    elif wordIndex == 1:
        selectedWord = wordPool[1]
    elif wordIndex == 2:
        selectedWord = wordPool[2]
    elif wordIndex == 3:
        selectedWord = wordPool[3]   

    convertedWord = list(selectedWord) 
    random.shuffle(convertedWord)
    scrabledWord = "".join(convertedWord)
    print("Guess the scrambeld word: " + scrabledWord)
    userGuess = input()

    if userGuess == selectedWord:
        print('correct')
    else:
        print('incorrect')

scrambler()