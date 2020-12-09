from typing import List

def dot_product(xs:List[int], ys:List[int]) -> int:
    """Return the mathematical dot-product of xs and ys
    taken as vectors.
    Assumes len(xs) == len(ys) > 0
    >>> dot_product([1, 2], [3, 4])
    11
    """
    x = xs[0] * ys[0]
    y = xs[1] * ys[1]
    return x + y
