
def cyclic_shift(A:list, N:int, dest):
	""" cyclic_shift A:list.
		N - length A.
		dest - destination of shift
	"""
	if dest == 'l':
		T = A[0]
		for k in range(N-1):
			A[k] = A[k+1]
		A[N-1] = T
	elif dest == 'r':
		T = A[N-1]
		for k in range(1, N):
			A[N-k] = A[N-k-1]
		A[0] = T

def test_invert_array():
	A1 = [1, 2, 3, 4, 5]
	cyclic_shift(A1, 5, 'l')
	print(A1)
	if A1 == [2, 3, 4, 5, 1]:
		print('#test1 - ok')
	else:
		print('#test1 - fail')

	A2 = [5, 4, 3, 2, 1]
	cyclic_shift(A2, 5, 'r')
	if A2 == [1, 5, 4, 3, 2]:
		print('#test2 - ok')
	else:
		print('#test2 - fail')
			
test_invert_array()