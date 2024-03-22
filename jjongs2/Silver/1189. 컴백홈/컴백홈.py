from sys import stdin

DIRECTIONS = ((-1, 0), (0, -1), (0, 1), (1, 0))


def search(r0, c0, distance):
    if distance == K:
        return 1 if (r0, c0) == (0, C - 1) else 0
    count = 0
    for dr, dc in DIRECTIONS:
        r, c = r0 + dr, c0 + dc
        if 0 <= r < R and 0 <= c < C and grid[r][c] == '.':
            grid[r][c] = 'T'
            count += search(r, c, distance + 1)
            grid[r][c] = '.'
    return count


R, C, K = map(int, stdin.readline().split())
grid = list(map(list, stdin.read().splitlines()))
grid[-1][0] = 'T'
print(search(R - 1, 0, 1))
