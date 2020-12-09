Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:36:03) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def count_space(line: str) -> int:
        ''' Counts the number of spaces in a string
        '''
	num_space = 0
	for char in line:
		if char in ' ':
			num_space += 1
	return num_space
