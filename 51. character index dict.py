from typing import List
from typing import Dict

def char_index(xs: str) -> Dict[str, List[int]]:
    """
    >>> char_index("")
    {}
    >>> char_index("aaAAbbBB")
    {‘a’: [0, 1], ‘b’: [4, 5]:, ‘A’: [2, 3], ‘B’: [6, 7]}
    """
    index = {}
    for char in xs:
        if char not in index:
            index[char] = xs.find(char)
        else:
            index[char] += xs.find(char)
    return index
        
