def is_palindrome(word:str) -> bool:
    """
    returns true if word is a palindrome
    """
    return word == word[::-1]
