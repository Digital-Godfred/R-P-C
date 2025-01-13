import random

options = ["Rock","Paper","Scissors"]

player_choice = input("Rock, Paper or Scissors: ")
computer_choice = random.choice(options)

print("You chose: ", player_choice)
print("Computer chose ", computer_choice)

if player_choice == computer_choice:
    print("It's a tie")
    
elif player_choice == "Scissors" and computer_choice == "Paper":
    print("You win")

elif player_choice == "Paper" and computer_choice == "Rock":
    print("You win")

elif player_choice == "Rock" and computer_choice == "Scissors":
    print("You win")

else:
    print("Bitch you lost")
