# pip install numpy
import numpy as np

# Function to generate a random dataset
def generate_data(size=100):
    return np.random.randint(1, 100, size)

# Function to analyze data
def analyze_data(data):
    print("Analyzing dataset...")
    print(f"Mean: {np.mean(data)}")
    print(f"Median: {np.median(data)}")
    print(f"Standard Deviation: {np.std(data)}")
    print(f"Min Value: {np.min(data)}")
    print(f"Max Value: {np.max(data)}")

# Main function to run the analysis tool
def data_analysis_tool():
    print("Welcome to the Data Analysis Tool")

    # Generate random data
    data_size = int(input("Enter the size of the dataset: "))
    data = generate_data(data_size)
    
    print("\nGenerated Dataset:")
    print(data)

    # Analyze the dataset
    analyze_data(data)

# Run the data analysis tool
if __name__ == "__main__":
    data_analysis_tool()


# Sample interaction
# Welcome to the Data Analysis Tool
# Enter the size of the dataset: 10

# Generated Dataset:
# [12 85 46 23 89 67 30 56 19 91]

# Analyzing dataset...
# Mean: 51.8
# Median: 51.0
# Standard Deviation: 28.15367126288746
# Min Value: 12
# Max Value: 91
