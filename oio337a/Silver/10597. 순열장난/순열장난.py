# 순열장난

import sys
from collections import deque
input = sys.stdin.readline

def dfs(idx, arr):
  if idx == num_l:
    print(*arr)
    exit()
  num1 = int(num[idx])
  if not visited[num1]:
    visited[num1] = 1
    arr.append(num1)
    dfs(idx + 1, arr)
    visited[num1] = 0
    arr.pop()
  
  if idx + 1 < num_l:
    num2 = int(num[idx:idx+2])
    if num2 <= N and not visited[num2]:
      visited[num2] = 1
      arr.append(num2)
      dfs(idx + 2, arr)
      visited[num2] = 0
      arr.pop()

num = input().rstrip()
num_l = len(num)
N = num_l if num_l < 10 else 9 + (num_l - 9) // 2
visited = [0 for _ in range(N + 1)]

dfs(0, [])

