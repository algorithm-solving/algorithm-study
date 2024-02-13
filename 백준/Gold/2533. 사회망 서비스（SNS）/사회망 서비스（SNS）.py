from array import array
from sys import stdin

ROOT = 1


def search(adj):
    parents = array('i', [-1 for _ in range(N + 1)])
    parents[ROOT] = 0
    visited = array('I')
    stack = array('I', [ROOT])
    while stack:
        v0 = stack.pop()
        visited.append(v0)
        for v in adj[v0]:
            if parents[v] > -1:
                continue
            parents[v] = v0
            stack.append(v)
    return parents, visited


def find_min_count(adj):
    cumulative_sums = [array('I', [0, 1]) for _ in range(N + 1)]
    parents, visited = search(adj)
    while visited:
        child = visited.pop()
        parent = parents[child]
        cumulative_sums[parent][0] += cumulative_sums[child][1]
        cumulative_sums[parent][1] += min(cumulative_sums[child])
    return min(cumulative_sums[ROOT])


N = int(stdin.readline())
adj = [[] for _ in range(N + 1)]
for line in stdin.read().splitlines():
    u, v = map(int, line.split())
    adj[u].append(v)
    adj[v].append(u)
print(find_min_count(adj))
