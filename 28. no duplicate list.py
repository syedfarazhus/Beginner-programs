from typing import List

def make_unique(xs: List[int]) -> List[int]:
    """
    takes out duplicates froma list
    
    >>> make_unique([1, 2, 3, 4])
    [1, 2, 3, 4]
    >>> make_unique([1, 2, 2, 2, 3, 1, 4, -3])
    [1, 2, 3, 4, -3]
    """
    new_list = []
    for i in xs:
        if i not in new_list:
            new_list.append(i)
    return new_list
