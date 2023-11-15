from sys import stdin


def count(start, end):
    if start >= end:
        return start - end
    if start == 0:
        return 1 + count(1, end)
    if end & 1 == 0:
        return min(end - start, 1 + count(start, end // 2))
    return 1 + min(count(start, end - 1), count(start, end + 1))


N, K = map(int, stdin.read().split())
print(count(N, K))
