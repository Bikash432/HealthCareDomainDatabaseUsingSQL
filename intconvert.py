import pandas as pd

# Step 1: Define the path to your CSV file
excel_file_path = r"D:\RDBMS\Final_Project\medical_credentials1.csv"
output_file_path = r"D:\RDBMS\Final_Project\medical_credentials2.csv" 

# Read the CSV file
df = pd.read_csv(excel_file_path)

# Convert the 'Date' column to datetime if it's not already
#df['Graduation_Year'] = pd.to_datetime(df['Graduation_Year'], errors='coerce')

# Convert the datetime to integer (e.g., Unix timestamp)
df['Graduation_Year'] = df['Graduation_Year'].astype(int)

# Save the modified DataFrame to a new CSV file
df.to_csv(output_file_path, index=False)

print(df.head())
