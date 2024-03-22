# 음식물 피하기

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m, k = map(int, input().split())
board = [[0] * m for _ in range(n)]

for _ in range(k):
  x, y = map(int, input().split())
  board[x - 1][y - 1] = 1

visit = [[False] * m for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
res = 0

def dfs(x, y):
  global cnt
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < m:
      if board[nx][ny] == 1 and not visit[nx][ny]:
        visit[nx][ny] = True
        cnt += 1
        dfs(nx, ny)

for i in range(n):
  for j in range(m):
    if board[i][j] == 1 and not visit[i][j]:
      cnt = 0
      dfs(i, j)
      res = max(res, cnt)

print(res)