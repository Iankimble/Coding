# 1. We can make it safer - Add authentication, 
# Add age limit→ Make 2 different variations based on age. 
# option 1- Add more ways to verify people
# option 2- Make a different version of tik-tok

def signup():
    dob = int(input('what year were you born? '))
    tiktok_kids = [] # 8 - 12 is kids
    tiktok_teens = [] # 13 - 18 is teen
    tiktok_standard = [] # 19 > is adult
    currntYr = 2025
    usrAge = currntYr - dob
    print('my age is '+ str(usrAge))
    if usrAge < 12:
        print('welcome to tiktok kids')
        tiktok_kids.append(usrAge)
    elif usrAge > 12 and usrAge < 18:
        print('wassup chat, welcome to tik tok teens, 67!')
        tiktok_teens.append(usrAge)
    else:
        print('welcome to tiktok')
        tiktok_standard.append(usrAge)
#signup()


# 2. Add calling

# 3. Can’t send photos on direct message - 

# problem solving feature
# 4. Add external links in comment section - 

# problem solving feature
# 5. Ad blocker - disruptive feature


# Use the SDLC steps we learned to build a simple calculator app.

# Step 1. ideation - what features should you have in your calculator app.
# please write the 3 or 4 features as strings

# example
'1. Be able to do simple addition.'

# Step 2. analysis and requirements- how would you code out your calculator
# please write atleast 1 function for 1 of your features 
# explain how you would code it/ how you think you woulld code it.

'I would need to create possibly a function that allow users to enter 2 or more'
'integers together and provides the sum of those integer using the.'
'arithmatic addition operator.'

# exmaple
def add():
    num1 = int(input("enter a number: "))
    num2 =  int(input("enter ANOTHER number: "))
    sum = num1 + num2
    print("sum = " +str(sum))
    keepGoing = input("Would you like to add to the sum ? enter y or n")
    while keepGoing != 'n':
        numX= int(input("enter a number: "))
        sum += numX 
        print("NEW sum = " +str(sum))
add()



# Improve search  to be more content focused
'take string data in and anaylze strings for related keywords'
'if someone uses any of these keys words show them specific results'

keywords =['nfl', 'nba', 'anime', 'games',]
istragram =[]

'python','loops','games'

searchbar = input("what are you looking for today? ")
'nfl hoodies'
for word in keywords:
    results = word
    print("we found this content for you: " + str(results))



# Tik-tok VPN relocation - see content from other areas 


# Track purchase order history - when we buy something, 
# we should be able to track it.



# Safety - age verification

# Exclusively show STEM tab to kids


# Tiktok kids (ktt)




# Use the SDLC steps we learned to build a simple calculator app.

# Step 1. ideation - what features should you have in your calculator app.
# please write the 3 or 4 features as strings

#example
'my calculator should be able to do addition with 2 or more'
'numbers and print out the sum.'

'type in which arithmatic operator you want to use and then perform a calculator. '

'visualize data on calculator'

'multiple arithmatic operations in one request/ equation'

# step 2. analysis and requirements- how would you code out your calculator
# please explain how you would use code to acomplish this.
# please write your responses as a string and attempt
# at least 1 function for 1 of your features.

'I need to use a specficic operator and probably loop to perfrom'
'multiple addition operations. I also need to let the user type in numbers'

def addition():
    print('some code...')