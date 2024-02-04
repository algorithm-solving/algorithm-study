# 나머지 합

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num_li = list(map(int, input().split()))

r = [0] * m
prefix = 0
for i in range(n):
  prefix += num_li[i]
  r[prefix % m] += 1

answer = r[0]

for i in range(m):
  answer += r[i] * (r[i] - 1) // 2
print(answer)