print("----- SMART HEALTH MENU SYSTEM -----")

name = ""
age = 0
height = 0.0
weight = 0.0

while True:
    print("\nMenu Options:")
    print("1. Add Patient Basic Details")
    print("2. View Patient Details")
    print("3. Calculate BMI")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # Option 1: Add details
    if choice == "1":
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        height = float(input("Enter Height (in meters): "))
        weight = float(input("Enter Weight (in kg): "))
        print("Patient details added successfully!")

    # Option 2: View details
    elif choice == "2":
        if name == "":
            print("No patient data available!")
        else:
            print("\n--- Patient Details ---")
            print(f"Name   : {name}")
            print(f"Age    : {age}")
            print(f"Height : {height} m")
            print(f"Weight : {weight} kg")

    # Option 3: Calculate BMI
    elif choice == "3":
        if height == 0:
            print("Please add patient details first!")
        else:
            bmi = weight / (height ** 2)
            print(f"BMI = {bmi:.2f}")

    # Option 4: Exit
    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
