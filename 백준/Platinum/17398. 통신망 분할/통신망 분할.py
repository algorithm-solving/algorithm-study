from sys import stdin

read = stdin.readline


def find(v):
    while (parent := parents[v]) != v:
        parents[v] = parents[parent]
        v = parents[v]
    return v


def union(v1, v2):
    root1, root2 = find(v1), find(v2)
    if root1 == root2:
        return 0
    parents[root2] = root1
    cost = sizes[root1] * sizes[root2]
    sizes[root1] += sizes[root2]
    return cost


N, M, Q = map(int, read().split())
parents = list(range(N + 1))
sizes = [1 for _ in range(N + 1)]
initial_connections = [tuple(map(int, read().split())) for _ in range(M)]
removals = [int(read()) - 1 for _ in range(Q)]
remaining_connections = set(range(M)) - set(removals)
for i in remaining_connections:
    X, Y = initial_connections[i]
    union(X, Y)
total_cost = 0
for A in reversed(removals):
    X, Y = initial_connections[A]
    total_cost += union(X, Y)
print(total_cost)
