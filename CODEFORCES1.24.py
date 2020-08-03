strength, n = map(int, input().split())
s = []
x = 0
y = 0
for i in range(n):
    x, y = map(int, input().split())
    t = (x, y)
    s.append(t)
s.sort()
flag = 0
for x in s:
    if strength > x[0]:
        strength += x[1]
    else:
        print("NO")
        flag = 1
        break
if flag == 0:
    print("YES")
