import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

rounds = int(input("How many rounds do you want to play? "))

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

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
    rounds -= 1
    
    if rounds == 0:
        if user_wins > computer_wins:
            print("You won", user_wins, "out of", rounds + "games. You won the game!")
        elif computer_wins > user_wins:
            print("You won", computer_wins, "out of", rounds + "games. You lost the game!")
        else:
            print("You tied the game!")
        break