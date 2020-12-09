def shorter(string1:str, string2:str) -> str:
    """
    given two strings, returns True if the first
    string is shorter and False
    """
    if len(string1) < len(string2):
        return string1
    return string2
