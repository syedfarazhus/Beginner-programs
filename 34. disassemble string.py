from typing import List

def disassemble(cs:str) -> List[str]:
    """Return a list of characters comprising cs,
    maintaining order.
    >>> disassemble("")
    []
    >>> disassemble("abcdef")
    [‘a’, ‘b’, ‘c’, ‘d’, ‘e’, ‘f’]
    """
    dis = []
    i = 0
    while i < len(cs):
        dis.append(cs[i])
        i += 1
    return dis
        
