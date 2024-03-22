# # 단지 번호 붙이기
# # https://www.acmicpc.net/problem/2667

import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(board, a, b):
    n = len(board)
    queue = deque()
    queue.append((a, b))
    board[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] == 1:
                board[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count


n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, input().rstrip())))

cnt = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            cnt.append(bfs(board, i, j))

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])
