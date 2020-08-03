t = int(input())
n = []
for i in range(t):
    n.append(int(input()))


def toh(n, a=1, b=2, c=3):
    if n == 1:
        print("move disk 1 from rod " + str(a) + " to rod " + str(c))
    else:
        toh(n - 1, a, c, b)
        print("move disk " + str(n) + " from rod " +
              str(a) + " to rod " + str(c))
        toh(n - 1, b, a, c)
for i in n:
    toh(i)
    print((2**i) - 1)
