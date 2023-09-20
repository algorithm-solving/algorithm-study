from sys import stdin

read = stdin.readline

N = int(read())
K = int(read())
sensors = sorted(map(int, read().split()))
distances = sorted(sensors[i] - sensors[i - 1] for i in range(1, N))
print(sum(distances[:N - K]))
