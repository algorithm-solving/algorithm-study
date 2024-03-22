from sys import stdin

read = stdin.readline


def find(v):
    while (parent := parents[v]) != v:
        parents[v] = parents[parent]
        v = parents[v]
    return parent


def union(v1, v2):
    p1, p2 = find(v1), find(v2)
    if p1 != p2:
        parents[p2] = p1
        sizes[p1] += sizes[p2]
    return sizes[p1]


results = []
case_count = int(read())
for _ in range(case_count):
    parents, sizes = dict(), dict()
    F = int(read())
    for _ in range(F):
        id1, id2 = read().split()
        for user_id in id1, id2:
            parents.setdefault(user_id, user_id)
            sizes.setdefault(user_id, 1)
        results.append(union(id1, id2))
print('\n'.join(map(str, results)))
