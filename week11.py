import pandas as pd

class MedicalAnalyzer:
    def __init__(self, data):
        self.df = pd.DataFrame(data)

    def clean_data(self):
        # Fill missing values using forward fill
        self.df.fillna(method='ffill', inplace=True)
        return self.df

    def filter_high_bp(self):
        # Filter patients with systolic BP > 130
        return self.df[self.df['systolic'] > 130]

    def group_by_patient(self):
        # Group by patient and take mean of numeric columns
        return self.df.groupby('Patient').mean(numeric_only=True)

    def summary(self):
        # Statistical summary
        return self.df.describe()


if __name__ == "__main__":
    data = {
        'Patient': ['A', 'A', 'B', 'B', 'C'],
        'heart_rate': [72, 75, 80, None, 90],
        'systolic': [120, 135, 140, 128, 150],
        'diastolic': [80, 85, 90, 88, 95]
    }

    analyzer = MedicalAnalyzer(data)

    print("Cleaned Data:\n", analyzer.clean_data())
    print("\nHigh BP Patients:\n", analyzer.filter_high_bp())
    print("\nGrouped Data:\n", analyzer.group_by_patient())
    print("\nSummary:\n", analyzer.summary())
