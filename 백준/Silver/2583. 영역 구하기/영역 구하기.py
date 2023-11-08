from itertools import product
from sys import stdin

DIRECTIONS = ((-1, 0), (0, -1), (0, 1), (1, 0))


def find_area(init_r, init_c):
    area = 0
    stack = [(init_r, init_c)]
    while stack:
        r, c = stack.pop()
        if 0 <= r < N and 0 <= c < M and grid[r][c]:
            grid[r][c] = False
            area += 1
            stack.extend((r + dr, c + dc) for dr, dc in DIRECTIONS)
    return area


M, N, K = map(int, stdin.readline().split())
grid = [[True for _ in range(M)] for _ in range(N)]
for line in stdin.read().splitlines():
    r1, c1, r2, c2 = map(int, line.split())
    for r, c in product(range(r1, r2), range(c1, c2)):
        grid[r][c] = False
areas = sorted(find_area(r, c) for r, c in product(range(N), range(M)) if grid[r][c])
print(len(areas))
print(' '.join(map(str, areas)))
