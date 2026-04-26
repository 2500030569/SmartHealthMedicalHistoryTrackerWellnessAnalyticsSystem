vitals_list = []

# Function to add vital record
def add_vitals():
    date = input("Enter Date (DD-MM-YYYY): ")
    bp = input("Enter Blood Pressure (e.g., 120/80): ")
    sugar = float(input("Enter Blood Sugar Level: "))
    heart_rate = int(input("Enter Heart Rate (bpm): "))

    record = {
        "date": date,
        "bp": bp,
        "sugar": sugar,
        "heart_rate": heart_rate
    }

    vitals_list.append(record)
    print("Vital record added successfully!\n")


# Function to view all records
def view_vitals():
    if len(vitals_list) == 0:
        print("No records available!\n")
    else:
        print("\n--- Vital Records ---")
        for v in vitals_list:
            print(f"Date       : {v['date']}")
            print(f"BP         : {v['bp']}")
            print(f"Sugar      : {v['sugar']}")
            print(f"Heart Rate : {v['heart_rate']}")
            print("-------------------------")


# Main menu
while True:
    print("\n--- MENU ---")
    print("1. Add Vital Record")
    print("2. View Vital Records")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        add_vitals()

    elif choice == "2":
        view_vitals()

    elif choice == "3":
        print("Exiting system... Thank you!")
        break

    else:
        print("Invalid choice! Please enter 1-3.\n")
