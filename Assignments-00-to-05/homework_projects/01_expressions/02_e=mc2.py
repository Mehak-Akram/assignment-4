#Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula 
#(E stands for energy, m stands for mass, and C is the speed of light:

C = 299792458  

def mass_to_energy(mass):
    return mass * C**2

def main():
    while True:
        try:
            mass = float(input("Enter kilos of mass: "))
            energy = mass_to_energy(mass)
            print("\ne = m * C^2...\n")
            print(f"m = {mass} kg\n")
            print(f"C = {C} m/s\n")
            print(f"{energy:.6e} joules of energy!\n")
        except ValueError:
            print("Exiting program.")
            break

if __name__ == "__main__":
    main()
