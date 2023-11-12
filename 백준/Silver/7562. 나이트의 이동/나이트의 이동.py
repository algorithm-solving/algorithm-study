# 나이트의 이동
# https://www.acmicpc.net/problem/7562

import sys
from collections import deque
input = sys.stdin.readline

dx = [2, 2, -2, -2, -1, -1, 1, 1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

def bfs(sx, sy, ax, ay):
    q = deque()
    q.append([sx, sy])
    s[sx][sy] = 1
    while q:
        a, b = q.popleft()
        if a == ax and b == ay:
            print(s[ax][ay] -1)
            return
        for i in range(8):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < n and s[x][y] == 0:
                q.append([x, y])
                s[x][y] = s[a][b] + 1

t = int(input())
for _ in range(t):
    n = int(input())
    sx, sy = map(int, input().split())
    ax, ay = map(int, input().split())
    s = [[0] * n for _ in range(n)]
    bfs(sx, sy, ax, ay)
