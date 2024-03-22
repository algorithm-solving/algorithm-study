# 모노티지털 표현

import sys
input = sys.stdin.readline

k = int(input())
n = int(input())

dp = [set() for _ in range(9)]
for i in range(1, 9):
    dp[i].add(k * int('1' * i))
    for j in range(1, i):
        for x in dp[j]:
            for y in dp[i - j]:
                dp[i].add(x * y)
                dp[i].add(x + y)
                dp[i].add(abs(x - y))
                if y != 0:
                    dp[i].add(x // y)

for _ in range(n):
    num = int(input())
    for i in range(1, 9):
        if num in dp[i]:
            print(i)
            break
        if i == 8:
            print("NO")