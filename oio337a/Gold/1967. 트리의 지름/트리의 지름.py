from collections import deque
import sys

input = sys.stdin.readline

def bfs(x, mode):
    q = deque()
    q.append(x)
    c = [-1 for _ in range(n)]
    c[x] = 0
    while q:
        x = q.popleft()
        for w, nx in a[x]:
            if c[nx] == -1:
                c[nx] = c[x] + w
                q.append(nx)
    if mode == 1:
        return c.index(max(c))
    else:
        return max(c)

n = int(input())
a = [[] for _ in range(n)]

for i in range(n-1):
    x, y, w = map(int, input().split())
    a[x-1].append([w, y-1])
    a[y-1].append([w, x-1])
print(bfs(bfs(0, 1), 2))