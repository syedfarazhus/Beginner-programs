Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:36:03) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def guess_num() -> int:
	i = 0
	x = 0
	num = 16
	while int(x) != num:
		x = input('Guess a number.')
		if x == '':
			continue
		elif int(x) < num:
			print("Too Low")
		elif int(x) > num:
			print("Too High")
		
		i += 1
	return "It took you " + str(i) + " guesses"

>>> guess_num()
Guess a number.16
'It took you 1 guesses'
>>> 
