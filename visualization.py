import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
file_path = "../data/import pandas as pd
import os

# File paths
input_file_path = "../data/compare_historical_stock_prices.csv"  # Raw data file
output_file_path = "../data/compare_historical_stock_prices..csv"  # Cleaned data file

# Check if the raw data file exists
if os.path.exists(input_file_path):
    # Load the raw dataset
    data = pd.read_csv(input_file_path)

    # Display the first few rows of the dataset
    print("Raw Data Preview:")
    print(data.head())

    # Data Cleaning Steps (Example)
    # Remove rows with missing values
    data = data.dropna()

    # Standardize column names
    data.columns = data.columns.str.strip().str.lower().str.replace(' ', '_')

    # Save the cleaned data to a new file
    data.to_csv(output_file_path, index=False)
    print(f"Cleaned data saved to {output_file_path}")
else:
    print(f"Error: The file '{input_file_path}' does not exist. Please check the file path.").csv"
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print("Cleaned Data Preview:")
print(data.head())

# Visualization 1: Line plot of crime trends over years
plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x='year', y='total_cases', hue='region')
plt.title("Crime Trends by Region")
plt.xlabel("Year")
plt.ylabel("Total Cases")
plt.legend(title="Region")
plt.savefig("../visuals/crime_trends_by_region.png")
plt.show()

# Visualization 2: Bar plot of total crimes by region
region_crimes = data.groupby('region')['total_cases'].sum().reset_index()
plt.figure(figsize=(8, 6))
sns.barplot(data=region_crimes, x='region', y='total_cases')
plt.title("Total Crimes by Region")
plt.xlabel("Region")
plt.ylabel("Total Cases")
plt.xticks(rotation=45)
plt.savefig("../visuals/import pandas as pd
import os

# File paths
input_file_path = "../data/compare_historical_stock_prices.csv"  # Raw data file
output_file_path = "../data/compare_historical_stock_prices..csv"  # Cleaned data file

# Check if the raw data file exists
if os.path.exists(input_file_path):
    # Load the raw dataset
    data = pd.read_csv(input_file_path)

    # Display the first few rows of the dataset
    print("Raw Data Preview:")
    print(data.head())

    # Data Cleaning Steps (Example)
    # Remove rows with missing values
    data = data.dropna()

    # Standardize column names
    data.columns = data.columns.str.strip().str.lower().str.replace(' ', '_')

    # Save the cleaned data to a new file
    data.to_csv(output_file_path, index=False)
    print(f"Cleaned data saved to {output_file_path}")
else:
    print(f"Error: The file '{input_file_path}' does not exist. Please check the file path.").png")
plt.show()
