import sys

input = sys.stdin.readline

# 입력받기
n, m = map(int, input().split())
board = [list(str(input().rstrip())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
queue = [[0, 0]]
board[0][0] = 1
while queue:
    a, b = queue[0][0], queue[0][1]
    del queue[0]
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < n and 0 <= y < m and board[x][y] == "1":
            queue.append([x, y])
            board[x][y] = board[a][b] + 1
print(board[n - 1][m - 1])
