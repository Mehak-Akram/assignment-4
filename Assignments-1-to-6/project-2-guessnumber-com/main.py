# import random

# def guess_num():
#     """Python Project 2: Guess The Number (Computer)"""
#     num = random.randint(1, 50)
#     guess_left = 7
#     score = 100  
#     print("\n🎉 Welcome to the Number Guessing Game! 🎉")
#     print("🔢 Try to guess the number between 1 and 50! 🎯")

#     while guess_left > 0:
#         print(f"\n🕵️‍♂️ You have {guess_left} guesses left.")
#         try:
#             guess = int(input("👉 Take a guess: "))
#         except ValueError:
#             print("🚫 Invalid input: please enter a number.")
#             continue

#         # Guess the secret number
#         if guess < num:
#             print("📉 Too low! Try again. 🔼")
#             score -= 10
#         elif guess > num:
#             print("📈 Too high! Try again. 🔽")
#             score -= 10
#         else:
#             print(f"🎉 Congratulations! 🎊 You guessed the correct number in {7 - guess_left + 1} tries. 🏆")
#             print(f"🎯 Your final score is: {score} points! 🎯")
#             return

#         guess_left -= 1

#     print(f"\n😢 You ran out of guesses! The number was {num}. Better luck next time! 🍀")
#     print("🚀 Your final score is: 0 points. Try again! 🎮")

# guess_num()

import random

def guess_num():
    """Python Project 2: Guess The Number (Computer)"""
    num = random.randint(1, 50)
    guess_left = 7
    score = 100  
    print("\nWelcome to the Number Guessing Game!")
    print("Try to guess the number between 1 and 50!")

    while guess_left > 0:
        print(f"\nYou have {guess_left} guesses left.")
        try:
            guess = int(input("Take a guess: "))
        except ValueError:
            print("Invalid input: please enter a number.")
            continue

        # Guess the secret number
        if guess < num:
            print("Too low! Try again.")
            score -= 10
        elif guess > num:
            print("Too high! Try again.")
            score -= 10
        else:
            print(f"Congratulations! You guessed the correct number in {7 - guess_left + 1} tries.")
            print(f"Your final score is: {score} points!")
            return

        guess_left -= 1

    print(f"\nYou ran out of guesses! The number was {num}. Better luck next time!")
    print("Your final score is: 0 points. Try again!")

guess_num()

