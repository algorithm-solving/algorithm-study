from sys import stdin

A, Z = ord('a'), ord('z')


def index(c):
    return ord(c) - A


S = stdin.readline().strip()
counts = [[0 for _ in range(A, Z + 1)]]
for letter in S:
    count = counts[-1].copy()
    count[index(letter)] += 1
    counts.append(count)
_ = stdin.readline()
results = []
for line in stdin.read().splitlines():
    letter, left, right = line.split()
    i = index(letter)
    results.append(counts[int(right) + 1][i] - counts[int(left)][i])
print('\n'.join(map(str, results)))
