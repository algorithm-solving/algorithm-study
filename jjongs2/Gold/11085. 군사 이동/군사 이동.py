from sys import stdin


def find(x):
    while (parent := parents[x]) != x:
        parents[x] = parents[parent]
        x = parents[x]
    return x


def union(x1, x2):
    parents[find(x2)] = find(x1)


p, _ = map(int, stdin.readline().split())
parents = list(range(p))
c, v = map(int, stdin.readline().split())
roads = [tuple(map(int, line.split())) for line in stdin.read().splitlines()]
for start, end, width in sorted(roads, key=lambda x: -x[2]):
    union(start, end)
    if find(c) == find(v):
        print(width)
        break
