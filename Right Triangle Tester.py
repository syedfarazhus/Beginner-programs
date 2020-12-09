Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:36:03) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def is_right_triangle(a:float, b:float, c:float) -> bool:
	"""
	takes 3 sides of a triangle and determines if it is right

	is_right_triangle(3,4,5)
	True

	is_right_triangle(2,3,6)
	False
	"""
	side1 = min(a, b, c)
	side2 = a + b + c - side1 - max(a, b, c)
	return max(a, b, c) == (side1 ** 2 + side2 ** 2) ** 0.5

>>> is_right_triangle(3,4,5)
True
>>> is_right_triangle(2,3,6)
False
>>> 
