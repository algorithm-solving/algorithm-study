from sys import stdin

MAX_LENGTH = 20

result = 0
counts = [0 for _ in range(MAX_LENGTH + 1)]
N, K = map(int, stdin.readline().split())
lengths = [0 for _ in range(N)]
names = stdin.read().splitlines()
for index, name in enumerate(names):
    length = len(name)
    lengths[index] = length
    if index > K:
        counts[lengths[index - K - 1]] -= 1
    result += counts[length]
    counts[length] += 1
print(result)
