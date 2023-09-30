# 1로 만들기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
'''
f(N) = min(f(n/3) + 1, f(n/2) + 1, f(n - 1) + 1)
'''

# 런타임 에러

# n = int(input())
# dp = [False] * 10**6

# def f(n):
#   if (n == 1):
#     return 0
#   elif dp[n] != False:
#     return dp[n]
  
#   result  = (f(n - 1) + 1)
#   if n % 3 == 0:
#     result = min(result, f(n//3) + 1)
#   elif n % 2 == 0:
#     result = min(result, f(n//2) + 1)
#   dp[n] = result
#   return result

# print(f(n))

# 바텀업

n = int(input())
dp = [0] * (n + 1)

for i in range(2, n + 1):
  dp[i] = dp[i - 1] + 1
  if i % 3 == 0:
    dp[i] = min(dp[i], dp[i // 3] + 1)
  if i % 2 == 0:
    dp[i] = min(dp[i], dp[i // 2] + 1)
print(dp[n])