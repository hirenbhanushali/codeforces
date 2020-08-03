x = input()
length = len(x)
if length < 3:
    print("0")
else:
    x = x[1:length - 1]
    x = x.split(", ")
    s = set(x)
    print(len(s))
print(len(set(input() + ', ')) - 4)
