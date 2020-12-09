def largest(message:str) -> str:
    biggest = message[0]
    for char in message:
        if ord(char) > ord(biggest):
            biggest = char
    return biggest
    
