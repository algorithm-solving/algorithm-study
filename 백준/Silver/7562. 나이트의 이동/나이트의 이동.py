from collections import deque
from sys import stdin

read = stdin.readline

DIRECTIONS = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))


def search(size, start, end):
    depth = 0
    r0, c0 = start
    visited = [[False for _ in range(size)] for _ in range(size)]
    visited[r0][c0] = True
    deq = deque([start])
    while deq:
        for _ in range(len(deq)):
            r0, c0 = deq.popleft()
            if (r0, c0) == end:
                return depth
            for dr, dc in DIRECTIONS:
                r, c = r0 + dr, c0 + dc
                if 0 <= r < L and 0 <= c < L and not visited[r][c]:
                    visited[r][c] = True
                    deq.append((r, c))
        depth += 1


results = []
case_count = int(read())
for _ in range(case_count):
    L = int(read())
    S, E = (tuple(map(int, read().split())) for _ in range(2))
    results.append(search(L, S, E))
print('\n'.join(map(str, results)))
