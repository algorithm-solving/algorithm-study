from sys import stdin

read = stdin.readline

N = int(input())
durations = (tuple(map(int, input().split())) for _ in range(N))
starts, ends = map(sorted, zip(*durations))
i = count = 0
for s in starts:
    if s >= ends[i]:
        i += 1
        continue
    count += 1
print(count)
