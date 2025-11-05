# For Loops - A type of construct that runs code instructions
# a finite amount of times over a group of data. 

halloweenBag = ['Snickers','Hershey Bar','Twizzler','Candied Apple','Candy corn']

count = len(halloweenBag)

print(count)

# i is a variable and is short for iterator. 
for i in halloweenBag:
    print(i)
    print('I go this candy in my bag ' + i)


# Use a for loop to ask a user to type in 5 words and print each word out in
# the terminal. Once the user has finished typing 5 words, 
# the for loop should end. 

# Clarification: program should ask the user to type in one word. Then the program
# should print it out and ask them to type another word. Your program
# should do this 5 times.

# Hint # 1: you should use the range() function.

# Create a function that uses a for loop to find the largest number. 
# Your user should be able to type in 5 numbers. 
# Once the user types in 5 numbers your program 
# should be able the find the highest number.

# Hint # 1: this problem is very similar to the first.
# Hint # 2: You will need to use a list.
# Hint # 3: You will need to use thhe max() function. 
# - you can use w3schools or googl to find out what the max() function does 