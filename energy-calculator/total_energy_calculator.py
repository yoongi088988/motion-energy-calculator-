def calculate_energy():
	print("--- Energy Calculator ---")
	
	# 1. Get user input
	mass = float(input("Enter mass (kg): "))
	velocity = float(input("Enter velocity (m/s): "))
	height = float(input("Enter height (m): "))
	
	# 2. Physics constants
	g = 9.8 #Gravity on Earth
	
	# 3. Calculations
	kinetic_energy = 0.5 * mass * (velocity ** 2)
	potential_energy = mass * g * height
	total_energy = kinetic_energy + potential_energy 
	
	# 4. Show results
	print("\n--- Results ---")
	print(f"Kinetic Energy: {kinetic_energy} Joules")
	print(f"Potential Energy: {potential_energy} Joules")
	print(f"Total Mechanical Energy: {total_energy} Joules")
	
# 5. Run the function
calculate_energy()