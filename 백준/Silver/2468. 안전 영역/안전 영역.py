from sys import stdin

read = stdin.readline

DIRECTIONS = ((-1, 0), (0, -1), (0, 1), (1, 0))


def search(r0, c0, h):
    visited[r0][c0] = True
    stack = [(r0, c0)]
    while stack:
        r1, c1 = stack.pop()
        for dr, dc in DIRECTIONS:
            r2, c2 = r1 + dr, c1 + dc
            if 0 <= r2 < N and 0 <= c2 < N and heights[r2][c2] > h and not visited[r2][c2]:
                visited[r2][c2] = True
                stack.append((r2, c2))


max_count = 1
N = int(read())
heights = [tuple(map(int, read().split())) for _ in range(N)]
min_h, max_h = (func(map(func, heights)) for func in (min, max))
for h in range(min_h, max_h):
    count = 0
    visited = [[False for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if heights[r][c] > h and not visited[r][c]:
                search(r, c, h)
                count += 1
    max_count = max(max_count, count)
print(max_count)
