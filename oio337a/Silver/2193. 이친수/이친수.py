# 이친수

import sys
input = sys.stdin.readline

'''
1 = 1   1
2 = 1   10
3 = 2   101, 100
4 = 3   1010, 1001, 1000
5 = 5   10101, 10100, 10010, 10000, 10001
6 = 8   101010, 101001, 101000, 100101, 100100, 100001, 100000, 100010
'''

def main(n):
  dp[1] = 1
  dp[2] = 1

  for i in range(3, n + 1):
    dp[i] = dp[i - 2] + dp[i - 1]

  print(dp[n])
  return

n = int(input())
dp = [0] * (n + 1)
if n == 1 or n == 2:
  print(1)
else:
  main(n)