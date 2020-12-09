Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:36:03) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def largest(word: str) -> str:
	x = ''
	for char in word:
		if ord(char) > ord(char - 1)
		x = ord(char)
		
SyntaxError: invalid syntax
>>> ef largest(word: str) -> str:
	x = ''
	for char in word:
		if ord(char) > ord(char - 1):
			x = ord(char)
			
SyntaxError: invalid syntax
>>> def largest(word: str) -> str:
	x = ''
	for char in word:
		if ord(char) > ord(char - 1):
			x = ord(char)
	return x

>>> def largest(word: str) -> str:
	x = ''
	for char in word:
		if ord(char) > ord(char - 1):
			x += char
	return x

>>> largest(wafflez)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    largest(wafflez)
NameError: name 'wafflez' is not defined
>>> largest('wafflez')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    largest('wafflez')
  File "<pyshell#10>", line 4, in largest
    if ord(char) > ord(char - 1):
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> def largest(word: str) -> str:
	x = word[0]
	if len(word) == 1:
		return word
	elif len(word) > 1:
		for char in word:
			if char > x:
			x = char
	return x
SyntaxError: expected an indented block
>>> 
>>> def largest(word: str) -> str:
        ''' determines largest character in a string
        '''
	x = word[0]
	if len(word) == 1:
		return word
	elif len(word) > 1:
		for char in word:
			if char > x:
				x = char
	return x

>>> largest('waffle')
'w'
>>> largest
<function largest at 0x11309c9e0>
>>> def remove_largest(word: str) -> str:
        ''' determines largest character in a string and removes
        it from string
        '''
	x = word[0]
	if len(word) == 1:
		return ''
	elif len(word) > 1:
		for char in word:
			if char > x:
				x = char
	return word.replace(x,'')

>>> remove_largest('waffle')
'affle'
>>> 
