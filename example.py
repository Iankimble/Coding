def nflQuiz():
    print("1. Which NFL team has the least amount of championship titles in the last 10 years?")
    print('A. Kansas City')
    print('B. New England')
    print('C. Philadelphia')
    print('D. Los Angeles')

    userAnswer_1 = input('user answer: ')
    print(userAnswer_1)

    correctAnswer_1 = 'd'

    if userAnswer_1 == correctAnswer_1:
        print('Correct. Los Angeles Rams have won only 1 title in the last 10 years.')
    else:
        print('Incorrrect.')

    print("2. Who is the rushing yard leader in 2024?")
    print('A. Derick Henry')
    print('B. Saquan Barkley')
    print('C. CeeDee Lamb')
    print('D. Josh Jacobs')

    userAnswer_1 = input('user answer: ')
    print(userAnswer_1)

    correctAnswer_1 = 'b'

    if userAnswer_1 == correctAnswer_1:
        print('Correct. Saquan Barkley was the rushing leader in 2024')
    else:
        print('Incorrrect.')

nflQuiz()