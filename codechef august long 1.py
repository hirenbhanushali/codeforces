t = int(input())
sol = []
for i in range(t):
	n,k = map(int,input().split())
	positions = list(map(int,input().split()))
	l = 0
	for i in positions:
		if k%i==0:
			if l==0:
				l=i
			else:
				if k//i<k//l:
					l=i
	if l==0:
		sol.append(-1)
	else:
		sol.append(l)
for i in sol:
	print(i)