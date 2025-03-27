GRAVITY = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14,
    "Earth": 1.0
}

def calculate_weight(weight: float, planet: str):
    convert = planet.capitalize()
    
    if convert in GRAVITY:
        calculate = round(weight * GRAVITY[convert], 2)
        print(f"📝 Your weight on {convert} would be {calculate} kg! 🚀")
    else:
        print("\n❌ Your Planet Is Not Found")

def main():
    print("\n🌍 Welcome to the Planetary Weight Calculator\n")
    try:
        user_weight = float(input("Enter your weight on Earth (kg): "))

        print("\nAvailable planets: Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune")
        user_planet = input("\nEnter the planet name: ")

        if not user_planet or not user_weight:
            print("\n⚠️ Please enter a valid number and planet name!")
        else:
            calculate_weight(user_weight, user_planet)
    except ValueError:
        print("❌ Please enter only numbers for weight!")

if __name__ == "__main__":
    main()
