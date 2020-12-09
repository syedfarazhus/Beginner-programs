from typing import List

def col_sums(lst: List[List[int]]) -> List[int]:
    '''
    Return a new list that contains the sum of each column in lst.
    All columns in lst are of the same length.

    >>> col_sums([[5, 10, 15], [1, 2, 3]])
    [6, 12, 18]
    '''
    nl = []
    for i in range(3):
	    nl.append((lst[0][i]+lst[1][i]))
    return nl
