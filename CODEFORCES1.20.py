import math
n, x = map(int, input().split())
half = n / 2
half = math.ceil(half)
if x > half:
    x -= half
    print(x * 2)
else:
    print((x * 2) - 1)

# a,b=map(int,input().split())
# c=b-(a+1)//2
# print ([2*b-1,2*c][c>0]
