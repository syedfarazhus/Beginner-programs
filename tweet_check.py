Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:36:03) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def tweet_check(word: str) -> bool:
        '''returns False if the candidate word contains any
        characters that are not alphanumeric or underscore
        '''
	for char in word:
		if not ( char.isalnum() or char == '_' ):
			return False
	return True
