# 유기농 배추
# https://www.acmicpc.net/problem/1012

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
T = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    que = [[x, y]]
    while que:
        a, b = que[0][0], que[0][1]
        del que[0]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m and s[nx][ny] == 1:
                s[nx][ny] = 0
                que.append([nx, ny])
for _ in range(T):
    m, n, k = map(int, input().split())
    s = [[0] * m for _ in range(n)]
    cnt = 0
    for _ in range(k):
        x, y = map(int, input().split())
        s[y][x] = 1
    for i in range(n):
        for j in range(m):
            if s[i][j] == 1:
                bfs(i, j)
                s[i][j] = 0
                cnt += 1
    print(cnt)

''' dfs '''

# T = int(input())

# def dfs(x, y, n, m):
#   if x >= 0 and x < n and y >= 0 and y < m:
#     if board[x][y] == 1:
#       board[x][y] = 0
#       dfs(x + 1, y, n, m)
#       dfs(x, y + 1, n, m)
#       dfs(x - 1, y, n, m)
#       dfs(x, y - 1, n, m)

# for _ in range(T):
#   m, n, k = map(int, input().split())
#   board = [[0] * m for _ in range(n)]
#   cnt = 0
#   for _ in range(k):
#     x, y = map(int, input().split())
#     board[y][x] = 1
#   for i in range(n):
#     for j in range(m):
#       if board[i][j] == 1:
#         board[i][j] = 0
#         dfs(i + 1, j, n, m)
#         dfs(i, j + 1, n, m)
#         dfs(i - 1, j, n, m)
#         dfs(i, j - 1, n, m)
#         cnt += 1
#   print(cnt)
