# N번째 큰 수

import sys
import heapq
input = sys.stdin.readline

hq = []
N = int(input())
for _ in range(N):
    for i in map(int, input().split()):
        if len(hq)>=N:
            heapq.heappushpop(hq, i)
        else :
            heapq.heappush(hq, i)
print(heapq.heappop(hq))