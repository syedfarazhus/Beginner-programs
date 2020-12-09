Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:36:03) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> def dice_roll() -> int:
	''' prints the result of a six-sided dice roll
	until a six is rolled and returns the number of rolls required
	'''
	i = 0
	final = 6
	x = 0
	while x != final:
		x = random.randint(1, 6)
		print(x)
		i += 1
	return 'It took ' + str(i) + ' rolls to get 6'

>>> dice_roll()
1
5
1
6
'It took 4 rolls to get 6'
>>> dice_roll()
4
5
1
6
'It took 4 rolls to get 6'
>>> dice_roll()
3
2
4
3
6
'It took 5 rolls to get 6'
>>> 
