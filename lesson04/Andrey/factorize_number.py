# -*- coding: utf-8 -*
def factorize_number(x):
	'''
		Раскладывает число на множители
		x - целое положительное число
		Выводит на экран
	'''
	divisor = 2
	while x > 1:
		if x % divisor == 0:
			print(divisor)
			x //= divisor
		else:
			divisor += 1

help(factorize_number)

x = 1024
print('factorize_numbers of ', x, ':')
factorize_number(x)
