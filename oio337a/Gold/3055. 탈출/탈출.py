# 탈출

import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs():
  while que:
    y, x = que.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < c and 0 <= ny < r:
        if visit[ny][nx] == -1 and (graph[ny][nx] == '.' or graph[ny][nx] == 'S'):
          if graph[y][x] == '*':
            visit[ny][nx] = 'submerge'
            graph[ny][nx] = '*'
          else:
            visit[ny][nx] = visit[y][x] + 1
            graph[ny][nx] = 'S'
          que.append((ny, nx))
        elif graph[ny][nx] == 'D' and graph[y][x] == 'S':
          return visit[y][x] + 1
  return 'KAKTUS'

r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
que = deque()
visit = [[-1]*c for _ in range(r)]

for i in range(r):
  for j in range(c):
    if graph[i][j] == '*':
      que.append((i, j))
      visit[i][j] = 'submerge'
    elif graph[i][j] == 'S':
      start = (i, j)
      visit[i][j] = 0

que.append(start)
print(bfs())