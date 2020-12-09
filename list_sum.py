Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:36:03) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from typing import List
>>> def list_sum(xs: List[int]) -> int:
	i = 0
	sum = 0
	while i < len(xs):
		sum += xs[i]
		i += 1
	return sum

>>> list_sum([1,2,3,4,5])
15
>>> 
