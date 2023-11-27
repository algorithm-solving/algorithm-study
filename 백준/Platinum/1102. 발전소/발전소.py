from math import inf
from sys import stdin

read = stdin.readline


def search(count, visited):
    if count >= P:
        return 0
    if (memo := costs[visited]) < inf:
        return memo
    cost = inf
    for i in range(N):
        if visited & 1 << i == 0:
            continue
        for j in range(N):
            if visited & (mask := 1 << j) != 0:
                continue
            cost = min(cost, search(count + 1, visited | mask) + adj[i][j])
    costs[visited] = cost
    return cost


N = int(read())
adj = [tuple(map(int, read().split())) for _ in range(N)]
costs = [inf for _ in range(1 << N)]
init_count, init_visited = 0, 0
for i, char in enumerate(read().strip()):
    if char == 'Y':
        init_visited |= 1 << i
        init_count += 1
P = int(read())
min_cost = search(init_count, init_visited)
print(min_cost if min_cost < inf else -1)
