t = int(input())
sol = []


def numberOfPaths(m, n):
    if(m == 1 or n == 1):
        return 1
    return numberOfPaths(m - 1, n) + numberOfPaths(m, n - 1)
for i in range(t):
    m, n = map(int, input().split())
    sol.append(numberOfPaths(m, n))
for i in sol:
    print(i)
