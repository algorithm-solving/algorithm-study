from sys import stdin

read = stdin.readline

MAX_COUNT = 10000

n, k = map(int, read().split())
coins = [int(read()) for _ in range(n)]
counts = [0] + [MAX_COUNT + 1 for _ in range(k)]
for coin in coins:
    for i in range(coin, k + 1):
        counts[i] = min(counts[i], counts[i - coin] + 1)
count = counts[k]
print(count if count <= MAX_COUNT else -1)
