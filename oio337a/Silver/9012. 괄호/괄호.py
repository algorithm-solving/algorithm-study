n = int(input())

for _ in range(n):
    VPS = list(input())
    a = 0
    for i in VPS:
        if i == '(':
            a += 1
        else:
            a -= 1
        if a == -1:
            break
    print("YES") if a == 0 else print("NO")
