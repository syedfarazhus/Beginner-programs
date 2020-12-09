from typing import TextIO

def sum_file(file:TextIO) -> int:
    '''
    takes a file containing one number on each
    line and adds the numbers
    '''
    sum = 0
    for line in file:
        sum += int(line)
    return sum
    
