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

print(dataDict)