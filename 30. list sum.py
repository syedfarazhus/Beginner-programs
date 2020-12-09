from typing import List

def list_sum(xs: List[int]) -> int:
    """
    get sum of given list

    """
    i = 0
    sum = 0
    while i < len(xs):
        sum += xs[i]
        i += 1
    return sum
    
