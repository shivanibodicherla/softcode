import random

def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return " Congratulations you have  win the game!"
    else:
        return "ohh sorry You have  lose the game !"

def display_result(user_choice, computer_choice, result):
    print(f"\nYou have choosen : {user_choice}")
    print(f"Computer has choosen : {computer_choice}")
    print(f"Result of the game : {result}\n")

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        result = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, result)

        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1

        print(f"Score - Your score : {user_score}, Computer score : {computer_score}\n")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors Game!\n")
    play_game()
