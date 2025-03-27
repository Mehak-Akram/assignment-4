import random
import string
import pyperclip

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    """Generates a secure password based on user preferences."""
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        print("❌ You must select at least one character type!")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_strength(password):
    """Determines password strength."""
    length_score = len(password)
    digit_score = sum(c.isdigit() for c in password)
    symbol_score = sum(c in string.punctuation for c in password)
    
    score = length_score + digit_score + symbol_score
    
    if score < 10:
        return "⚠️ Weak"
    elif score < 20:
        return "✅ Medium"
    else:
        return "💪 Strong"

# Get user input
length = int(input("🔢 Enter password length: "))
use_upper = input("🔠 Include Uppercase letters? (y/n): ").lower() == 'y'
use_lower = input("🔡 Include Lowercase letters? (y/n): ").lower() == 'y'
use_digits = input("🔢 Include Numbers? (y/n): ").lower() == 'y'
use_symbols = input("🔣 Include Symbols? (y/n): ").lower() == 'y'

password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)

if password:
    print("\n🎉 Your Generated Password: ", password)
    print("🔑 Strength: ", password_strength(password))
    pyperclip.copy(password)
    print("📋 Password copied to clipboard!")
