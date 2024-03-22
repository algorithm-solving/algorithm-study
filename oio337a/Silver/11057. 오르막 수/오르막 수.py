# 오르막 수

'''

1 2 3 4 5 6 7 8 9

1 1 1 1 1 1 1 1 1
1 2 3 4 5 6 7 8 9
1 3 6 10 15 21 28 36 45 55

'''
n = int(input())
dp = [1] * 10
MOD = 10_007

for i in range(1, n):
  for j in range(1, 10):
    dp[j] += dp[j - 1]

# print(dp)
print(sum(dp) % MOD)