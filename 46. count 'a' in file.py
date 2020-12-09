from typing import TextIO

def num_a(file:TextIO) -> int:
    count = 0
    for line in file:
        count += file.count('a')
    return count

        
