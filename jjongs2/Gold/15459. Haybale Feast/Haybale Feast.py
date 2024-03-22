from sys import stdin

DELTAS = (-1, 1)


def find(v):
    while (parent := parents[v]) != v:
        parents[v] = parents[parent]
        v = parents[v]
    return v


def union(v1, v2):
    root1, root2 = find(v1), find(v2)
    if root1 != root2:
        parents[root2] = root1
        haybales[root1][1] += haybales[root2][1]
    return haybales[root1][1]


def find_min_spiciness(threshold):
    for v0, F, S in sorted(haybales, key=lambda x: x[2]):
        if F >= threshold:
            return S
        for dv in DELTAS:
            v = v0 + dv
            if not (0 <= v < N):
                continue
            if haybales[v][2] > S:
                continue
            if union(v0, v) >= threshold:
                return S


N, M = map(int, stdin.readline().split())
parents = list(range(N))
haybales = [[i, *map(int, line.split())] for i, line in enumerate(stdin.read().splitlines())]
print(find_min_spiciness(M))
