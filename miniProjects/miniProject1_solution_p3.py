def pythonQuiz():
    grade = 0
    print('1. What is a function argument?')
    print('A. placeholder data that goes into a function.')
    print('B. Real data that goes into a function.')
    print('C. A piece of data used to compare values.')
    userAnswer = input()
    # print('this is what the user typed : ' + userAnswer)
    correctAnswer = 'b'
    if userAnswer == correctAnswer:
        print("Correct")
        grade += 1
    else: 
        print("incorrect")
    print('2. True or false; 0 and 1 can be used as boolean values?')
    print('A. True')
    print('B. False')
    userAnswer = input()
    # print('this is what the user typed : ' + userAnswer)
    correctAnswer = 'a'
    if userAnswer == correctAnswer:
        print("Correct")
        grade += 1
    else: 
        print("incorrect")
    print('3. What is a function invocation?')
    print('A. It is when you write the instructions for your function')
    print('B. It is when you pass data into your function')
    print('C. It is when you call the function')
    userAnswer = input()
    # print('this is what the user typed : ' + userAnswer)
    correctAnswer = 'b'
    if userAnswer == correctAnswer:
        print("Correct")
        grade += 1
    else: 
        print("incorrect")
    print('4. What is the difference between an integer and a float?')
    print('A. An integer is a decimal number and a float is a whole number')
    print('B. An integer is a whole number and a float is a decimal number')
    print('C. There is no difference. they are both number data types')
    userAnswer = input()
    # print('this is what the user typed : ' + userAnswer)
    correctAnswer = 'b'
    if userAnswer == correctAnswer:
        print("Correct")
        grade += 1
    else: 
        print("incorrect")
    print('5. How many parameters can you have in a function?')
    print('A. 1')
    print('B. 2')
    print('C. As many as you want')
    userAnswer = input()
    # print('this is what the user typed : ' + userAnswer)
    correctAnswer = 'b'
    if userAnswer == correctAnswer:
        print("Correct")
        grade += 1
    else: 
        print("incorrect")  
        print(" here is your score:  " + str(grade) + "/ 5")

pythonQuiz()