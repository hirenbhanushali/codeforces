import math
with open("in.txt") as file:

    t = int(file.readline())

    sol = []

    for i in range(t):
        s = file.readline()
        if int(s) > 0:
            sol.append(int(s))
        else:
            length = len(s)
            sCopy = s[:length - 3]
            x = s[length - 2]
            y = s[length - 3] + "0"
            if int(y) > int(x):
                sCopy += x
            else:
                sCopy += y
            sol.append(int(sCopy))
            # if int(s[length - 2] + "0") > int(s[length - 1]):
            #    sol.append(sCopy + s[length - 1])
            # else:
            #    sol.append(sCopy + s[length - 2] + "0")
    with open("out.txt", mode="w") as out:
        for i in sol:
            out.write(str(i) + "\n")
