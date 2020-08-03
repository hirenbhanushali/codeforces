x1, y1, x2, y2 = map(int, input().split())
if x1 != x2 and y1 != y2 and abs(x1 - x2) != abs(y1 - y2):
    print(-1)
elif x1 == x2:
    print(str(x1 + abs(y1 - y2)) + " " + str(y1) + " " +
          str(x2 + abs(y1 - y2)) + " " + str(y2))
elif y1 == y2:
    print(str(x1) + " " + str(y1 + abs(x1 - x2)) +
          " " + str(x2) + " " + str(y2 + abs(x1 - x2)))
else:
    print(str(x1) + " " + str(y2) + " " + str(x2) + " " + str(y1))
# it will be better to calculate absolute difference and store it in a
# variable and then print all variables without using str and " "
