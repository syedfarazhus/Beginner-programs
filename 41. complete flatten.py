from typing import List

def flatten(L: List) -> List:
    """ Return a list of literals comprising L --
    without necessarily preserving ordering.
    
    >>> flatten([[1, 2], [], [[3], [4, 5]])
    [1, 2, 3, 4, 5]
    >>> flatten([])
    
    """
    flat = []
    
    if L == []:
        return None

    for sub in L:
        for items in sub:
            for item in items:
                flat.append(item)
    return flat
            
    
    
