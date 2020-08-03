t = int(input())
n = []
for i in range(t):
    n.append(int(input()))


def printn(n, k=1):
    if n == 0:
        return k
    print(k, end=" ")
    return printn(n - 1, k + 1)
for i in n:
    printn(i)
    print()
