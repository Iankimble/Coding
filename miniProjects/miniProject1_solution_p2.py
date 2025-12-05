# create a quiz game that gives users options.
# users type in a letter/ number that represent the answer
# keep track of answers and show them the total at the end

def pythonQuiz():
    grade = 0
    print('1. Which of the following is not a data type? ')
    print("A. Function")
    print('B. Integer')
    print('C. Float')
    print('D. String')
    userAnswer = input('')
    correctAnswer = 'a'
    if userAnswer == correctAnswer:
        grade += 1
        print('Correct')
    else:
        print('Incorrect')

    print('2. what is a function parameter? ')
    print("A. a variable that uses data")
    print('B. a peice of code that does operations')
    print('C. a peice of data that is a placeholder for data')
    print('D. real data that is worked on in a function')
    userAnswer = input('')
    correctAnswer = 'c'
    if userAnswer == correctAnswer:
        grade += 1
        print('Correct')
    else:
        print('Incorrect')
    
    print('3. What is a for loop? ')
    print("A. a type of function that repeats code forever")
    print('B. a type of function that checks conditions')
    print('C. a type of function that repeats 3 times')
    print('D. a type of function that repeats a finite amount of times')
    userAnswer = input('')
    correctAnswer = 'd'
    if userAnswer == correctAnswer:
        grade +=1
        print('Correct')
    else:
        print('Incorrect')
    print('4. True or false, a 0 and 1 can be considered booleans? ')
    print("A. True") 
    print('B. False') 
    userAnswer = input('')
    correctAnswer = 'a'
    if userAnswer == correctAnswer:
        grade +=1
        print('Correct')
    else:
        print('Incorrect')
    
    print('5. what is a function invocation? ')
    print("A. it is when we write the function instructions")
    print('B. it is when we use conditionals in a function')
    print('C. it is when we invoke and call a function')
    print('D. it is none of the above')
    userAnswer = input('')
    correctAnswer = 'a'
    if userAnswer == correctAnswer:
        grade +=1
        print('Correct')
    else:
        print('Incorrect')

    print('6. which these is a python operator? ')
    print("A. assignment")
    print('B. list')
    print('C. boolean')
    print('D. casting')
    userAnswer = input()
    correctAnswer = 'a'
    if userAnswer == correctAnswer:
        grade +=1
        print('Correct')
    else:
        print('Incorrect')

    print('7. What does thee pthon float() function do? ')
    print("A. Changes a number data type into a decimal number")
    print('B. Returns a sequence of numbers starting from 0, increments by 1')
    print('C. Prints specified messagee to screen')
    userAnswer = input()
    correctAnswer = 'a'
    if userAnswer == correctAnswer:
        grade +=1
        print('Correct')
    else:
        print('Incorrect')
    
    print('8. Which symbbols / characters represent true and false? ')
    print("A. and, not")
    print('B. !=', '==') 
    print("C. 0, 100")
    print("D. True and False")
    userAnswer = input()
    correctAnswer = 'd'
    if userAnswer == correctAnswer:
        grade +=1
        print('Correct')
    else:
        print('Incorrect')

    print('here is your final grade: '+ str(grade) + '/ 5')

pythonQuiz()


