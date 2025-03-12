from random import randint


# Keep creating games as long as the user wants to play
while True:
    print('\n--------------------------------------------------------------\n')
    answer = input('Do you want to play mastermind? (yes/no) ')
    if answer.lower() == 'no':
        print('Bye.')
        break

    # Create the code for the user to guess
    code = ''
    for i in range(4):
        code += str(randint(0, 9))

    # Simbols legend
    print('''\nS (Strike) = correct digit at the right place
B (Ball) = correct digit at the wrong place''' )

    # Set the number of guess attempts for the user to 9
    n_attempt = 0
    while n_attempt < 9:
        guess = input('\nEnter a four-digit code. ')
        if not guess.isdigit() or len(guess) != 4:
            print('Invalid guess, please retry.')
            continue
        n_attempt += 1
        code_digits = [digit for digit in code]
        guess_digits = [digit for digit in guess]
        strikes, balls = 0, 0

        # The user guesses the code and wins the game
        if guess == code:
            print('You win.')
            break

        # Count the strikes
        for i in range(4):
            if code_digits[i] == guess_digits[i]:
                strikes += 1
                code_digits[i] = guess_digits[i] = None

        # Count the balls
        for i in range(4):
            if guess_digits[i] is not None and guess_digits[i] in code_digits:
                balls += 1
                code_digits[code_digits.index(guess_digits[i])] = None

        # Display a suggestion to the user after each attempt
        print(f'Attempt {n_attempt}/9: \n{strikes}S\n{balls}B')

    # The user does not guess the code after 9 attempts and loses the game
    if guess != code:
        print(f'You lose. The code was {code}.')