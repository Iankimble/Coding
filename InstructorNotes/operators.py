# Operators
# Operators are a construct (built-in system) that give
# data types more actions and power. 

# Arithmetic family of operators (Math)
# Artihmetic operators are just math operations
# arithmetic operators are the addition, subtraction, 
# multiplication, and division symbols

#print(2 + 4)
#print(3 * 10)
#print(20 - 10)
#print(3 / 1)
#print(1.34 * 2)

# Print() is a function where anything inside the rounds will be
# printed out in the terminal. 

# Assignment Operator Family
# these operators assign values to variables
# (otherwise known as containers)

x = "Ian"
schoolName = "Boys Latin"

value1 = 10
value1 += 1
value1 -= 2

#print(value1)
#print(x)
#print(schoolName)

# Comparison Operator Family
# Comparison family of operators simply compares values. 

#print(2 > 1) 
#print(100 < 29)
#print("123Abc" == "123Avbc") # double equal signs mean
# its comparing if the values are "THE SAME" 

#print(2 != 3) # NOT the same

# Logical Operator Family
# it checks and compares if certain code conditions
# are true or false

print(3 > 1 and "Ian" == "Ian") # This will return true

# the AND operator checks to see BOTH condition are true. 
# If BOTH are TRUE the answer is TRUE. 

print(2 == 1 or 3 > 2) # This will return true
# The OR operator checks if ONE of the conditions is TRUE.
# So long as ONE of the conditions is TRUE, it will be TRUE.

print(not(3 > 1 and "Ian" == "Ian")) # false
# The NOT operator will give the opposite result. 
# the NOT operator flips the result.

algebraPassed = True
historyPassed = True

# does this person need credit recovery
# true means they passed
#print(not(algebraPassed== True and historyPassed == True))

gradeA = 100
gradeB = 90


# we need a function that will 
# calculate the total cost 
# of each item with sales and shipping tax

# artic coat = 250.00
# snow boats = 150.00
# goggles = 100.00

# sale tax = 0.08
# shipping tax = 0.02
# 0.10

def totalCost(itemName, itemPrice):
    tax = 0.10
    totalTax = itemPrice * tax
    totalPrice = totalTax + itemPrice
    print(totalPrice)

# totalCost('artic Coat',100.00)

"Artic coat total is $275.00"
"Snow boots total is $165.00"
"Goggles total is $110.00"

mynumbers = [10,8,3, 28,300,57]

def sortHiLow(arry,i):

# mynumbers.sort()
# print(mynumbers)

