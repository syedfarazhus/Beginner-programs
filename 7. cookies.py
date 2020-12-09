def cookies(adult:int, teen:int, child:int) -> int:
    """
    returns the number of cookies
    required to serve a specified number of adults, teens, and
    children
    """
    total_cookies = (adult * 3) + (teen * 5) + (child * 2)
    return total_cookies
