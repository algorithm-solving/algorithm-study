from collections import deque
from sys import stdin

DIRECTIONS = ((-1, 0), (0, -1), (0, 1), (1, 0))


def search(start, end):
    depth = 1
    r0, c0 = start
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[r0][c0] = True
    deq = deque([start])
    while True:
        depth += 1
        for _ in range(len(deq)):
            r0, c0 = deq.popleft()
            for dr, dc in DIRECTIONS:
                r, c = r0 + dr, c0 + dc
                if 0 <= r < N and 0 <= c < M and maze[r][c] == '1' and not visited[r][c]:
                    if (r, c) == end:
                        return depth
                    visited[r][c] = True
                    deq.append((r, c))


N, M = map(int, stdin.readline().split())
maze = stdin.read().splitlines()
print(search((0, 0), (N - 1, M - 1)))
