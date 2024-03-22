from sys import stdin

read = stdin.readline

N = int(read())
durations = [tuple(map(int, read().split())) for _ in range(N)]
time = count = 0
for start, end in sorted(durations, key=lambda d: (d[1], d[0])):
    if time > start:
        continue
    count += 1
    time = end
print(count)
