# 2xn 타일링 2

import sys
input = sys.stdin.readline

'''
1 = 1
2 = 3 11, =, ㅁ 2
3 = 5 111, 1=, =1, 1ㅁ, ㅁ1 4 2^2 + n-2
4 = 11 1111, 11=, 1=1, =11, ==, 11ㅁ, 1ㅁ1, ㅁ11, ㅁㅁ, =ㅁ, ㅁ= 2^3 + n - 2

dp[n] = 2^(n-1) + dp[n - 2]
'''

n = int(input())
dp = [0] * 1_001
dp[1], dp[2] = 1, 3

for i in range(3, n + 1):
  dp[i] = (2**(i - 1) + dp[i - 2])%10_007

print(dp[n])

  
