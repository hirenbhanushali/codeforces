t = int(input())
sol = []
for i in range(t):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    s = set(l)
    count = []
    for i in s:
        if l.count(i) > 1:
            count.append((i, l.count(i)))
    x = max([x[1] for x in count])
    if x * k < k + x:
        sol.append(x * k)
    else:
        sol.append(x + k)
for i in sol:
    print(i)
