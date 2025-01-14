import random

options = ["Rock","Paper","Scissors"]


    
def play():
    print("Rock, Paper, Scissors")
    print("Win Best of 3 to beat the computer")

    player_score = 0
    computer_score = 0

    while player_score < 3 and computer_score < 3:
        player_choice = input("Rock, Paper, or Scissors: ").capitalize()
        computer_choice = random.choice(options)

        print(f"Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            print("It's a tie")
        elif (player_choice == "Scissors" and computer_choice == "Paper") or \
             (player_choice == "Paper" and computer_choice == "Rock") or \
             (player_choice == "Rock" and computer_choice == "Scissors"):
            print("You win this round")
            player_score += 1
        else:
            print("You lose this round")
            computer_score += 1

    if player_score > computer_score:
        print("Congratulations! You win the game")
        print(f"Player: {player_score} Computer: {computer_score}")
    else:
        print("You lost the game. Better luck next time!")
    
