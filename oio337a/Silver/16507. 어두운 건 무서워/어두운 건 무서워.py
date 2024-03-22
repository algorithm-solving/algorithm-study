# 어두운 건 무서워

import sys
input = sys.stdin.readline

r, c, q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]

prefix = [[0] * (c+1) for _ in range(r + 1)]

for i in range(r):
    for j in range(c):
        prefix[i + 1][j + 1] = (prefix[i][j + 1] +
                                prefix[i + 1][j] - prefix[i][j]) + board[i][j]

for i in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    ans = prefix[r2][c2] - prefix[r1 - 1][c2] - prefix[r2][c1 - 1] + prefix[r1 - 1][c1 - 1]
    num = (r2 - r1 + 1) * (c2 - c1 + 1)
    print(ans // num)