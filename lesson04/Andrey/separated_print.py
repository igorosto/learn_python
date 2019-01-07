
def hello_separated(name='World', separator="-"):
	print('Hello, ', name, sep=separator)
	
hello_separated('John', '***')
hello_separated(separator='***')
hello_separated(separator='***', name='John')
