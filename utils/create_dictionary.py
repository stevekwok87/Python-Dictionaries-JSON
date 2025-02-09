def create_dictionary(rowIndex, colIndex, dataTable):

    '''
    Function to create a dictionary from user input data

    Inputs:
        rowIndex (list): The indices of the rows
        colIndex (list): The indices of the columns
        dataTable (numpy array): The data table

    Returns:
        dataDictionary (dict): A dictionary containing the data
    '''

    dataDictionary = {
        'rowIndex': rowIndex,
        'colIndex': colIndex,
        'dataTable': dataTable
    }

    return dataDictionary