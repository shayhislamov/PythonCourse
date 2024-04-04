# Importing the random module for generating random numbers
import random

# Initializing variables to keep track of user and computer wins
user_wins = 0
computer_wins = 0

# List of options for the game
options = ["rock", "paper", "scissors"]

# Using a WHILE LOOP to continue the game until the user decides to quit
while True:
    # Taking user input
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    
    # Exiting the loop if the user inputs 'q'
    if user_input == "q":
        break

    # Checking if the user input is valid
    if user_input not in options:
        continue

    # Generating a random number to represent the computer's choice
    random_number = random.randint(0, 2)
    # Mapping the random number to the corresponding option
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    # Printing the computer's choice
    print("Computer picked", computer_pick + ".")

    # Determining the winner based on user and computer choices
    # Introduction to if-else statements
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1

# Printing the final results
# Introduction to variables and printing output
print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")
