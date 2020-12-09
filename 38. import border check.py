from typing import List

def border_check(imports:List[str], forbidden:List[str]) -> bool:
    """
    given two lists of strings forbidden and imports returns
    False iff any string in forbidden is a substring of any
    string in imports.
    """
    for item in imports:
        for x in forbidden:
            if item in x:
                return False
    return True
