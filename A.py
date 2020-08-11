t = int(input())
sol = []
for i in range(t):
    n = int(input())
    l = [str(x) for x in range(1, n + 1)]
    sol.append(" ".join(l))
for i in sol:
    print(i)
