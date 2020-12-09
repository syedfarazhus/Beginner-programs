from typing import TextIO

def num_empty_lines(file:TextIO) -> int:
    count = 0
    for line in file:
        if line == '\n':
            count += 1
    return count
        
