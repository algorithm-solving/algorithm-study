# 이항 계수 2

'''
nCk = n! / (n - k)! * k!

f(7) = f(6) + f(5)
'''

# 시간 초과

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 6)

# n, k = map(int, input().split())

# def bino_coef(n, k):
#   if k == 0 or n == k:
#     return 1
#   return bino_coef(n - 1, k) + bino_coef(n - 1, k - 1)

# MOD = 10_007

# print(bino_coef(n, k) % MOD)

def bino_coef(n, k):
  dp = [[0] * (k + 1) for _ in range(n + 1)]

  for i in range(n + 1):
    dp[i][0] = 1
  for i in range(k + 1):
    dp[i][i] = 1
  
  for i in range(1, n + 1):
    for j in range(1, k + 1):
      dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
  
  return dp[n][k]

n, k = map(int, input().split())
MOD = 10_007

print(bino_coef(n, k) % MOD)