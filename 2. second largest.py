def second_largest(a:int, b:int, c:int) -> int:
    """
    returns second largest number out of a sequence of numbers
    """
    final = a + b + c - max(a,b,c) - min(a,b,c)
    return final
