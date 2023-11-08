from itertools import product
from sys import stdin

DIRECTIONS = ((-1, 0), (0, -1), (0, 1), (1, 0))


def search(r0, c0, color):
    stack = [(r0, c0)]
    while stack:
        r, c = stack.pop()
        if 0 <= r < N and 0 <= c < N and grid[r][c] == color:
            grid[r][c] = 'Y' if color in 'RG' else ''
            stack.extend((r + dr, c + dc) for dr, dc in DIRECTIONS)


N = int(stdin.readline())
grid = list(map(list, stdin.read().splitlines()))
counts = dict.fromkeys('RGBY', 0)
for colors in ('RGB', 'Y'):
    color_set = set(colors)
    for r, c in product(range(N), repeat=2):
        color = grid[r][c]
        if color in color_set:
            search(r, c, color)
            counts[color] += 1
print(counts['R'] + counts['G'] + counts['B'], counts['Y'] + counts['B'])
