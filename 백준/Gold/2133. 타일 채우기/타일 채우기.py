
n = int(input())
dp = [0 for i in range(31)]  # n의 범위가 30까지
dp[2] = 3
for i in range(4, n+1):
    if i % 2 == 0:
        dp[i] = dp[i-2] * 3 + sum(dp[:i-2]) * 2 + 2

print(dp[n])
