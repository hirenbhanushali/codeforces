def josephus(n, k):
    if(n == 1):
        return n
    else:
        return(josephus(n - 1, k) + k - 1) % n + 1
print(josephus(5, 2))
