import pandas as pd

def change_column_dtype_and_drop_na(csv_input, csv_output, column_name, new_dtype):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_input)
    df = df[pd.to_numeric(df[column_name], errors='coerce').notnull()]
    df[column_name] = df[column_name].astype(new_dtype)
    df.to_csv(csv_output, index=False)

# Example usage
csv_input = r"D:\RDBMS\Final_Project\medical_credentials2.csv"  # Path to your input CSV file
csv_output = r"D:\RDBMS\Final_Project\medical_credentials3.csv"  # Path to save the modified CSV file

column_name = 'Graduation_Year'  # Column whose datatype needs to be changed
new_dtype = 'int'  # New datatype (e.g., 'int', 'float', 'str')

change_column_dtype_and_drop_na(csv_input, csv_output, column_name, new_dtype)
