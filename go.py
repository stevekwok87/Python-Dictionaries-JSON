"""
Top level run file to demonstrate how to store 2D data tables as JSON files.

The script shows how to store 2D data in a dictionary as a JSON file.  Then
how to load this back.  Note that because JSON files do not support numpy
arrays, an additional step is needed to conevrt the numpy array to a list
before saving as a JSON file.  This step then needs to be reversed when
loading back again.

Author: Steve Kwok

"""
import numpy as np
from utils.create_dictionary import create_dictionary
from utils.save_dict_to_json import save_dict_to_json
import json
import os

# Set the location of the dataabase folder where the JSON files should be stored.
folder_path = 'database'

# Define the data is lists and and a numpy array
rowIndex = [1, 2, 3, 4, 5]

colIndex = [10, 20, 30, 40]

dataTable = np.array([[1.1, 1.2, 1.3, 1.4],
              [2.1, 2.2, 2.3, 2.4],
              [3.1, 3.2, 3.3, 3.4],
              [4.1, 4.2, 4.3, 4.4],
              [5.1, 5.2, 5.3, 5.4]])

# Create the dictionary
dataDict = create_dictionary(rowIndex, colIndex, dataTable)

# Save the dictionary to a JSON file in the database folder
save_dict_to_json(dataDict, folder_path)

# Reload the JSON file to a different dictionary
# Define the name of the file
load_file_name = os.path.join(folder_path, "dataDict.json")

# Load the JSON file
with open(load_file_name, "r") as f:
    dataDictLoaded = json.load(f)

# # Convert the list back to a NumPy array
# dataDictLoaded["dataTable"] = np.array(dataDictLoaded["dataTable"])

print(dataDictLoaded)

# Interpolation test
# ------------------
from scipy.interpolate import interpn

# Define the x & y values where you want to interpolate the data
iRow = 3
iCol = 40

zi = interpn((dataDictLoaded['rowIndex'], dataDictLoaded['colIndex']), dataDictLoaded['dataTable'], (iRow, iCol), method='linear', bounds_error=False, fill_value=None)

# Output the interpolated values
print('Row: ', iRow)
print('Col: ', iCol)
print('Interpolation result: ', zi)
# ------------------