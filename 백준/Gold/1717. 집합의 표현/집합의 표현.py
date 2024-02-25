from sys import stdin


def find(v):
    while (parent := parents[v]) != v:
        parents[v] = parents[parent]
        v = parents[v]
    return parent


def union(v1, v2):
    root1, root2 = find(v1), find(v2)
    if root1 != root2:
        parents[root2] = root1


n, _ = map(int, stdin.readline().split())
parents = list(range(n + 1))
results = []
for line in stdin.read().splitlines():
    op, a, b = map(int, line.split())
    if op == 0:
        union(a, b)
    elif op == 1:
        results.append('YES' if find(a) == find(b) else 'NO')
print('\n'.join(results))
