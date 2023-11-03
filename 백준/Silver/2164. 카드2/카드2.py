from sys import stdin

read = stdin.readline


def act(num):
    if num == 1:
        return 1
    if num & 1 == 0:
        return act(num // 2) * 2
    return act(num + 1) - 2


N = int(read())
print(act(N))
