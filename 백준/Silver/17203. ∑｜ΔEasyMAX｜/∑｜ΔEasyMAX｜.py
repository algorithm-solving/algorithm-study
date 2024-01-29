from sys import stdin

N, Q = map(int, stdin.readline().split())
A = tuple(map(int, stdin.readline().split()))
prefix_sums = [0, 0]
for i in range(1, N):
    delta = abs(A[i] - A[i - 1])
    prefix_sums.append(prefix_sums[i] + delta)
results = []
for line in stdin.read().splitlines():
    i, j = map(int, line.split())
    results.append(prefix_sums[j] - prefix_sums[i])
print('\n'.join(map(str, results)))
