from collections import deque
from itertools import product
from sys import stdin

DIRECTIONS = ((-1, 0), (0, -1), (0, 1), (1, 0))


def search(grid):
    deq = deque()
    visited = [[-1 for _ in range(M)] for _ in range(N)]
    for r, c in product(range(N), range(M)):
        if grid[r][c] == '0':
            visited[r][c] = 0
            deq.append((r, c, 0))
            break
    count = 0
    while deq:
        count += 1
        for _ in range(len(deq)):
            r0, c0, m0 = deq.popleft()
            for dr, dc in DIRECTIONS:
                r, c = r0 + dr, c0 + dc
                if not (0 <= r < N and 0 <= c < M):
                    continue
                v = visited[r][c]
                if v >= 0 and v & m0 == m0:
                    continue
                obj = grid[r][c]
                if obj == '1':
                    return count
                if obj == '#':
                    continue
                if obj in 'ABCDEF' and m0 & 1 << ord(obj) - ord('A') == 0:
                    continue
                m = m0
                if obj in 'abcdef':
                    m |= 1 << ord(obj) - ord('a')
                visited[r][c] = m
                deq.append((r, c, m))
    return -1


N, M = map(int, stdin.readline().split())
maze = stdin.read().splitlines()
print(search(maze))
