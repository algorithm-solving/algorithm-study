# 적록색약

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
board = [list(input().rstrip()) for _ in range(n)]
visit = [[False] * n for _ in range(n)]
answer = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, target):
  global cnt
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < n:
      if board[nx][ny] == target and not visit[nx][ny]:
        visit[nx][ny] = True
        dfs(nx, ny, target)

cnt = 0
for i in range(n):
  for j in range(n):
    if not visit[i][j]:
      cnt += 1
      dfs(i, j, board[i][j])

answer.append(cnt)

visit = [[False] * n for _ in range(n)]
cnt = 0

for i in range(n):
  for j in range(n):
    if board[i][j] == 'R':
      board[i][j] = 'G'

for i in range(n):
  for j in range(n):
    if not visit[i][j]:
      cnt += 1
      dfs(i, j, board[i][j])

answer.append(cnt)
print(*answer)