# Maximum Subarray

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n = int(input())
  x = list(map(int, input().split()))
  prefix = [0]
  
  for i in range(n):
    prefix.append(max(prefix[-1] + x[i], x[i]))
  print(max(prefix[1:]))