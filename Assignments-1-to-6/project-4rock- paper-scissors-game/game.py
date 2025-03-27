import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_user_choice():
    choices = {"rock": "✊", "paper": "✋", "scissors": "✌"}
    choice = input("Enter rock ✊, paper ✋, or scissors ✌: ").lower()
    while choice not in choices:
        print("Invalid choice. Try again.")
        choice = input("Enter rock ✊, paper ✋, or scissors ✌: ").lower()
    return choice

def determine_winner(user, computer):
    choices = {"rock": "✊", "paper": "✋", "scissors": "✌"}
    if user == computer:
        return "It's a tie! ♻"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You win! 🎉"
    else:
        return "Computer wins! 🚀"

def play_game():
    print("Welcome to Rock, Paper, Scissors Game 🎮")
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        choices = {"rock": "✊", "paper": "✋", "scissors": "✌"}
        print(f"You chose: {choices[user_choice]}")
        print(f"Computer chose: {choices[computer_choice]}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1
        
        print(f"Score: You {user_score} - {computer_score} Computer")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! 🎮")
            break

if __name__ == "__main__":
    play_game()
