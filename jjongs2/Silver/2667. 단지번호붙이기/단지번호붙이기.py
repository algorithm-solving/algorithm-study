from sys import stdin

DIRECTIONS = ((-1, 0), (0, -1), (0, 1), (1, 0))


def search(init_r, init_c):
    count = 0
    stack = [(init_r, init_c)]
    while stack:
        r, c = stack.pop()
        if not (0 <= r < N and 0 <= c < N):
            continue
        if grid[r][c] == '0':
            continue
        grid[r][c] = '0'
        count += 1
        stack.extend((r + dr, c + dc) for dr, dc in DIRECTIONS)
    return count


N = int(stdin.readline())
grid = list(map(list, stdin.read().splitlines()))
counts = [search(r, c) for r in range(N) for c in range(N) if grid[r][c] == '1']
results = [len(counts)] + sorted(counts)
print('\n'.join(map(str, results)))
