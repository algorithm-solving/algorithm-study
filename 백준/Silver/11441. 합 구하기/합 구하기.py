from sys import stdin

N = int(stdin.readline())
A = tuple(map(int, stdin.readline().split()))
M = int(stdin.readline())
prefix_sums = [0]
for num in A:
    prefix_sums.append(prefix_sums[-1] + num)
results = []
for line in stdin.read().splitlines():
    i, j = map(int, line.split())
    results.append(prefix_sums[j] - prefix_sums[i - 1])
print('\n'.join(map(str, results)))
