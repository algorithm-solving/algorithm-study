from sys import stdin

read = stdin.readline

N = int(read())
k = int(read())
low, high = 1, k
while low <= high:
    mid = (low + high) // 2
    count = 0
    for i in range(1, N + 1):
        count += min(N, mid // i)
    if count < k:
        low = mid + 1
    else:
        high = mid - 1
print(low)
