from sys import stdin

N, Q = map(int, stdin.readline().split())
ids = [int(stdin.readline()) - 1 for _ in range(N)]
prefix_sums = [[0, 0, 0]]
for i in ids:
    p = prefix_sums[-1].copy()
    p[i] += 1
    prefix_sums.append(p)
results = []
for line in stdin.read().splitlines():
    a, b = map(int, line.split())
    result = ' '.join(str(p2 - p1) for p1, p2 in zip(prefix_sums[a - 1], prefix_sums[b]))
    results.append(result)
print('\n'.join(results))
