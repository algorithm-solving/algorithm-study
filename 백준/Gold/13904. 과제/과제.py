from heapq import heappop
from heapq import heappush
from sys import stdin

read = stdin.readline

N = int(read())
assignments = [tuple(map(int, read().split())) for _ in range(N)]
scores = []
for d, w in sorted(assignments):
    heappush(scores, w)
    if d < len(scores):
        heappop(scores)
print(sum(scores))
