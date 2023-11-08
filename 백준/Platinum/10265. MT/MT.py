from sys import stdin

read = stdin.readline

n, k = map(int, read().split())
heads = [0] + list(map(int, read().split()))
components, cycles = [], []
visited = [False for _ in range(n + 1)]
for vertex in range(1, n + 1):
    if visited[vertex]:
        continue
    path = []
    while not visited[vertex]:
        visited[vertex] = True
        path.append(vertex)
        vertex = heads[vertex]
    for c in components:
        if vertex in c:
            c.extend(path)
            break
    else:
        components.append(path)
        cycles.append(len(path) - path.index(vertex))
counts = [[0 for _ in range(k + 1)] for _ in range(2)]
for i, c in enumerate(components):
    curr, prev = i & 1, i & 1 ^ 1
    min_len, max_len = cycles[i], len(c)
    for j in range(k, -1, -1):
        counts[curr][j] = counts[prev][j]
        for count in range(min_len, min(j, max_len) + 1):
            counts[curr][j] = max(counts[curr][j], counts[prev][j - count] + count)
print(counts[curr][k])
