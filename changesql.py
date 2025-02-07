import pyodbc
import pandas as pd

# SQL Server connection settings
server = 'MSI\\SQLEXPRESS01'
database = 'HealthCare_Huge'
trusted_connection = 'yes'  # Use 'yes' for Windows authentication

# Create a connection string
conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection={trusted_connection};'

# File path to your CSV file
csv_file = r"C:\Users\bikas\OneDrive\Desktop\RDBMS\PROJECT\medical_credential4.csv"

# Table name to create or insert into
table_name = 'MEDICAL_CREDENTIALS'


# Function to load CSV data into SQL Server table
def load_csv_into_sql(conn, cursor):
    try:
        # Load CSV data into pandas DataFrame
        df = pd.read_csv(csv_file)

        # Insert DataFrame into SQL Server table
        df.to_sql(name=table_name, con=conn, if_exists='append', index=False)

        print(f"Data loaded from CSV into table '{table_name}' successfully.")
    except FileNotFoundError:
        print(f"CSV file '{csv_file}' not found.")
    except Exception as e:
        print(f"Failed to load data into SQL Server: {e}")

# Connect to SQL Server
try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()


    # Load CSV data into SQL Server table
    load_csv_into_sql(conn, cursor)

    # Close connections
    cursor.close()
    conn.close()

except pyodbc.Error as e:
    print(f'Error connecting to SQL Server: {e}')
