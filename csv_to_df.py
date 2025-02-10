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
This example imports the same data but into a Pandas dataframe - also stored in the data_dictionary.

"""

# Define the path to the CSV file
file_path = "./rawdata/basic_table.csv"

# Define a blank dictionary for the dataframe to go in
data_dictionary = {}

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Print the first few rows
print(df.head())

# Save to JSON file
print(' ')
print('Saving dataframe to JSON')
df.to_json("dataframe.json", orient="records", indent=4)
print('Saving dataframe to JSON - compete')
print(' ')


# You can also then place in a dictionary
data_dictionary["table_dataframe"] = df

# Define metadata & add to the Data Dictionary
data_dictionary['Title'] = 'Basic Table'
data_dictionary['createdOn'] = '2025-01-15'
data_dictionary['dataDescription'] = 'Example table used to demonstrate import'

# And save that to a JSON file
print(' ')
print('Saving dataframe in dictionary to JSON')

# Serialise the dictionary in preparation for saving to a JSON file
print(data_dictionary['table_dataframe'])
data_dictionary['table_dataframe'] = df.to_dict(orient='records')
print(data_dictionary['table_dataframe'])
with open('dataframe_in_dict.json', 'w') as json_file:
    json.dump(data_dictionary, json_file, indent=4)
print('Saving dataframe in dictionary to JSON - complete')
print(' ')

print(' ')
print('--------')
print(' ')