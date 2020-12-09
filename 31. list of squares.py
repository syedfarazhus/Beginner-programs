from typing import List

def squares(k:int) -> List[int]:
    """Return a list of the first k squares.
    >>> squares(1)
    [1]
    >>> squares(3)
    [1, 4, 9]
    """
    squares = []
    for i in range(1, k+1):
        squares.append(i**2)
    return squares
    
        
