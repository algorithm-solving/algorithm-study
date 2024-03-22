from sys import stdin

read = stdin.readline

DIRECTIONS = ((0, 0), (0, 1), (1, 0), (1, 1))


def compress(r, c, size):
    if size == 1:
        return image[r][c]
    new_size = size >> 1
    quadrants = [compress(r + dr * new_size, c + dc * new_size, new_size) for dr, dc in DIRECTIONS]
    pivot = quadrants[0]
    if len(pivot) == 1 and all(q == pivot for q in quadrants):
        return pivot
    return f'({"".join(quadrants)})'


N = int(read())
image = [read().strip() for _ in range(N)]
print(compress(0, 0, N))
