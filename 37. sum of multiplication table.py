def sumxtable(num:int) -> int:
    """
    given a positive integer N, adds up the
    numbers in the N × N multiplication table.
    """
    sum = 0
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            sum += i * j
    return sum
            
