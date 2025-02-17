from random import randint


#Keep creating games as long as the user wants to play
while True:
    answer = input('\nDo you want to play a mastermind game? ')
    if answer.lower() == 'no':
        print('Bye.')
        break

    #Create the code for the user to guess
    code = ''
    for i in range(4):
        code += str(randint(0, 9))

    #Simbols legend
    print('''\nS (Strike) = correct digit at the right place
    \nB (Ball) = correct digit at the wrong place''' )

    #Set the guess attempts for the user to 9
    for i in range(9):
        attempt = input('\nEnter a four-digit code. ')
        s, b = 0, 0
        n = -1

        #The user guesses the code and wins the game
        if attempt == code:
            print('You win.')
            break

        #The user does not guess the code and the game continues
        for digit in code:
            n += 1

            #Count the correct digits at the right place
            if digit == attempt[n]:
                s += 1

            #Count the correct digits at the wrong place
            elif digit in attempt:
                b += 1

        #Display a suggestion to the user after each attempt
        print(f'{s}S\n{b}B')

    #The user does not guess the code after 9 attempts and loses the game
    if attempt != code:
        print(f'You lose. The code was {code}.')