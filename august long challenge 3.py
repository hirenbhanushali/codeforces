t = int(input())
sol = []
for i in range(t):
	c,r = map(int,input().split())
	dc = 1
	dr = 1
	if c>=10:
		if c%9==0:
			dc=c//9
		else:
			dc=(c//9)+1
	if r>=10:
		if r%9==0:
			dr=r//9
		else:
			dr=(r//9)+1
	if dc<dr:
		sol.append("0"+" "+str(dc))
	else:
		sol.append("1"+" "+str(dr))
for i in sol:
	print(i)