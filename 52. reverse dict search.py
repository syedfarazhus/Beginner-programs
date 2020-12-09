from typing import List
from typing import Dict

def reverse_lookup(d: Dict, item) -> List:
    '''
    Returns all keys such that d[keys] == item
    >>> reverse_lookup({1: ‘A’, 19: ‘B’, -31: ‘A’}, ‘A’)
    [1, -31]
    reverse_lookup({1: ‘A’, 19: ‘B’, -31: ‘A’}, ‘C’)
    []
    '''
    new_dict = {}
    
    for key in d:
        if d[key] not in new_dict.keys():
            new_dict[d[key]] = [key]
        else:
            new_dict[d[key]].append(key)
            
    if item not in d.values():
        return []
        
            
    return new_dict.get(item)

        
    
    
