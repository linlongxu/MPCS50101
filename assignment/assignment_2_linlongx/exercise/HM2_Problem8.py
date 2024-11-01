#Problem 8
#Linlong Xu

import random

def play_game():
    while True:
        player = input("Choose: rock, paper, or scissors: ")
        if player not in ["rock", "paper", "scissors"]:
            print("You must choose paper, rock, or scissors.")
            play_again = input("Would you like to play again? (y/n): ")
            if play_again == 'n':
                break
            else:
                continue

        computer = random.choice(["rock", "paper", "scissors"])
        print(f"Computer choose {computer}")
        if player == computer:
            print("It's a tie! Let's settle this.")
        elif (player == "rock" and computer == "scissors") or \
             (player == "scissors" and computer == "paper") or \
             (player == "paper" and computer == "rock"):
            print("You win!")
        else:
            print("The computer wins :(")

        play_again = input("Would you like to play again? (y/n): ").lower()
        if play_again == 'n':
            break