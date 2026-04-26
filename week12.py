import matplotlib.pyplot as plt

# Function to plot heart rate
def plot_heart_rate(days, heart_rate):
    plt.figure()
    plt.plot(days, heart_rate, marker='o')
    plt.title("Heart Rate Trend")
    plt.xlabel("Days")
    plt.ylabel("Heart Rate")
    plt.grid()
    plt.savefig("heart_rate.png")
    plt.show()


# Function to plot blood pressure
def plot_bp(days, systolic, diastolic):
    plt.figure()
    plt.plot(days, systolic, label="Systolic")
    plt.plot(days, diastolic, label="Diastolic")
    plt.title("Blood Pressure Trend")
    plt.xlabel("Days")
    plt.ylabel("BP")
    plt.legend()
    plt.grid()
    plt.savefig("bp.png")
    plt.show()


# Main program
if __name__ == "__main__":
    days = [1, 2, 3, 4, 5, 6, 7]
    heart_rate = [72, 75, 78, 80, 76, 74, 77]
    systolic = [120, 122, 125, 130, 128, 126, 124]
    diastolic = [80, 82, 85, 88, 86, 84, 83]

    plot_heart_rate(days, heart_rate)
    plot_bp(days, systolic, diastolic)
