def remove_largest(message:str) -> str:
    biggest = message[0]
    for char in message:
        if ord(char) > ord(biggest):
            biggest = char
    final_message = message.replace(biggest, '')
    return final_message
    
