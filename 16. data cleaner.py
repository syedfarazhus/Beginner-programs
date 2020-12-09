def clean_data(data:str) -> str:
    """
    Remove all quotes, and discard whitespace at the front and back of the line.
    Then, return a list that contains all of the individual
    tems in the line.
    """
    return data.strip(' ').replace('"','').split(',')
