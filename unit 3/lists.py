# Lists - A system for collecting and organizing multiple peices 
# of data. 

# List Syntax (how it is written)
# When we want to create a list, we first create a variable name
# and assign it to the square brackets [].
# we then put the data we want to collect inside of
# the square brackets

shoppingCart = ['water','ice cream','cereal','apples']

# Accessing items in a list-
# when we want to access an item in a list we write the variable name
# and then use the square brackets and pass in the item position in
# the brackets

# python is a zero-based index language. meaning; when counting
# items, zero is treated as an actual numbers and is counted.

print(shoppingCart[2])

shoppingCart.append("orange")

#print(shoppingCart)

def addItemToCart():
    bestBuyCart= ['8k Monitor','Graphics Card', 'Speakers', 'pro controller']
    item = input("Please add new item: ")
    bestBuyCart.append(item)
    print(bestBuyCart)

def removeItemToCart():
    bestBuyCart= ['8k Monitor','Graphics Card', 'Speakers', 'pro controller']
    item = input("Please remove item: ")
    bestBuyCart.remove(item)
    print(bestBuyCart)

# Create a function to remove the graphics card item from the list.
# use one of the method from w3schools

#___________________________________________

# Create a function that adds a new number to a list and then puts the list 
# in order from least to greatest. 
# The new number should be passed into your function as a parameter. 
# The number you will add is 60. 

numbersList = [100, 23, 450, 63, 1, 6, 19, 1000]

def addAndSort(newNumber):
    numbersList.append(newNumber) # new number has been added. 
    numbersList.sort() # just add sort, and we are done.   
    print(numbersList) # just telling the computer to print

addAndSort(60)












# Add new logic to this function to make so that the list prints out 
# in reverse order so instead of least to greats, it is greatest to least. 








# 1. Sort a list of numbers, find the min and max number
# 2. Create a function that will insert a value in a list

# 2. Create a function that will show a breakfast menu and dinner menu
# depending on the time time input


#  