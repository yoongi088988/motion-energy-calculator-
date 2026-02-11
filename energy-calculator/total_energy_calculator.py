def get_kinetic_energy(mass,velocity):
	kinetic_energy = 0.5 * mass * (velocity**2)
	return kinetic_energy

def get_potential_energy(mass,g,height):
	potential_energy = mass*g*height
	return potential_energy

def get_total_energy(kinetic_energy , potential_energy):
	total_energy = kinetic_energy + potential_energy
	return total_energy
	
def main():
	g = 9.8
	mass = float(input("Enter mass (kg): "))
	velocity = float(input("Enter velocity (m/s): "))
	height = float(input("Enter height (m): "))
	kinetic_energy = get_kinetic_energy(mass,velocity)
	potential_energy = get_potential_energy(mass,g,height) 
	total_energy = get_total_energy(kinetic_energy,potential_energy)
	
	print("\n --- Energy Calculator ---")
	print(f"Kinetic_energy is {kinetic_energy} Joules.")
	print(f"Potential energy is {potential_energy} Joules.")
	print(f"Total energy is {total_energy} Joules.")

if __name__ == "__main__":
    main()

