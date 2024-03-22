from sys import stdin

read = stdin.readline

N, K = map(int, read().split())
coins = [int(read()) for _ in range(N)]
count = 0
for coin in reversed(coins):
    if K == 0:
        break
    if coin > K:
        continue
    count += K // coin
    K %= coin
print(count)
