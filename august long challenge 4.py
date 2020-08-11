t = int(input())
sol = []
for i in range(t):
	s = input()
	p = input()
	l = [x for x in s]
	for i in p:
		l.remove(i)
	l.append(p)
	l.sort()
	sol.append("".join(l))
for i in sol:
	print(i)