from sys import stdin

read = stdin.readline

N = int(read())
count = 1
prefix_sum = 1
for _ in range(N - 2):
    count, prefix_sum = prefix_sum + 1, prefix_sum + count
print(count)
