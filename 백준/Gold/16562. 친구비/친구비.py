from sys import stdin


def find(v):
    while (parent := parents[v]) != v:
        parents[v] = parents[parent]
        v = parents[v]
    return parent


def union(v1, v2):
    p1, p2 = find(v1), find(v2)
    parents[p2] = p1
    A[p1] = min(A[p1], A[p2])


N, M, k = map(int, stdin.readline().split())
parents = list(range(N))
A = list(map(int, stdin.readline().split()))
for line in stdin.read().splitlines():
    v, w = map(lambda x: int(x) - 1, line.split())
    union(v, w)
result = 'Oh no'
cost = 0
roots = set(map(find, range(N)))
for root in roots:
    cost += A[root]
    if cost > k:
        break
else:
    result = cost
print(result)
