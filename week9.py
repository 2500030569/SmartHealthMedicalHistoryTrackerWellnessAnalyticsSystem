class InvalidVitalError(Exception):
    def __init__(self, message="Invalid vital data"):
        super().__init__(message)


def validate_heart_rate(hr):
    if hr < 40 or hr > 200:
        raise InvalidVitalError("Heart rate must be between 40 and 200")
    return True


def validate_bp(bp):
    # Simple placeholder validation
    if "/" not in bp:
        raise InvalidVitalError("Invalid BP format")


class Vitals:
    def __init__(self, bp, heart_rate):
        validate_bp(bp)
        validate_heart_rate(heart_rate)
        self.bp = bp
        self.heart_rate = heart_rate

    def display(self):
        print("BP:", self.bp, "HR:", self.heart_rate)


class Patient:
    def __init__(self, name):
        self.name = name
        self.vitals = []

    def add_vitals(self, vital):
        self.vitals.append(vital)

    def show(self):
        print("Patient Name:", self.name)
        for v in self.vitals:
            v.display()


# Main Program
p = Patient("Ram")

try:
    v1 = Vitals("120/80", 75)
    v2 = Vitals("130/90", 250)  # This will raise error

    p.add_vitals(v1)
    p.add_vitals(v2)

except InvalidVitalError as e:
    print("Error:", e)

finally:
    print("Program executed")

p.show()
