s = "abBAcC"
while(not(s.islower())):
    if len(s) == 0:
        break
    prev = s[0]
    l = [s[0]]
    for i in range(1, len(s)):
        x = s[i]
        y = prev
        print(x, y)
        if x.lower() == y.lower():
            if s[i].isupper() == prev.islower() or s[i].islower() == prev.isupper():
                print("removing", prev)
                l.remove(prev)
                continue
            else:
                l.append(s[i])
        else:
            l.append(s[i])
        print(l)
        prev = l[-1]
    print(l)
    s = "".join(l)
