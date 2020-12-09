Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:36:03) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def is_palindrome(statement: str) -> bool:
        '''detects if a string is a palindrome but
        ignoring whitespace and ignoring case.
        '''
	statement = statement.lower().strip()
	reverse = ''
	for char in statement:
		reverse = char + reverse
	return statement == reverse
