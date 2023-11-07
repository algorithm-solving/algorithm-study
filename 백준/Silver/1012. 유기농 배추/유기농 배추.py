from sys import stdin

read = stdin.readline

DIRECTIONS = ((-1, 0), (0, -1), (0, 1), (1, 0))


def move(r, c):
    if not field[r][c]:
        return
    field[r][c] = False
    for dr, dc in DIRECTIONS:
        move(r + dr, c + dc)


results = []
T = int(read())
for _ in range(T):
    M, N, K = map(int, read().split())
    field = [[False for _ in range(N + 1)] for _ in range(M + 1)]
    for _ in range(K):
        r, c = map(int, read().split())
        field[r][c] = True
    count = 0
    for r in range(M):
        for c in range(N):
            if field[r][c]:
                move(r, c)
                count += 1
    results.append(count)
print('\n'.join(map(str, results)))
