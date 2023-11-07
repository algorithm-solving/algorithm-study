from sys import stdin

read = stdin.readline

DIRECTIONS = ((-1, 0), (0, -1), (0, 1), (1, 0))


def search(init_r, init_c):
    size = 0
    stack = [(init_r, init_c)]
    while stack:
        r, c = stack.pop()
        if not (0 <= r < N and 0 <= c < M):
            continue
        if not grid[r][c]:
            continue
        size += 1
        grid[r][c] = False
        for dr, dc in DIRECTIONS:
            stack.append((r + dr, c + dc))
    return size


N, M, K = map(int, read().split())
grid = [[False for _ in range(M)] for _ in range(N)]
for _ in range(K):
    r, c = map(int, read().split())
    grid[r - 1][c - 1] = True
max_size = 0
for r in range(N):
    for c in range(M):
        if grid[r][c]:
            max_size = max(max_size, search(r, c))
print(max_size)
