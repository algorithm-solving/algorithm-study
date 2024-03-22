import sys
input = sys.stdin.readline
"""
dp[2] = dp[1] + cost[1] or dp[0] + cost[2]

dp[3] = dp[2] + cost[1] or dp[1] + cost[2] or dp[0] + cost[3]

dp[4] = dp[3] + cost[1] or dp[2] + cost[2] or dp[1] + cost[3] or dp[0] + cost[4]
"""
n = int(input())
dp = [0] * (n+1)
cost = [0] + list(map(int, input().split()))
dp[1] = cost[1]

for i in range(2, n+1):
    for j in range(1, i + 1):
        if dp[i] < dp[i - j] + cost[j]:
            dp[i] = dp[i - j] + cost[j]

print(dp[n])
