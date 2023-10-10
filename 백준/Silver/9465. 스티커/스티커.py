from sys import stdin

read = stdin.readline

T = int(read())
for _ in range(T):
    n = int(read())
    top, bottom = [[0] + list(map(int, read().split())) for _ in range(2)]
    for i in range(2, n + 1):
        top[i] += max(bottom[i - 1], bottom[i - 2])
        bottom[i] += max(top[i - 1], top[i - 2])
    print(max(top[n], bottom[n]))
