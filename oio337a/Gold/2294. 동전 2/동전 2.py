# 동전 2

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [10_001] * (k + 1)
dp[0] = 0

for coin in coins:
  for i in range(coin, k + 1):
    dp[i] = min(dp[i], dp[i - coin] + 1)

print(-1) if dp[k] == 10_001 else print(dp[k])