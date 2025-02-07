import csv

def remove_commas_from_column(input_file, output_file, column_name):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        
        if column_name not in fieldnames:
            raise ValueError(f"Column '{column_name}' does not exist in the input file.")
        
        rows = list(reader)
        
        for row in rows:
            row[column_name] = row[column_name].replace(',', '')
        
        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

input_file = r"D:\RDBMS\Final_Project\medical_credentials3.csv" 
output_file = r"D:\RDBMS\Final_Project\medical_credentials4.csv" 
column_name = 'MEDICAL_SCHOOL'

remove_commas_from_column(input_file, output_file, column_name)
print(f"Commas removed from column '{column_name}' and written to '{output_file}'.")
