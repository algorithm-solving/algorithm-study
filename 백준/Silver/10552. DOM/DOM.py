from sys import stdin

read = stdin.readline

N, M, P = map(int, read().split())
next_channels = [0 for _ in range(M + 1)]
for _ in range(N):
    fav, hate = map(int, read().split())
    if next_channels[hate] == 0:
        next_channels[hate] = fav
count = 0
visited = [False for _ in range(M + 1)]
visited[P] = True
curr = P
while (curr := next_channels[curr]) != 0:
    if visited[curr]:
        count = -1
        break
    visited[curr] = True
    count += 1
print(count)
