# Rock Paper Scissors

import random

# Keep track of user and comp score
user = 0
comp = 0

options = ["rock", "paper", "scissors"]

while True:
    # .lower() to make all data the same
    user_input = input("Rock - Paper - Scissors\nQ to Quit\n").lower()
    if user_input == 'q':
        # Stops the While Loop
        break
    # Checking the list
    if user_input not in options:
        # Continues the While loop, will not run code below
        continue

    # Rock: 0, Paper: 1, Scissors: 2
    random_number = random.randint(0, 2)
    comp_pick = options[random_number]

    print(f"Computer picked {comp_pick}")

    if user_input == "rock" and comp_pick == "scissors":
        print("You won!")
        user += 1
    elif user_input == "paper" and comp_pick == "rock":
        print("You won!")
        user += 1
    elif user_input == "scissors" and comp_pick == "paper":
        print("You won!")
        user += 1
    # If user and computer pick same it is a tie
    elif user_input == "scissors" and comp_pick == "scissors" or user_input == "rock" and comp_pick == "rock" or user_input == "paper" and comp_pick == "paper":
        print("Tie!")
    else:
        print("Computer won!")
        comp += 1

print(f"User Wins {user} | Computer Wins {comp}\nGoodbye!")
