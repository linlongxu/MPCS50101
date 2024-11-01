from HM4_Problem7 import get_computer_choice, determine_winner

while True:
    player_choice = input("Choose rock, paper, or scissors: ").lower()
    if player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice.")
        continue

    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)

    if result == "draw":
        print(f"Both chose {player_choice}. It's a draw!")
    elif result == "player":
        print(f"You chose {player_choice} and computer chose {computer_choice}. You win!")
    else:
        print(f"You chose {player_choice} and computer chose {computer_choice}. Computer wins!")

    if input("Play again? (y/n): ").lower() != 'y':
        break
