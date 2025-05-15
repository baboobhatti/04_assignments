
# Energy calculation using Einstein's mass-energy equivalence formula => E = m * c**2
# E stands for energy.
# M stands for body mass.
# C is speed of light (constant value = 299792458 m/s)

def energy_joules(c):
    # get body mass from user
    body_mass : float = float(input("Enter body mass(in kg): "))
    energy_e : int = body_mass * (c ** 2)
    print(f"mass of {body_mass} kg is about {energy_e} joules of energy.")

if __name__ == '__main__':
    c : int = 299792458
    energy_joules(c)     