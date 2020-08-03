n, m = map(int, input().split())
if m > n:
    print(-1)
else:
    for i in range((n + 1) // 2, n + 1):
        if i % m == 0:
            break
    print(i)
