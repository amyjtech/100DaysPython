# Automate the Boring Stuff with Python - Lesson 12
# Guess the Number Game

import random


def randomNumberGame():

    # Requesting the player's name and saving to variable
    print('Hello, what is your name?')
    name = input()
    
    print(f'Well,',name,'I am thinking of a number between 1 and 20...')

    # Generating secret number
    secretNumber = random.randint(1,20)

    print('Take a guess!')

    # Using range to allow player 6 guesses
    for guessesTaken in range(1,7):
        # Letting player know which guess they are on
        print(f'This is your',guessesTaken,'guess!')

        # Taking the player's input and saving to 'guess' variable
        guess = int(input())

        if guess < secretNumber:
            print('Your guess is too low!')
        elif guess > secretNumber:
            print('Your guess is too high!')
        # Break loop if correct, or guessed 6 times
        else:
            break

    if guess == secretNumber:
        print(f'You guessed correctly! It took you',guessesTaken,'guesses!')
    else:
        print(f'The number I am thinking of is',secretNumber)

    # Calling 'playAgain()'
    playAgain()

# Asking player if they want to play again
def playAgain():
    print('Would you like to play again?\n0 for No, 1 for Yes')

    again = int(input())

    # 0 exits, 1 calls 'randomNumberGame()'
    if again == 0:
        print(f'Goodbye!')
    elif again == 1:
        randomNumberGame()
    # If user does not enter 0 or 1, program tells them the input is invalid and starts over
    else:
        print('Incorrect input!')
        playAgain()

# Starting the game!
randomNumberGame()