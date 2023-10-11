from sys import stdin

read = stdin.readline

N, K = map(int, read().split())
values = [0 for _ in range(K + 1)]
for _ in range(N):
    W, V = map(int, read().split())
    for weight in range(K, W - 1, -1):
        values[weight] = max(values[weight], values[weight - W] + V)
print(values[K])
