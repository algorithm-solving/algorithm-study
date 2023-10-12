from sys import stdin

read = stdin.readline

K, N = map(int, read().split())
lengths = [int(read()) for _ in range(K)]
low, high = 1, max(lengths)
while low <= high:
    mid = (low + high) // 2
    count = sum(length // mid for length in lengths)
    if count < N:
        high = mid - 1
    else:
        low = mid + 1
print(high)
