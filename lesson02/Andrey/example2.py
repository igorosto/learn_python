print(' -= Example 2 =-')
flag = True
N = int(input('input N: ') or 1)
for i in range(N):
	x = int(input('input x'+ str(i) + ': ') or 0)
	flag = (flag and
		x % 10 == 0)
print(flag)