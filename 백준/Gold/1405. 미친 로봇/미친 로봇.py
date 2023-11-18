from sys import stdin


def move(r0, c0, count):
    if count == 0:
        return 1
    prob = 0
    for i, p in enumerate(P):
        if p == 0:
            continue
        r, c = r0 + dr[i], c0 + dc[i]
        if visited[r][c]:
            continue
        visited[r][c] = True
        prob += move(r, c, count - 1) * p
        visited[r][c] = False
    return prob


N, *P = map(int, stdin.read().split())
P = tuple(pct / 100 for pct in P)
dr, dc = (1, -1, 0, 0), (0, 0, 1, -1)
size = N * 2 + 1
visited = [[False for _ in range(size)] for _ in range(size)]
visited[N][N] = True
print(move(N, N, N))
