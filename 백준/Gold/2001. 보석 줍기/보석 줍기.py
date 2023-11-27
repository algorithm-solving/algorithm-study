from collections import deque
from itertools import product
from sys import stdin

read = stdin.readline

N, M, K = map(int, read().split())
vertices = [int(read()) - 1 for _ in range(K)]
indexes = [-1 for _ in range(N)]
for i, v in enumerate(vertices):
    indexes[v] = i
if indexes[0] < 0:
    vertices.append(0)
adj = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, read().split())
    a, b = a - 1, b - 1
    adj[a][b] = c
    adj[b][a] = c
for via, v1, v2 in product(range(N), repeat=3):
    limit = min(adj[v1][via], adj[via][v2])
    adj[v1][v2] = max(limit, adj[v1][v2])
counts = [[-1 for _ in range(1 << K)] for _ in range(N)]
deq = deque([(0, 0, 0)])
while deq:
    v1, vis1, cnt1 = deq.popleft()
    for v2 in vertices:
        if cnt1 > adj[v1][v2]:
            continue
        if counts[v2][vis1] >= 0:
            continue
        counts[v2][vis1] = cnt1
        if (i := indexes[v2]) < 0:
            continue
        deq.append((v2, vis1, cnt1))
        if (vis2 := vis1 | 1 << i) == vis1:
            continue
        cnt2 = cnt1 + 1
        counts[v2][vis2] = cnt2
        deq.append((v2, vis2, cnt2))
print(max(counts[0]))
