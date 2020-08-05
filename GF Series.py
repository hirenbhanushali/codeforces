sys.setrecursionlimit(10**6)


def gfseries(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return (gfseries(n - 2) * gfseries(n - 2)) - gfseries(n - 1)
print(gfseries())
