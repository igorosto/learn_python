x = int(input('input x: ') or 0)
y = int(input('input y: ') or 0)

if x == 0 or y == 0:
	print('invalid x or y')
else:
	if y > 0:	
		if x > 0:	
			print('I')
		else:
			print('II')
	elif y < 0: 	
		if x < 0:	
			print('III')
		else:
			print('IV')
