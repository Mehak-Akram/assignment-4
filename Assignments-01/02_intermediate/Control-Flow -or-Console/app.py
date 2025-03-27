import random

def high_low_game(rounds=5):
    score = 0
    print("Welcome to the High-Low Game!")
    
    for round_number in range(1, rounds + 1):
        user_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)
        
        print(f"\nRound {round_number}: Your number is {user_number}")
        guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()
        
        if (guess == "higher" and user_number > computer_number) or (guess == "lower" and user_number < computer_number):
            print("Correct! You get a point.")
            score += 1
        else:
            print("Wrong guess.")
        
        print(f"The computer's number was {computer_number}.")
    
    print(f"\nGame Over! Your final score is {score}/{rounds}.")

high_low_game()
