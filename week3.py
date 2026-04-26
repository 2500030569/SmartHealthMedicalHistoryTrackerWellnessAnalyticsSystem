print("---- VITAL SIGNS LOG SYSTEM ----")

vitals_list = []

while True:
    print("\nMenu:")
    print("1. Add Vital Record")
    print("2. View All Records")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    # Option 1: Add record
    if choice == "1":
        date = input("Enter Date (DD-MM-YYYY): ").strip()
        bp = input("Enter Blood Pressure (e.g., 120/80): ").strip()
        sugar = float(input("Enter Blood Sugar Level: "))
        heart_rate = int(input("Enter Heart Rate (bpm): "))

        record = f"Date: {date}, BP: {bp}, Sugar: {sugar}, Heart Rate: {heart_rate}"

        vitals_list.append(record)

        print("Vital record added successfully!")

    # Option 2: View records
    elif choice == "2":
        if len(vitals_list) == 0:
            print("No vital records available!")
        else:
            print("\n--- All Vital Records ---")
            for v in vitals_list:
                print(v)

    # Option 3: Exit
    elif choice == "3":
        print("Exiting system... Thank you!")
        break

    # Invalid choice
    else:
        print("Invalid choice! Please try again.")
        
