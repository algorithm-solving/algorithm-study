# 스티커

import sys
input = sys.stdin.readline

'''
아래 경우 중 max 값을 dp에 저장한다.

1. 전 과정의 dp 값의 위치와 겹치지 않는 현재 위치의 값의 합 dp[i] = dp[i - 1] + data[i]
2. 전 과정을 포기하고 전전 과정의 값과 현재 위치의 더 큰값의 합 dp[i] = dp[i - 2] + data[i]
'''

t = int(input())

for _ in range(t):
  n = int(input())
  dp = [list(map(int, input().split())) for _ in range(2)]  

  if n > 1:
    dp[0][1] += dp[1][0] # 0 윗줄
    dp[1][1] += dp[0][0] # 1 아랫줄
  for i in range(2, n):
    dp[0][i] += max(dp[1][i - 1], dp[1][i - 2])
    dp[1][i] += max(dp[0][i - 1], dp[0][i - 2])

  print(max(dp[0][-1], dp[1][-1]))