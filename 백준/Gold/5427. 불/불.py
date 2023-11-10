from collections import deque
from itertools import product
from math import inf
from sys import stdin

read = stdin.readline

DIRECTIONS = ((-1, 0), (0, -1), (0, 1), (1, 0))


def search(grid):
    deq = deque()
    visited = [[False for _ in range(W)] for _ in range(H)]
    for h, w in product(range(H), range(W)):
        match grid[h][w]:
            case '@':
                start = (h, w, 0)
            case '*':
                deq.append((h, w, -inf))
            case _:
                continue
        visited[h][w] = True
    deq.append(start)
    while deq:
        h0, w0, d0 = deq.popleft()
        for dh, dw in DIRECTIONS:
            h, w, d = h0 + dh, w0 + dw, d0 + 1
            if 0 <= h < H and 0 <= w < W:
                if grid[h][w] == '.' and not visited[h][w]:
                    visited[h][w] = True
                    deq.append((h, w, d))
            elif d > 0:
                return d
    return -1


results = []
case_count = int(read())
for _ in range(case_count):
    W, H = map(int, read().split())
    floors = [read().strip() for _ in range(H)]
    time = search(floors)
    results.append(str(time) if time > 0 else 'IMPOSSIBLE')
print('\n'.join(results))
