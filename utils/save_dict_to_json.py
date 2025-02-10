def save_dict_to_json(dictionary, folder_path):
    '''
    Save a dictionary to a JSON file


    Inputs
        dictionary (dict):  The dictionary to save to a JSON file
        folder_path (str):  The path of the folder where the JSON file is to be created
    '''

    import inspect
    import json
    import os

    # Convert the NumPy array to a list
    dictionary["dataTable"] = dictionary["dataTable"].tolist()

    # Get the name of the dictionary and set the file name using the dictionary name
    frame = inspect.currentframe().f_back
    for name, value in frame.f_locals.items():
        if value is dictionary:
            filename = f"{name}.json"
            break
    else:
        raise ValueError("Could not extract dictionary name for us in JSON file name")
        filename = "defaultFilenameDueToError.json"  # Fallback if name is not found

    # Construct the file path from the database folder name and filename
    file_path = os.path.join(folder_path, filename)
    
    # Save dictionary to file
    with open(file_path, "w") as file:
        json.dump(dictionary, file, indent=4)
    
    print(f"Dictionary saved as {filename}")