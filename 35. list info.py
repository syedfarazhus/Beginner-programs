from typing import List

def list_info(xs:List[int]) -> List[int]:
    """
    when given a non-empty integer list, returns a list comprised of the:
    1. smallest value in the list,
    2. largest value in the list, and the
    3. value closest to the average of the smallest and largest (i.e.
    the middle value).
    >>>list_info([1 , 11 , 7 , 3 , 23])
    [1, 23, 11]
    """
    
    info = []
    avg = (max(xs) + min(xs)) / 2
    close = 0
    
    info.append(min(xs))
    info.append(max(xs))
    
    for i in xs:
        if abs( avg - i ) < abs(avg - close):
            close = i
    
    info.append(close)
    return info
        
