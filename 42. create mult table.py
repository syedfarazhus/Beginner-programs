from typing import List

def mult_table(N: int) -> List[List[int]]:
    '''Return a N x N list of lists containing the N x N
    multiplication table.
    >>> mult_table(1)
    [[1]]
    >>> mult_table(3)
    [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
    >>> mult_table(0)
    []
    '''
    matrix = []
    for x in range(1, N + 1):
        row = []
        for y in range(1, N + 1):
            row.append(x * y) 
        matrix.append(row)
    return matrix
