from sys import stdin

ROOT = 1


def find_farthest(start):
    vertex, distance = 0, 0
    visited = [False for _ in range(n + 1)]
    stack = [(start, 0)]
    while stack:
        v0, w0 = stack.pop()
        visited[v0] = True
        for v, dw in adj[v0]:
            if visited[v]:
                continue
            if (w := w0 + dw) > distance:
                vertex, distance = v, w
            stack.append((v, w))
    return vertex, distance


n = int(stdin.readline())
adj = [[] for _ in range(n + 1)]
for line in stdin.read().splitlines():
    v1, v2, weight = map(int, line.split())
    adj[v1].append((v2, weight))
    adj[v2].append((v1, weight))
farthest_v = find_farthest(ROOT)[0]
print(find_farthest(farthest_v)[1])
