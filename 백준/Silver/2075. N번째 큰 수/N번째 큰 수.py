from heapq import heappush
from heapq import heappushpop
from sys import stdin

read = stdin.readline

N = int(read())
heap = []
for _ in range(N):
    for num in map(int, read().split()):
        if len(heap) < N:
            heappush(heap, num)
        else:
            heappushpop(heap, num)
print(heap[0])
