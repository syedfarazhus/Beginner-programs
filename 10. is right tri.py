def is_right_tri(a:int, b:int, c:int) -> bool:
    """
    returns true if the given side values of a triangle are from a right triangle
    """
    side1 = min(a,b,c)
    side2 = a + b + c - max(a,b,c) - min(a,b,c)
    hyp = max(a,b,c)
    return side1**2 + side2**2 == hyp**2
