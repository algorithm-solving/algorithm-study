from sys import stdin

read = stdin.readline

N, M = map(int, read().split())
heights = list(map(int, read().split()))
low, high = 0, max(heights)
while high - low > 1:
    mid = (low + high) // 2
    cut = 0
    for h in heights:
        cut += max(0, h - mid)
    if cut < M:
        high = mid
    else:
        low = mid
print(low)
