from sys import stdin

read = stdin.readline


def find(v):
    while (parent := parents[v]) != v:
        parents[v] = parents[parent]
        v = parents[v]
    return parent


def union(v1, v2):
    p1, p2 = find(v1), find(v2)
    parents[p2] = p1


N, _ = int(read()), read()
parents = list(range(N))
adj = [tuple(map(int, read().split())) for _ in range(N)]
for c1 in range(1, N):
    for c2 in range(c1):
        if adj[c1][c2] == 1:
            union(c1, c2)
result = 'NO'
cities = map(lambda x: int(x) - 1, read().split())
root = find(next(cities))
for city in cities:
    if find(city) != root:
        break
else:
    result = 'YES'
print(result)
