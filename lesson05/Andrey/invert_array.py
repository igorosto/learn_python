
def invert_array(A:list, N:int):
	""" Invert A:list.
		N - length A.
	"""
	for k in range(N//2):
		# T = A[k]
		# A[k] = A[N-1-k]
		# A[N-1-k] = T
		A[k], A[N-1-k] = A[N-1-k], A[k]

def test_invert_array():
	A1 = [1, 2, 3, 4, 5]
	invert_array(A1, 5)
	if A1 == [5, 4, 3, 2, 1]:
		print('#test1 - ok')
	else:
		print('#test1 - fail')

	A2 = [0, 0, 0, 0, 0, 0, 10]
	invert_array(A2, 7)
	if A2 == [10, 0, 0, 0, 0, 0, 0]:
		print('#test2 - ok')
	else:
		print('#test2 - fail')
			
test_invert_array()