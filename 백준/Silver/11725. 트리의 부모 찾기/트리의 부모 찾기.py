from sys import stdin

ROOT = 1


def find_parents(root):
    parents = [0 for _ in range(N + 1)]
    parents[root] = root
    stack = [root]
    while stack:
        v0 = stack.pop()
        for v in adj[v0]:
            if parents[v] > 0:
                continue
            parents[v] = v0
            stack.append(v)
    return parents[2:]


N = int(stdin.readline())
adj = [[] for _ in range(N + 1)]
for line in stdin.read().splitlines():
    v1, v2 = map(int, line.split())
    adj[v1].append(v2)
    adj[v2].append(v1)
result = find_parents(ROOT)
print('\n'.join(map(str, result)))
