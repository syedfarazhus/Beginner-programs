from typing import List

def make_unique(xs: List[int]) -> None:
    """
    given a list of integers, updates the list by
    removing duplicates

    >>> L = [1, 2, 2, 2, 3, 1, 4, -3]
    >>> make_unique(L)
    [1, 2, 3, 4, -3]
    """
   
    new_list = []
    for i in xs:
        if i not in new_list:
            new_list.append(i)
    xs = new_list
    return xs
    
