from sys import stdin


def find(v):
    while (parent := parents[v]) != v:
        parents[v] = parents[parent]
        v = parents[v]
    return v


def union(v1, v2):
    parents[find(v2)] = find(v1)


_, L = map(int, stdin.readline().split())
drawers = [False for _ in range(L + 1)]
parents = list(range(L + 1))
results = []
for line in stdin.read().splitlines():
    A, B = map(lambda x: find(int(x)), line.split())
    if drawers[A] and drawers[B]:
        results.append('SMECE')
        continue
    if drawers[A]:
        drawers[B] = True
    else:
        drawers[A] = True
    union(B, A)
    results.append('LADICA')
print('\n'.join(results))
