from sys import stdin

read = stdin.readline

N, K, D = map(int, read().split())
rules = [tuple(map(int, read().split())) for _ in range(K)]
low, high = 1, N
while high - low > 1:
    mid = (low + high) // 2
    count = 0
    for A, B, C in rules:
        if mid >= A:
            count += (min(B, mid) - A) // C + 1
    if count < D:
        low = mid
    else:
        high = mid
print(high)
