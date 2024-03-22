# 영역 구하기

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

m, n, k = map(int, input().split())
point_list = [list(map(int, input().split())) for _ in range(k)]

board = [[0] * n for _ in range(m)]
visit = [[False] * n for _ in range(m)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
answer = []

for a1, a2, b1, b2 in point_list:
  for i in range(a2, b2):
    for j in range(a1, b1):
      board[i][j] = 1

def dfs(x, y):
  global cnt
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < m and 0 <= ny < n:
      if board[nx][ny] == 0 and not visit[nx][ny]:
        visit[nx][ny] = True
        cnt += 1
        dfs(nx, ny)

for i in range(m):
  for j in range(n):
    if board[i][j] == 0 and not visit[i][j]:
      cnt = 0
      dfs(i, j)
      answer.append(cnt + 1 if cnt == 0 else cnt)

print(len(answer))
answer.sort()
print(*answer)