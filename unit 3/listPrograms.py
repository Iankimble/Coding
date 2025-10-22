# create a function
# user enters data 
# users options should be morning, afternoon, night
# if/else
# if morning= show morning food list
# if afternoon  = show lunch food list
# if night = show dinner food list
# if none of these options show error

def foodByTimeOfDay():
    timeOfDay = ['morning','afternoon','night']
    breakfast = ['sausage,egg, and cheese', 'bagel','apple and orange']
    lunch = []
    dinner= []
    print(timeOfDay)
    selection = input("Please select a time of day: morning, afternoon, night: ")
    if selection == 'night':
        print("it is dinner")
        print(breakfast)
        print(['sausage,egg, and cheese', 'bagel','apple and orange'])
        
    elif selection == 'morning':
        print("it is breakfast")
    elif selection == 'afternoon':
        print("it is lunchtime")
    else:
        print('error; cant find that input')

foodByTimeOfDay()