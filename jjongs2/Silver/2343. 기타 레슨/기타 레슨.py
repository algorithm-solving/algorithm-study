from sys import stdin

read = stdin.readline


def min_bd_size(bd_count, durations):
    low, high = max(durations), sum(durations)
    if bd_count >= high / low:
        return low
    while high - low > 1:
        mid = (low + high) // 2
        count = 1
        size = 0
        for d in durations:
            size += d
            if size > mid:
                count += 1
                size = d
        if count > M:
            low = mid
        else:
            high = mid
    return high


N, M = map(int, read().split())
durations = tuple(map(int, read().split()))
print(min_bd_size(M, durations))
