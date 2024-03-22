from itertools import product
from sys import stdin

R, C, _ = map(int, stdin.readline().split())
grid = [[0 for _ in range(C + 1)]] + [[0, *map(int, stdin.readline().split())] for _ in range(R)]
for r, c in product(range(1, R + 1), range(1, C + 1)):
    grid[r][c] += grid[r][c - 1] + grid[r - 1][c] - grid[r - 1][c - 1]
results = []
for line in stdin.read().splitlines():
    r1, c1, r2, c2 = map(int, line.split())
    r1, c1 = r1 - 1, c1 - 1
    area = (r2 - r1) * (c2 - c1)
    prefix_sum = grid[r2][c2] - grid[r2][c1] - grid[r1][c2] + grid[r1][c1]
    results.append(prefix_sum // area)
print('\n'.join(map(str, results)))
