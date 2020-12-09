from typing import List

def fibbo(k:int) -> List[int]:
    """
    given k, returns a list of the first k
    Fibonacci numbers
    >>>fibbo(8)
    [0, 1, 1, 2, 3, 5, 8, 13, 21]
    """

    L = [0,1]
    i = 1
    while len(L) < k + 1:
        new_num = L[i] + L[i-1]
        L.append(new_num)
        i += 1
    return L
    
