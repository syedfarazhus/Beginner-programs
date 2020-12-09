import math

SLICES_PER_PIZZA = 8

def pizzas(adult:int, teen:int, child:int) -> int:
    """
    returns the number of pizzas
    required to serve a specified number of adults, teens, and
    children
    """
    total_slices = (adult * 2) + (teen * 3) + (child * 1)
    total_pizzas = math.ceil(total_slices / SLICES_PER_PIZZA)
    return total_pizzas
