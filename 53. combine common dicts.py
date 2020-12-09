from typing import List
from typing import Dict

def combine(H1: Dict[int, List[int]], H2: Dict[int, List[int]] ) -> Dict[int, int]:
    """Return the dictionary where each key is a key
    that is in both H1 and H2.

    The value associated with each key in the new
    dictionary is the sum of all the integers associated
    with that key in H1 and H2.

    >>> combine({1: [2], 4: [5, 6]}, {4: [8]})
    {4: 19}
    """
    new = {}

    for key in H1:
        if key in H2:
            new[key] = sum(H1[key] + H2[key])
    return new
