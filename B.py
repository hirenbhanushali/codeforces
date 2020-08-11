n = int(input())
logs = list(map(int,input().split()))
nevents = int(input())
flag = 0
for i in range(nevents):
    x = input()
    if x[0]=="+":
        logs.append(int(x[2:]))
    else:
        logs.remove(int(x[2:]))
    s = set(logs)
    s = list(s)
    for i in s:
        if logs.count(i) >= 8:
            print("YES")
            break
        elif logs.count(i) >= 6:
            h = s.copy()
            h.remove(i)
            for j in h:
                if logs.count(j) >= 2:
                    print("YES")
                    break
            break
        elif logs.count(i) >= 4:
            h = s.copy()
            h.remove(i)
            for j in h:
                if logs.count(j) >= 4:
                    print("YES")
                    flag = 1
                    break
            if flag==1:
                break
        else:
            print("NO")
            break