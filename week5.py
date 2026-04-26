# Week - 5

health_info = ("Blood Group: O+", "DOB: 12-05-2005")

conditions = set()

patient = {}

patient["id"] = int(input("Enter Patient ID: "))
patient["name"] = input("Enter Patient Name: ")
patient["age"] = int(input("Enter Age: "))

n = int(input("Enter no. of medical conditions: "))

for i in range(n):
    cond = input("Enter Condition: ")
    conditions.add(cond)

patient["health_info"] = health_info
patient["conditions"] = conditions

print("\n--- Patient Medical Record ---")
print("ID:", patient["id"])
print("Name:", patient["name"])
print("Age:", patient["age"])
print("Health Info:", patient["health_info"])
print("Medical Conditions:", patient["conditions"])
