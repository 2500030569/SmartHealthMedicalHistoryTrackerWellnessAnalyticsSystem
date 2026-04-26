# Assuming a base class Record exists
class Record:
    def __init__(self, record_id):
        self.record_id = record_id


class PatientRecord(Record):
    def __init__(self, record_id, name, age, disease):
        super().__init__(record_id)
        self.name = name
        self.age = age
        self.disease = disease

    def display_record(self):
        print("In-Patient Clinical Record")
        print("Record ID:", self.record_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)


# Input
rid = int(input("Enter Record ID: "))
name = input("Enter Patient Name: ")
age = int(input("Enter Age: "))
disease = input("Enter Disease: ")

# Object creation
patient = PatientRecord(rid, name, age, disease)
patient.display_record()
