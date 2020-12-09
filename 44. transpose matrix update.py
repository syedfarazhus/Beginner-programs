from typing import List

def transpose_update(matrix:List[List]) -> List[List]:
    i = 0
    copy = matrix.copy()
    for row in copy:
        row = [copy[0][i], copy[1][i], copy[2][i]]
        matrix[i] = row
        i += 1
    return matrix

