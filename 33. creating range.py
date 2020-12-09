from typing import List

def list_range(a:int, b:int, c:int) -> List[int]:
    """Return list(range(a,b,c)) without using range.
    Assumes a, b, c are nonzero integers.
    >>> list_range(0, 4, 1)
    [0, 1, 2, 3]
    >>> list_range(3, 11, 4)
    [3, 7]
    >>> list_range(6, 3, -1)
    [6, 5, 4]
    """
    L = []
    current = a
    while (current < b and c > 0) or (current > b and c < 0):
        L.append(current)
        current += c
    return L
    
    
