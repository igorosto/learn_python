x = int(input('input x: ') or 0)

if x < 0:
	print('A')
elif x < 5: # x >= 0
	print('B')
elif x < 10:  # x >= 5
	print('C')
else:  # x >= 10
	print('D')