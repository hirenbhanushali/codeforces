s = input()
if int(s) > 0:
    print(int(s))
else:
    length = len(s)
    sCopy = s[:length - 2]
    x = s[length - 1]
    y = s[length - 2] + "0"
    if int(y) > int(x):
        sCopy += x
    else:
        sCopy += str(int(y))
    print(int(sCopy))
# above soln wrong for a test
# n=input();print(max(map(int,(n,n[:-1],n[:-2]+n[-1]))))
