import random

def choose_word():
    words = ["python", "developer", "github", "streamlit", "ecommerce", "vscode", "chainlit"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    print("🎉 Welcome to Hangman Game! 🎉")
    
    while attempts > 0:
        print("\n📝 Word: " + display_word(word, guessed_letters))
        guess = input("🔠 Guess a letter: ").lower()

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter! Try again.")
        elif guess in word:
            guessed_letters.add(guess)
            if all(letter in guessed_letters for letter in word):
                print("\n🎊 Congratulations! You guessed the word: 🎉", word.upper())
                break
        else:
            guessed_letters.add(guess)
            attempts -= 1
            print(f"❌ Wrong guess! {attempts} attempts left. 😟")

        if attempts == 0:
            print("\n Game over! The word was: ❗", word.upper())

if __name__ == "__main__":
    hangman()
