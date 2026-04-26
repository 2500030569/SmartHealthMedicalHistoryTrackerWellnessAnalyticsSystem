print("----- Patient Basic Profile -----")

name = input("Enter Patient Profile Name: ")
age = int(input("Enter Age: "))
gender = input("Enter Gender: ")
blood_group = input("Enter Blood Group: ")
height = float(input("Enter Height (in cm): "))
weight = float(input("Enter Weight (in kg): "))
phone = input("Enter Phone Number: ")

print("\n--- Patient Profile Summary ---")

print(f"Name        : {name}")
print(f"Age         : {age} years")
print(f"Gender      : {gender}")
print(f"Blood Group : {blood_group}")
print(f"Height      : {height} cm")
print(f"Weight      : {weight} kg")
print(f"Phone No    : {phone}")

print("\nProfile Saved Successfully!")
