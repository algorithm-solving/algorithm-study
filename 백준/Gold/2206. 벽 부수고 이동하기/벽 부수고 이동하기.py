from collections import deque
from sys import stdin

DIRECTIONS = ((-1, 0), (0, -1), (0, 1), (1, 0))
F = 2


def search(grid):
    depth = 0
    visited = [[F for _ in range(C)] for _ in range(R)]
    visited[0][0] = 0
    deq = deque([(0, 0, 0)])
    while deq:
        depth += 1
        for _ in range(len(deq)):
            r0, c0, f0 = deq.popleft()
            if (r0, c0) == (R - 1, C - 1):
                return depth
            for dr, dc in DIRECTIONS:
                r, c = r0 + dr, c0 + dc
                if not (0 <= r < R and 0 <= c < C):
                    continue
                f = f0 if grid[r][c] == '0' else f0 + 1
                if f < visited[r][c]:
                    visited[r][c] = f
                    deq.append((r, c, f))
    return -1


R, C = map(int, stdin.readline().split())
grid = stdin.read().splitlines()
print(search(grid))
