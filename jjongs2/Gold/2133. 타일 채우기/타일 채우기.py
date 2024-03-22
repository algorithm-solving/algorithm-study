from sys import stdin


def count(width):
    if width & 1 == 1:
        return 0
    w = width // 2
    counts = [1] + [0 for _ in range(w)]
    for i in range(1, w + 1):
        counts[i] = 3 * counts[i - 1] + 2 * sum(counts[:i - 1])
    return counts[-1]


N = int(stdin.read())
print(count(N))
