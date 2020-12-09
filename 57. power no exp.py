def pow(x:int, y:int) -> float:
    """
    Returns x**y
    
    >>> pow(2, 3)
    8
    >>> pow(10, 2)
    100
    >>> pow(500, 0)
    1
    """
    i = 1
    value = x
    if y == 0:
        return 1
    while i != y:
        value *= x
        i += 1
    return value
        
    
    
