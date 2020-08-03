x = 2458


def snum(n, summ=0):
    if n < 10:
        return summ + n
    return snum(n // 10, summ + n % 10)

print(snum(x))
