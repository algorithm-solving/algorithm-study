from sys import stdin

INF = 16_000_000


def search(curr_v, visited):
    if (ret := costs[curr_v][visited]) > 0:
        return ret
    cost_sum = INF
    for next_v, cost in enumerate(W[curr_v]):
        mask = 1 << next_v
        if visited & mask == 0:
            cost_sum = min(cost_sum, search(next_v, visited | mask) + cost)
    costs[curr_v][visited] = cost_sum
    return cost_sum


N = int(stdin.readline())
W = [[INF if cost == '0' else int(cost) for cost in line.split()] for line in stdin.read().splitlines()]
costs = [[0 for _ in range(1 << N)] for _ in range(N)]
for v in range(1, N):
    costs[v][-1] = W[v][0]
print(search(0, 1))
