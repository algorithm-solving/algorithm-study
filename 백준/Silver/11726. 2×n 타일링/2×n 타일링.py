# 2xn 타일링

import sys
input = sys.stdin.readline

'''
1 = 1
2 = 2
3 = 3 111, 1=, =1
4 = 5 1111, 11=, 1=1, =11, ==
'''

n = int(input())
dp = [0] * (n + 1)

def f(n):
  dp[1] = 1
  dp[2] = 2
  for i in range(3, n + 1):
    dp[i] = (dp[i - 2] + dp[i - 1])%10_007
  print(dp[n])

if n == 1 or n == 2:
  print(n)
else:
  f(n)
