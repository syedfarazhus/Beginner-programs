def string_reverse(message:str) -> str:
    revd = ""
    for char in message:
        revd = char + revd
    return revd

def cappa(message:str) -> str:
    message = message.upper()
    return message

def vowel(message:str) -> bool:
    for char in message:
        if char in 'aeiouAEIOU':
            return True          
    return False

def pal(message:str) -> bool:
    message = message.lower().strip(' ')
    return message == message[::-1]
