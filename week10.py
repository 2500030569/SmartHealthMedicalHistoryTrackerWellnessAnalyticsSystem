import numpy as np

class VitalTrends:
    def __init__(self, heart_rate, bp_systolic, bp_diastolic):
        self.heart_rate = np.array(heart_rate)
        self.bp_systolic = np.array(bp_systolic)
        self.bp_diastolic = np.array(bp_diastolic)

    def heart_rate_stats(self):
        return {
            "mean": np.mean(self.heart_rate),
            "max": np.max(self.heart_rate),
            "min": np.min(self.heart_rate),
            "std_dev": np.std(self.heart_rate)
        }

    def blood_pressure_stats(self):
        return {
            "systolic_mean": np.mean(self.bp_systolic),
            "diastolic_mean": np.mean(self.bp_diastolic)
        }


    def detect_abnormal_hr(self):
        abnormal = self.heart_rate[
            (self.heart_rate < 60) | (self.heart_rate > 100)
        ]
        return abnormal.tolist()

    def trend(self):
        diff = np.diff(self.heart_rate)
        return diff.tolist()


if __name__ == "__main__":
    hr = [72, 75, 78, 120, 85, 55, 90]
    sys = [120, 122, 125, 130, 128, 110, 115]
    dia = [80, 82, 85, 90, 88, 70, 75]

    vt = VitalTrends(hr, sys, dia)

    print("Heart Rate Stats:", vt.heart_rate_stats())
    print("BP Stats:", vt.blood_pressure_stats())
    print("Abnormal HR:", vt.detect_abnormal_hr())
    print("HR Trend:", vt.trend())
