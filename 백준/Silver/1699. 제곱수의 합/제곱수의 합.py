# 제곱수의 합

'''
1 = 1
2 = 2
3 = 3  
4 = 1  2^2
5 = 2  2^2 + 1
6 = 3  2^2 + 1 + 1
7 = 4  2^2 + 1 + 1 + 1
8 = 2  2^2 + 2^2
9 = 1  3^2
10 = 2 3^2 + 1
11 = 3 
12 = 2 3^2 + 2^2
'''

n = int(input())
dp = [i for i in range(n + 1)]

for i in range(1, n + 1):
  for j in range(1, i):
    if j * j > i:
      break
    if dp[i] > dp[i - j * j] + 1:
      dp[i] = dp[i - j * j] + 1

print(dp[n])