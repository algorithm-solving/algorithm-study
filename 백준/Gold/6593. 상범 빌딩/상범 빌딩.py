from collections import deque
from itertools import product
from sys import stdin

read = stdin.readline

DIRECTIONS = ((-1, 0, 0), (0, -1, 0), (0, 0, -1), (0, 0, 1), (0, 1, 0), (1, 0, 0))


def search(grids):
    depth = 0
    deq = deque()
    visited = [[[False for _ in range(C)] for _ in range(R)] for _ in range(F)]
    for f, r, c in product(range(F), range(R), range(C)):
        if grids[f][r][c] == 'S':
            visited[f][r][c] = True
            deq.append((f, r, c))
            break
    while deq:
        depth += 1
        for _ in range(len(deq)):
            f0, r0, c0 = deq.popleft()
            for df, dr, dc in DIRECTIONS:
                f, r, c = f0 + df, r0 + dr, c0 + dc
                if 0 <= f < F and 0 <= r < R and 0 <= c < C and not visited[f][r][c]:
                    if grids[f][r][c] == 'E':
                        return depth
                    if grids[f][r][c] == '.':
                        visited[f][r][c] = True
                        deq.append((f, r, c))
    return -1


results = []
while True:
    F, R, C = map(int, read().split())
    if F == 0:
        break
    floors = [[read().strip() for _ in range(R + 1)] for _ in range(F)]
    time = search(floors)
    results.append(f'Escaped in {time} minute(s).' if time > 0 else 'Trapped!')
print('\n'.join(results))
