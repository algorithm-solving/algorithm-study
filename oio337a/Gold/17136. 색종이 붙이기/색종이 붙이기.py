# 색종이 붙이기

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

board = [list(map(int, input().split())) for _ in range(10)]
color = [5 for _ in range(5)]
total = 25

def check(y, x, offset):
    for i in range(y, y+offset + 1):
        for j in range(x, x+offset + 1):
            if board[i][j] != 1: return False
    return True

def backtrack(y, x, c):
    global total
    if y >= 10:
        total = min(total, c)
        return
    if x >= 10:
        backtrack(y + 1, 0, c)
        return
    if board[y][x] == 1:
        for k in range(5):
            if color[k] == 0: continue
            if y + k >= 10 or x + k >= 10: continue

            if not check(y, x, k): break
            for i in range(y, y + k + 1):
                for j in range(x, x + k + 1):
                    board[i][j] = 0
            color[k] -= 1
            backtrack(y, x+k+1, c + 1)
            color[k] += 1
            for i in range(y, y + k + 1):
                for j in range(x, x + k + 1):
                    board[i][j] = 1
    else: backtrack(y, x + 1, c)

backtrack(0, 0, 0)
print(-1 if total == 25 else total)
