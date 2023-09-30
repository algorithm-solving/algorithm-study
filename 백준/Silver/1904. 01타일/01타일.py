# 01타일

import sys
input = sys.stdin.readline

'''
dp[1] = 1   1
dp[2] = 2   11, 00
dp[3] = 3   111, 001, 100
dp[4] = 5   1111, 0011, 1001, 1100, 0000
'''

# 메모리 초과

def f(n):
  dp[1] = 1
  dp[2] = 2
  for i in range(3, n + 1):
    dp[i] = (dp[i - 2] + dp[i - 1])%15746
  print(dp[n])

n = int(input())
dp = [0] * (n + 1)

if n == 1 or n == 2:
  print(n)
else:
  f(n)