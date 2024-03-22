# 쉬운 계단 수

'''
1 = 1,2,3,4,5,6,7,8,9
2 = 1,2,3,4,5,6,7,8
3 = 2,3,4,5,6,7,8,9
4 = 1,2,3,4,5,6,7,8
'''

n = int(input())
dp = [[0] * 10 for _ in range(n + 1)]
for i in range(1, 10):
  dp[1][i] = 1

MOD = 1_000_000_000

for i in range(2, n + 1):
  for j in range(10):
    if j == 0:
      dp[i][j] = dp[i - 1][1]
    elif j == 9:
      dp[i][j] = dp[i - 1][8]
    else:
      dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[n]) % MOD)