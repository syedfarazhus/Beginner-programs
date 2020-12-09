Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:36:03) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> def roll_sum(num: int) -> int:
	'''accumulates the result of dice rolls until a given
	sum is accumulated and returns the number of rolls required
	'''
	i = 0
	x = 0
	while x != num:
		y = random.randint(1, 6)
		print(y)
		x += y
		i += 1
	return 'it took ' + str(i) + ' rolls'

>>> roll_sum(24)
1
3
6
1
6
5
2
'it took 7 rolls'
>>> 
