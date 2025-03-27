#Write a simple joke bot. The bot starts by asking the user what they want. However, your program will only respond to one response: Joke.

# If the user enters Joke then we will print out a single joke. Each time the joke is always the same

PROMPT = "What do you want?"
JOKE = ("Here is a joke for you! Why do programmers prefer dark mode? "
        "Because light attracts bugs!")
SORRY = "Sorry, I only tell jokes."

user_input = input(PROMPT + " ")

if user_input == "Joke":
    print(JOKE)
else:
    print(SORRY)
