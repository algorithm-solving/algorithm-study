from sys import stdin


def find(v):
    while (parent := parents[v]) != v:
        parents[v] = parents[parent]
        v = parents[v]
    return v


def union(v1, v2):
    parents[find(v2)] = parents[find(v1)]


G = int(stdin.readline())
parents = list(range(G + 1))
result = int(stdin.readline())
planes = map(int, stdin.read().splitlines())
for i, g in enumerate(planes):
    root = find(g)
    if root == 0:
        result = i
        break
    union(root - 1, root)
print(result)
