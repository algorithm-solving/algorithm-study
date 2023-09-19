from sys import stdin

read = stdin.readline

N, L = map(int, read().split())
leaks = sorted(map(int, read().split()))
count = end = 0
for leak in leaks:
    if leak > end:
        end = leak + L - 1
        count += 1
print(count)
