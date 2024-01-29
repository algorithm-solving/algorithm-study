from sys import stdin

read = stdin.readline

_, M = map(int, read().split())
counts = [0 for _ in range(M)]
counts[0] = 1
result = 0
prefix_sum = 0
for num in map(int, read().split()):
    prefix_sum = (prefix_sum + num) % M
    result += counts[prefix_sum]
    counts[prefix_sum] += 1
print(result)
