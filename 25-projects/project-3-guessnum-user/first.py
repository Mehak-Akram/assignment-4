import random

def play_game():
    num = random.randint(1, 50)
    attempts = 5  
    guess_count = 0

    print("🎯 Welcome to the 'Guess The Number' Game!")
    print("🔢 I have selected a number between 1 and 50. Can you guess it?")
    print(f"💡 You have {attempts} attempts. Good luck!\n")

    while guess_count < attempts:
        try:
            guess = int(input("👉 Enter your guess: "))
        except ValueError:
            print("⚠️ Please enter a valid number!")
            continue

        guess_count += 1
        remaining_attempts = attempts - guess_count

        if guess < num:
            print("⬇️ Too Low! Try a higher number.")
        elif guess > num:
            print("⬆️ Too High! Try a lower number.")
        else:
            print(f"🎉 Congratulations! You guessed it right in {guess_count} attempts. 🏆")
            break

        if abs(num - guess) <= 3:
            print("🔥 You're very close!")

        if remaining_attempts > 0:
            print(f"🕐 Attempts left: {remaining_attempts}")
        else:
            print(f"❌ Game Over! The correct number was {num}. Better luck next time! 😢")

    replay = input("\n🔄 Do you want to play again? (yes/no): ").strip().lower()
    if replay == "yes":
        play_game()
    else:
        print("👋 Thanks for playing! Have a great day!")

play_game()
