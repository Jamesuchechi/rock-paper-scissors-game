import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "that`s a tie"
    elif (user_choice.lower() == "rock" and computer_choice == "scissors") or \
         (user_choice.lower() == "paper" and computer_choice == "rock") or \
         (user_choice.lower() == "scissors" and computer_choice == "paper"):
        return "you are the winner"
    else:
        return "computer wins, sorry!"
    
def play_game():
    print("Welcome to Rock, Paper and Scissors game!")

    while True:
        user_choice = input("Enter your choice(Rock, Paper, Scissors) or 'k' to quit: ")
        if user_choice.lower() == "k":
            break
        elif user_choice.lower() not in ["rock", "paper", "scissors"]:
            print("Invalid choice, please try again! ")
            continue
        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"\nComputer chose: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))

play_game()
