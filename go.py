"""
Script to demonstrate how to:
- Import data from a csv into a Pandas dataframe
- Convert to JSON format
- Save to a JSON file

"""

import numpy as np
import pandas as pd
import json


"""
Example showing how to read in a basic table format and put it into an numpy array which is then stored in a dictionary.

"""

filePath = "./data/basicTable.csv"  # Adjust this path based on your file location
DataDictionary = {
    "table_array": np.genfromtxt(filePath, delimiter=',', dtype=None, names=True, encoding='utf-8')
}


"""
This example imports the same data but into a Pandas dataframe - also stored in the DataDictionary.

"""

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(filePath)
DataDictionary["table_dataframe"] = df

# Display the first few rows
print(df.head())
# print(DataDictionary["table_dataframe"].head())

breakpoint()

"""
# Read the Excel file
df = pd.read_excel('your_file.xlsx', sheet_name='Sheet1')

# Define metadata
metadata = {
    "author": "John Doe",
    "createdOn": "2025-01-05",
    "dataDescription": "Sales data"
}

# Convert to JSON
data = df.to_dict(orient='records')

# Combine metadata and data into one dictionary
final_json = {
    "metadata": metadata,
    "data": data
}

# Save to file
with open('output_with_metadata.json', 'w') as json_file:
    json.dump(final_json, json_file, indent=4)

print("Excel data with metadata saved to 'output_with_metadata.json'")

"""