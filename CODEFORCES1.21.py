n, m, a, b = map(int, input().split())
if (m / b) > (1 / a):
    x = ((n // m) * b) + ((n % m) * a)
    y = (((n // m) * b) + b)
    print(min(x, y))
else:
    print((n * a))
