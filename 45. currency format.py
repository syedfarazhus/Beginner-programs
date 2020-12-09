def print_money(x: float) -> str:
    """
    t returns a float string-formatted as
    Canadian currency
    >>> print_money(7/3)
    ‘$2.33’
    """
    return "${:.2f}".format(x)
