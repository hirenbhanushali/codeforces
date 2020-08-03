levels = int(input())
a = input().split()[1:]
b = input().split()[1:]
c = set(a + b)
print(["Oh, my keyboard!", "I become the guy."][len(c) == levels])
