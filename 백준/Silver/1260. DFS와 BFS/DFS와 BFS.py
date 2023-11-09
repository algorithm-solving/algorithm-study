from collections import deque
from sys import stdin

N, M, V = map(int, stdin.readline().split())
adj = [[] for _ in range(N + 1)]
for line in stdin.read().splitlines():
    v1, v2 = map(int, line.split())
    adj[v1].append(v2)
    adj[v2].append(v1)
for a in adj:
    a.sort()
results = [[], []]
for i in range(2):
    visited = [False for _ in range(N + 1)]
    deq = deque([V])
    while deq:
        vertex = deq.pop() if i == 0 else deq.popleft()
        if visited[vertex]:
            continue
        visited[vertex] = True
        results[i].append(vertex)
        deq.extend(reversed(adj[vertex]) if i == 0 else adj[vertex])
print('\n'.join(' '.join(map(str, result)) for result in results))
