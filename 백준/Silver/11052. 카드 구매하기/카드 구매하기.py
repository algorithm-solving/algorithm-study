from sys import stdin

read = stdin.readline

N = int(read())
costs = [0] + list(map(int, read().split()))
for i in range(2, N + 1):
    for j in range(1, i):
        costs[i] = max(costs[i], costs[i - j] + costs[j])
print(costs[N])
