from collections import deque
from itertools import product
from sys import stdin

read = stdin.readline

DIRECTIONS = ((-1, 0), (0, -1), (0, 1), (1, 0))


def find_farthest(grid, start):
    depth = -1
    visited = [[False for _ in range(C)] for _ in range(R)]
    deq = deque([start])
    while deq:
        for _ in range(len(deq)):
            r0, c0 = deq.popleft()
            visited[r0][c0] = True
            for dr, dc in DIRECTIONS:
                r, c = r0 + dr, c0 + dc
                if not (0 <= r < R and 0 <= c < C):
                    continue
                if visited[r][c]:
                    continue
                if grid[r][c] == '#':
                    continue
                deq.append((r, c))
        depth += 1
    return (r0, c0), depth


results = []
T = int(read())
for _ in range(T):
    C, R = map(int, read().split())
    labyrinth = [read().strip() for _ in range(R)]
    for r, c in product(range(R), range(C)):
        if labyrinth[r][c] == '.':
            root = (r, c)
            break
    leaf, _ = find_farthest(labyrinth, root)
    _, rope_length = find_farthest(labyrinth, leaf)
    results.append(f'Maximum rope length is {rope_length}.')
print('\n'.join(results))
