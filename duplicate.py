import pandas as pd
import os

# Step 1: Define the path to your CSV file
excel_file_path = r"D:\RDBMS\Final_Project\address.csv"
output_file_path = r"D:\RDBMS\Final_Project\address1.csv"
column_name = 'adrs_id' 

# Verify that the file exists
if not os.path.exists(excel_file_path):
    print(f"Error: The file {excel_file_path} does not exist.")
    exit(1)

# Verify that the file is accessible
try:
    with open(excel_file_path, 'r') as file:
        pass
except PermissionError:
    print(f"Error: You do not have permission to read the file {excel_file_path}.")
    exit(1)

# Step 2: Read the CSV file into a DataFrame
try:
    df = pd.read_csv(excel_file_path)
    df_cleaned = df.dropna()
except Exception as e:
    print(f"Error reading the CSV file: {e}")
    exit(1)

# Step 3: Check if the column exists in the DataFrame
if column_name not in df.columns:
    print(f"Error: The column {column_name} does not exist in the CSV file.")
    print("Available columns:", df.columns.tolist())
    exit(1)

# Remove duplicate keys from the specified column
# Option 1: Keep the first occurrence of each duplicate
df_cleaned = df.drop_duplicates(subset=[column_name], keep='first')

# Step 4: Save the cleaned DataFrame back to a new CSV file
try:
    df_cleaned.to_csv(output_file_path, index=False)
except Exception as e:
    print(f"Error saving the cleaned data to CSV file: {e}")
    exit(1)

print(f"Duplicates removed and cleaned data saved to {output_file_path}")
