from typing import List
from typing import Dict

def char_freq(msg:str) -> Dict[str, List[int]]:
    freq = {}
    for char in msg:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1
    return freq
    
