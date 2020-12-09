def area_triangle(a:int, b:int, c:int) -> float:
    """
    Takes 3 sides of a triangle and outputs are of triangle
    """
    s = (a + b + c) / 2
    return ( s * (s - a) * (s - b) * (s - c) ) ** (0.5)
