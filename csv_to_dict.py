import csv
import json

# Define the path to the CSV file
file_path = "./rawdata/basic_table.csv"

# Initialize an empty dictionary
data_dict = {}

# Open the CSV file and read its contents
with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Extract the column headings from the first row
    
    # Define the columns in the dictionary
    for key in header:
        data_dict[key] = []

    # Iterate through the rows to populate the dictionary
    for row in reader:
        
        # Loop through each item in the row and add to a seperate list
        for key, value in zip(header, row):
            data_dict[key].append(value)  #Add value to list


# Define metadata & add to the Data Dictionary
data_dict['Title'] = 'Basic Table'
data_dict['createdOn'] = '2025-01-15'
data_dict['dataDescription'] = 'Example table used to demonstrate import'

# Print the resulting dictionary
print(data_dict)

# Save to file
with open('data_dict.json', 'w') as json_file:
    json.dump(data_dict, json_file, indent=4)

print("data_dict saved to 'data_dict.json'")