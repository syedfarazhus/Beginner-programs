from typing import List

def count(xs: List[int], ys: List[int]) -> int:
    count = 0
    for i in ys:
        if i in xs:
            count += 1
    return count
             
            
