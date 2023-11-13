# 토마토

import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
  while que:
    y, x = que.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < m and 0 <= ny < n:
        if graph[ny][nx] == 0:
          graph[ny][nx] = graph[y][x] + 1
          que.append((ny, nx))
  res = 0
  for line in graph:
    if 0 in line:
      return -1
    res = max(max(line), res)
  return res - 1

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

que = deque()

for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      que.append((i, j))

print(bfs())