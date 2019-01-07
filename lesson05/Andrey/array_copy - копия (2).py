N = int(input('input N: ') or 1)
A = [0] * N
B = [0] * N

for k in range(N):
	A[k] = int(input('input item of A: ') or 333)
	
for k in range(N):
	B[k] = A[k]
	
C = A
A[0] = 777
print('B: ', B)
print('C: ', C)

C = list(B)
print('C: ', C)