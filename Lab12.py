# SmartFarm Environmental Data Analysis with NumPy
# Practice: Arrays, Indexing, Slicing, Arithmetic, Comparisons, Sorting, File I/O

# 1) Import NumPy
import numpy as np

# 2) Load the CSV Dataset
# The file has headers, so skip the first row
data = np.genfromtxt("student_practice_data.csv", delimiter=",", skip_header=1)
print("Dataset loaded successfully!\n")

# 3) Array Attributes
print("=" * 50)
print("3) ARRAY ATTRIBUTES")
print("=" * 50)
print(f"Shape of dataset (rows × columns): {data.shape}")
print(f"Number of elements (size): {data. size}")
print(f"Number of dimensions (ndim): {data.ndim}")
print()

# 4) Indexing
print("=" * 50)
print("4) INDEXING")
print("=" * 50)
# Extract the first row of data
first_row = data[0]
print(f"First row: {first_row}")

# Extract the third row
third_row = data[2]
print(f"Third row: {third_row}")

# Extract the temperature column (column 0)
temperature_col = data[:, 0]
print(f"Temperature column (first 5 values): {temperature_col[:5]}")

# Extract the humidity column (column 2)
humidity_col = data[:, 2]
print(f"Humidity column (first 5 values): {humidity_col[:5]}")
print()

# 5) Slicing
print("=" * 50)
print("5) SLICING")
print("=" * 50)
# Extract the first 5 rows and first 3 columns
first_5_rows_3_cols = data[:5, :3]
print(f"First 5 rows, first 3 columns:\n{first_5_rows_3_cols}\n")

# Extract the last 2 rows and last 2 columns
last_2_rows_2_cols = data[-2:, -2:]
print(f"Last 2 rows, last 2 columns:\n{last_2_rows_2_cols}\n")

# Extract every other row (rows 0,2,4…) and columns 1 to 3
every_other_row = data[::2, 1:4]
print(f"Every other row, columns 1 to 3 (first 3 rows shown):\n{every_other_row[:3]}")
print()

# 6) Arithmetic Operations
print("=" * 50)
print("6) ARITHMETIC OPERATIONS")
print("=" * 50)
# Make a copy to preserve original data
data_modified = data.copy()

# Convert temperature from Celsius to Fahrenheit: F = C * 9/5 + 32
temp_fahrenheit = data_modified[:, 0] * 9/5 + 32
print(f"Temperature in Fahrenheit (first 5): {temp_fahrenheit[:5]}")

# Increase moisture readings (column 1) by 5%
data_modified[:, 1] = data_modified[:, 1] * 1.05
print(f"Moisture increased by 5% (first 5): {data_modified[:5, 1]}")

# Reduce humidity readings (column 2) by 10%
data_modified[:, 2] = data_modified[:, 2] * 0.90
print(f"Humidity reduced by 10% (first 5): {data_modified[:5, 2]}")
print()

# 7) Comparison Operators
print("=" * 50)
print("7) COMPARISON OPERATORS")
print("=" * 50)
# Find all rows where temperature > 25°C
high_temp_rows = data[data[:, 0] > 25]
print(f"Rows where temperature > 25°C: {len(high_temp_rows)} rows found")
if len(high_temp_rows) > 0:
    print(f"First matching row: {high_temp_rows[0]}")

# Find rows where moisture is below 40%
low_moisture_rows = data[data[:, 1] < 40]
print(f"\nRows where moisture < 40%: {len(low_moisture_rows)} rows found")
if len(low_moisture_rows) > 0:
    print(f"First matching row: {low_moisture_rows[0]}")

# Find rows where humidity is between 75% and 85%
humidity_range_rows = data[(data[:, 2] >= 75) & (data[:, 2] <= 85)]
print(f"\nRows where humidity between 75% and 85%: {len(humidity_range_rows)} rows found")
if len(humidity_range_rows) > 0:
    print(f"First matching row: {humidity_range_rows[0]}")
print()

# 8) Sorting
print("=" * 50)
print("8) SORTING")
print("=" * 50)
# Sort the dataset by temperature column (column 0)
sorted_by_temp = data[data[:, 0].argsort()]
print(f"Sorted by temperature (first 3 rows):\n{sorted_by_temp[:3]}")

# Sort the dataset by humidity column (column 2)
sorted_by_humidity = data[data[:, 2]. argsort()]
print(f"\nSorted by humidity (first 3 rows):\n{sorted_by_humidity[:3]}")

# Sort the dataset by moisture column in descending order
sorted_by_moisture_desc = data[data[:, 1].argsort()[::-1]]
print(f"\nSorted by moisture descending (first 3 rows):\n{sorted_by_moisture_desc[:3]}")
print()

# 9) Column-Wise or Row-Wise Operations
print("=" * 50)
print("9) COLUMN-WISE / ROW-WISE OPERATIONS")
print("=" * 50)
# Find the average temperature, moisture, and humidity
avg_temp = np.mean(data[:, 0])
avg_moisture = np.mean(data[:, 1])
avg_humidity = np.mean(data[:, 2])
print(f"Average Temperature: {avg_temp:.2f}°C")
print(f"Average Moisture: {avg_moisture:.2f}%")
print(f"Average Humidity: {avg_humidity:.2f}%")

# Find the maximum and minimum for each column
col_max = np.max(data, axis=0)
col_min = np.min(data, axis=0)
print(f"\nMaximum per column: {col_max}")
print(f"Minimum per column: {col_min}")

# Find the sum of all values
total_sum = np.sum(data)
print(f"\nSum of all values: {total_sum:.2f}")
print()

# 10) Boolean Indexing
print("=" * 50)
print("10) BOOLEAN INDEXING")
print("=" * 50)
# Extract all rows where temperature > 25 AND moisture > 40
condition_and = (data[:, 0] > 25) & (data[:, 1] > 40)
rows_and = data[condition_and]
print(f"Rows where temp > 25 AND moisture > 40: {len(rows_and)} rows")
if len(rows_and) > 0:
    print(f"First matching row: {rows_and[0]}")

# Extract rows where humidity < 80 OR temperature < 22
condition_or = (data[:, 2] < 80) | (data[:, 0] < 22)
rows_or = data[condition_or]
print(f"\nRows where humidity < 80 OR temp < 22: {len(rows_or)} rows")
if len(rows_or) > 0:
    print(f"First matching row: {rows_or[0]}")
print()

# 11) Save Processed Data
print("=" * 50)
print("11) SAVE PROCESSED DATA")
print("=" * 50)
# Save the modified data to a new CSV file
np.savetxt('processed_sensor_data.csv', data_modified, delimiter=',', fmt='%.2f')
print("Processed data saved to 'processed_sensor_data.csv'")



print("\n" + "=" * 50)
print("ANALYSIS COMPLETE!")
print("=" * 50)