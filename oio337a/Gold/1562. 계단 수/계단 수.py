import sys
input = sys.stdin.readline

mod = 1_000_000_000

n = int(input())

dp = [[[-1] * 11 for _ in range(101)] for _ in range(1 << 11)]


def go(f, b, x):
    if x < 0 or x > 9:
        return 0
    if b == n:
        if f == (1 << 10) - 1:
            return 1
        else:
            return 0
    if dp[f][b][x] != -1:
        return dp[f][b][x]
    dp[f][b][x] = 0
    if x == 0:
        dp[f][b][x] = go(f | (1 << (x + 1)), b + 1, (x + 1))
        dp[f][b][x] %= mod
    elif x == 9:
        dp[f][b][x] += go(f | (1 << (x - 1)), b + 1, (x - 1))
        dp[f][b][x] %= mod
    else:
        dp[f][b][x] += go(f | (1 << (x + 1)), b + 1, (x + 1))
        dp[f][b][x] %= mod
        dp[f][b][x] += go(f | (1 << (x - 1)), b + 1, (x - 1))
        dp[f][b][x] %= mod
    return dp[f][b][x]


ans = 0

for i in range(1, 10):
    ans += go(1 << i, 1, i)
    ans %= mod
print(ans)
