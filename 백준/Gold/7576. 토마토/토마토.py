from collections import deque
from itertools import product
from sys import stdin

read = stdin.readline

DIRECTIONS = ((-1, 0), (0, -1), (0, 1), (1, 0))

M, N = map(int, read().split())
grid = [list(map(int, read().split())) for _ in range(N)]
deq = deque()
count = 0
for r, c in product(range(N), range(M)):
    match grid[r][c]:
        case 0:
            count += 1
        case 1:
            deq.append((r, c))
depth = -1
while deq:
    depth += 1
    for _ in range(len(deq)):
        r0, c0 = deq.popleft()
        for dr, dc in DIRECTIONS:
            r, c = r0 + dr, c0 + dc
            if 0 <= r < N and 0 <= c < M and grid[r][c] == 0:
                count -= 1
                grid[r][c] = 1
                deq.append((r, c))
print(depth if count == 0 else -1)
