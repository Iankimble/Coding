import random

# Please make a new document called rps.py and Develop ideas and 
# analyze the requirements for a rock, paper, scissor game. 

# For the ideation phase, write down 3 things your rock, paper, 
# scissor game should be able to do

"1. Users should be able to choose between rock, paper, and scissor"
"depending on their selection, they can either win, lose, or tie"

"2. Rounds should go up to 4, if tied go into sudden death match"

"3. If a player wins, you can take away a win from the opponent"
"- could add it to yours"

"4. If you win 3 straight its an automatic win"

'multi-player'
'reset game option'

# For the requirements and analysis phase, write down at last 4 
# technical requirements; example: be able to use integer data type 
# to process decisions.

# requirements- contexualize it in programming terms
# - what data types do we need
# - what operators do we need
# - are we using if/else
# - are we using a loop

'1. We could use strings to represent each option and possibly integers for '

'the option'
'selection'
"example input 1 for rock, input 2 for scissor, input 3 for paper"
"'analysis = easy"

'2. we can use a comparison operator to compare who won more rounds.'
'the person who won more rounds, wins.'
"analysis = easy"

'3. we can use a loop to keep the game going until someone wins.'
"analysis  = easy"

'4. if function; user gets 3 wins consecutively, stop the game loop '
"analysis = medium"

# design  
# plan for how the program will "flow"; essentially, how will users
# use the program step-by-step

'Step. 1: Welcome the user to the game'
'Step. 2: Give them the option to play the game or see the game rules'
'Step. 3: if user select rules, show them the rules, else start the game'
'Step. 4: Inform the user the game has started and ask them to make a selection; R,P,S'
'Step. 5: Computer makes a random selection'
'Step. 6: determine and the user/ player if they won, lose, or tied' 
'and keep track of score and round'
'Step. 7: (LOOP) Show the user the RPS options and they will continue to play up until round 4.'
'step 7.5: check if the user has won consective rounds- if they win 3 straight- give them a special message'
'Step. 8: Determine and inform the user if they won and return them to the main menu'

# development

def rpsGame():
    rpsOptions_cpu = ["rock", "paper", "scissor"]

    print("Welcome to Rock Paper Scissor: the game!")
    print("Please select one of the following:")
    print('Enter p to start game,')
    print('Enter r to see the rules')
    selection = input()
    if selection == 'r':
        print("here are the game rules ...")
    elif selection == 'p':
        print('the game is starting...')
        choiceUser = input("please make selection, r= rock, p= paper, s= scissor")
        choiceCpu = random.choice(rpsOptions_cpu)
        # make a way to show the full selection word ; example: if s, 
        # the program should print scissor
        if choiceUser == 'r':
            selectWord = rpsOptions_cpu[0]
            print('user selected: ' + selectWord)
            print('cpu selected: '+ choiceCpu)
        elif choiceUser == 'p':
            selectWord = 'paper'
            print('user selected: ' + selectWord)
            print('cpu selected: '+ choiceCpu)
        elif choiceUser == 's':
            selectWord = 'scissor'
            print('user selected: ' + selectWord)
            print('cpu selected: '+ choiceCpu)
    else:
        print("Sorry, we didnt understand your entry.")


rpsGame()