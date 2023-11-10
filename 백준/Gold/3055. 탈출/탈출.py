from collections import deque
from itertools import product
from math import inf
from sys import stdin

DIRECTIONS = ((-1, 0), (0, -1), (0, 1), (1, 0))


def search(grid):
    deq = deque()
    visited = [[False for _ in range(C)] for _ in range(R)]
    for r, c in product(range(R), range(C)):
        match grid[r][c]:
            case '*':
                deq.append((r, c, -inf))
            case 'S':
                start = (r, c, 0)
            case _:
                continue
        visited[r][c] = True
    deq.append(start)
    while deq:
        r0, c0, d0 = deq.popleft()
        for dr, dc in DIRECTIONS:
            r, c, d = r0 + dr, c0 + dc, d0 + 1
            if not (0 <= r < R and 0 <= c < C):
                continue
            if grid[r][c] == 'D' and d > 0:
                return d
            if grid[r][c] == '.' and not visited[r][c]:
                visited[r][c] = True
                deq.append((r, c, d))
    return -1


R, C = map(int, stdin.readline().split())
forest = stdin.read().splitlines()
time = search(forest)
print(time if time > 0 else 'KAKTUS')
