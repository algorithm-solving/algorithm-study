from sys import stdin

read = stdin.readline

N = int(read())
sqrt = int(N ** 0.5)
counts = [i for i in range(N + 1)]
for n in range(2, sqrt + 1):
    sq_num = n * n
    for i in range(sq_num, N + 1):
        counts[i] = min(counts[i], counts[i - sq_num] + 1)
print(counts[N])
