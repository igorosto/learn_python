# -*- coding: utf-8 -*
def is_simple_number(x):
	'''
		Определяет, является ли число простым.
		x - целое положительное число
		Возвращает True\/False
	'''
	divisor = 2
	while divisor < x:
		if x%divisor == 0:
			return False
		divisor += 1
		return True

help(is_simple_number)

x = 10		
print(x, 'is_simple_number: ', is_simple_number(x))
