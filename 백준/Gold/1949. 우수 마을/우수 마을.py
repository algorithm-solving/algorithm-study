from sys import stdin

ROOT = 1


def search(adj):
    parents = [-1 for _ in range(N + 1)]
    parents[ROOT] = 0
    visited = []
    stack = [ROOT]
    while stack:
        v0 = stack.pop()
        visited.append(v0)
        for v in adj[v0]:
            if parents[v] > -1:
                continue
            parents[v] = v0
            stack.append(v)
    return parents, visited


def find_total_residents(adj, residents):
    cum_residents = [[0, resident] for resident in residents]
    parents, visited = search(adj)
    while visited:
        child = visited.pop()
        parent = parents[child]
        cum_residents[parent][0] += max(cum_residents[child])
        cum_residents[parent][1] += cum_residents[child][0]
    return max(cum_residents[ROOT])


N = int(stdin.readline())
residents = [0, *map(int, stdin.readline().split())]
adj = [[] for _ in range(N + 1)]
for line in stdin.read().splitlines():
    v1, v2 = map(int, line.split())
    adj[v1].append(v2)
    adj[v2].append(v1)
print(find_total_residents(adj, residents))
