print(' -= Example 1 =-')
flag = False
N = int(input('input N: ') or 1)
for i in range(N):
	x = int(input('input x'+ str(i) + ': ') or 0)
	flag = (x % 10 == 0) or flag
print(flag)