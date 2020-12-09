from typing import List

def mult(AA:List[List[int]], BB:List[List[int]]) -> List[List[int]]:
    """
    returns the matrix product A × B assuming correct dimensions
    """
    matrix = []
    for x in AA:
        row = []
        for y in BB:
            row.append(x * y) 
        matrix.append(row)
    return matrix
