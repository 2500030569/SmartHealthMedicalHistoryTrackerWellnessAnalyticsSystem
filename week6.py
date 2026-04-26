# Week - 6

class Patient:
    def __init__(self, patient_id, name, age, disease):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease

    def display_info(self):
        print("\n--- Patient Details ---")
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)


# Input from user
pid = int(input("Enter Patient ID: "))
name = input("Enter Patient Name: ")
age = int(input("Enter Age: "))
disease = input("Enter Disease: ")

# Create object
p1 = Patient(pid, name, age, disease)

# Display details
p1.display_info()
