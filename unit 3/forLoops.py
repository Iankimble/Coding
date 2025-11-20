# For Loops - A type of construct that runs code instructions
# a finite amount of times over a group of data. 

halloweenBag = ['Snickers','Hershey Bar','Twizzler','Candied Apple','Candy corn']

# count = len(halloweenBag)

# print(count)

# i is a variable and is short for iterator. 
# for i in halloweenBag:
#     print(i)
#     print('I got this candy in my bag ' + i)
















def tf():
    for x in range(3): 
        print('true or false: 3 is greater than 2')
        answer = input()
        if answer != 'true':
            print('wrong, try again')
            print('attempt: '+ str(x))
        else:
            print('great!')
            break # stops the loop. regardless of it being a for or while loop


# Use a for loop to ask a user to type in 5 words and print each word out in
# the terminal. Once the user has finished typing 5 words, 
# the for loop should end. 

# Clarification: program should ask the user to type in one word. Then the program
# should print it out and ask them to type another word. Your program
# should do this 5 times.

# Hint # 1: you should use the range() function.
# for x in range(5):
#     word = input("Please type in a word: ")
#     print(word)


# looping throuh strings
# word = "Python"
# for letter in word:
#     print(letter)


# looping through lists of numbers 
# shoppingPrices = [3.00, 5.40, 7.20, 9.00, 10.40, 11.00]
# total = 0

# for items in shoppingPrices:
#     total += items
#     print(total)

#print(total)







def schoolAttedenceSys():
    studentBody=  ['jordan','joel','devonte','...']

    present =[]
    absent =[]
    scannedIn = True
    for student in studentBody:
        print('Is '+ student + 'scanned in today?')
        response = input()

    # if student =! scannedIn
    # move to absent list
    # absent.append(student)
    # else put them in the present List
    # present. append(student)




def greet(name):
    return "Hi " + name
# print(greet("Ian"))





def checkout():
    groceryBag= [1,20,3,6,7]
    total= 0

    for item in groceryBag:
        total += item

# 1. We can make it safer - Add authentication, 
# Add age limit→ Make 2 different variations based on age. 

# option 1- Add more ways to verify people

# option 2-  Make a different version of tik-tok

def signup():
    dob = int(input('what year were you born? '))
    tiktok_kids = []
    tiktok_teens = []
    tiktok_standard = []
    # 8 -12 is kids
    # 13 - 18 is teen
    # 19 > is adult
    currntYr = 2025
    usrAge = currntYr- dob
    if usrAge > 8 and usrAge < 12:
        print('welcome to tiktok kids')
        tiktok_kids.append(usrAge)
        
signup()

# 2. Add calling

# 3. Can’t send photos on direct message - 
# problem solving feature

# 4. Add external links in comment section - 
# problem solving feature

# 5. Ad blocker - disruptive feature











# Create a function that uses a for loop to find the largest number. 
# Your user should be able to type in 5 numbers. 
# Once the user types in 5 numbers your program 
# should be able the find the highest number.

# Hint # 1: this problem is very similar to the first.
# Hint # 2: You will need to use a list.
# Hint # 3: You will need to use thhe max() function. 
# - you can use w3schools or googl to find out what the max() function does 











# Track purchase order history - when we buy something, 
# we should be able to track it.

# Tik-tok VPN relocation - see content from other areas 

# Safety - age verification

# Exclusively show STEM tab to kids

# Improve search  to be more content focused

# Tiktok kids (ktt)
