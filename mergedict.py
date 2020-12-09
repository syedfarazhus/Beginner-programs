from typing import List
from typing import Dict

def merge(d1: Dict, d2: Dict) -> Dict:
    """add all pairs from d2 into d1"""
    for key in d2:
        if key not in d1:
            d1[key] = d2[key]
        else:
            d1[key] += d2[key]
    return d1

def combine(d1:Dict, d2:Dict) -> Dict:
    """create new dict out of d1 and d2"""
    new_d = {}
    for key in d1:
        if key in d2:
            new_d[key] = sum(d1[key]) + sum(d2[key])
    return new_d

def sum_d(d, item):
    count = 0
    for key in d:
        for stats in d[key]:
            if item == stats:
                count += d[key][stats]
    return count

weapons = {
'sword': {'steel': 151,'sharpness': 100},
'arrow': {'steel': 120,'sharpness': 205,'age': 1}
}
 
