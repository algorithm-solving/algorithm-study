from sys import stdin

N, M = map(int, stdin.readline().split())
nums = tuple(map(int, stdin.readline().split()))
prefix_sums = [0]
for num in nums:
    prefix_sums.append(prefix_sums[-1] + num)
results = []
for line in stdin.read().splitlines():
    i, j = map(int, line.split())
    results.append(prefix_sums[j] - prefix_sums[i - 1])
print('\n'.join(map(str, results)))
