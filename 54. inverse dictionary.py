from typing import List
from typing import Dict

def invert_dict(H):
    new_dict = {}
    
    for key in H:
        if H[key] not in new_dict.keys():
            new_dict[H[key]] = [key]
        else:
            new_dict[H[key]].append(key)
    return new_dict
