import csv

def extract_columns(input_csv, output_csv, columns):
    with open(input_csv, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        # Ensure the specified columns exist in the input CSV
        columns = [col for col in columns if col in reader.fieldnames]

        with open(output_csv, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=columns)
            writer.writeheader()

            for row in reader:
                filtered_row = {col: row[col] for col in columns}
                writer.writerow(filtered_row)

# Example usage
input_csv = r"D:\RDBMS\Final_Project\DAC_NationalDownloadableFile.csv"  # Path to your input CSV file
output_csv = r"D:\RDBMS\Final_Project\facility_affiliation1.csv" # Path to your output CSV file
columns_to_extract = ['Ind_enrl_ID','facility_type' , 'Facility Affiliations Certification Number' , 'Facility Type Certification Number']  # Columns to extract

extract_columns(input_csv, output_csv, columns_to_extract)
