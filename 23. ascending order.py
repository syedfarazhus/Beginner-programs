def ndesc(msg:str) -> bool:
    value = ord(msg[0])
    for i in msg:
        if ord(i) >= value:
            value = ord(i)
        else:
            return False
    return True
