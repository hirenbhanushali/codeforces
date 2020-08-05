t = int(input())
n = []
for i in range(t):
    x, y = map(int, input().split())
    n.append((x, y))


def toh(n, val, a=1, b=2, c=3):
    moves = (2**n) - 1
    for i in range(1, moves + 1):
        if i % 3 == 1:
            print(str(a) + " " + str(c))
        elif i % 3 == 2:
            print(str(a) + " " + str(b))
        elif i % 3 == 0:
            print(str(b) + " " + str(c))
for i in n:
    toh(i[0], i[1])
