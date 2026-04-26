import csv
import os

FILE_NAME = "medical_records.csv"


def add_record(patient_id, name, age, disease):
    file_exists = os.path.exists(FILE_NAME)

    try:
        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(["Patient ID", "Name", "Age", "Disease"])

            writer.writerow([patient_id, name, age, disease])

        print("Record saved in CSV")

    except Exception as e:
        print("File error:", e)


def view_records():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    except FileNotFoundError:
        print("CSV file not found")


# Example usage
# add_record(1, "Ram", 25, "Fever")
# view_records()
