t = int(input())
sol = []
for i in range(t):
    x, y = map(int, input().split())
    l = []
    for i in range(x):
        j = input()
        l.append([a for a in j])
    moves = 0
    for i in range(x):
        if (len(l[i]) != 0):
            if "C" not in l[i]:
                if l[i][-1] == "R":
                    moves += 1
            else:
                moves += l[i].count("D")
    sol.append(moves)
for i in sol:
    print(i)
