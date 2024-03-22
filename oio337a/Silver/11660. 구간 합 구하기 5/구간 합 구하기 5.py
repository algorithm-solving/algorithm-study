import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

frefix = [[0] * (n+1) for _ in range(n + 1)]

for i in range(n):
    for j in range(n):
        frefix[i + 1][j + 1] = (frefix[i][j + 1] +
                                frefix[i + 1][j] - frefix[i][j]) + board[i][j]
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(frefix[x2][y2] - (frefix[x1 - 1][y2] +
          frefix[x2][y1 - 1] - frefix[x1 - 1][y1 - 1]))
