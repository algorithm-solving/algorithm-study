import heapq
from sys import stdin

n = int(stdin.readline())
heap = []

for _ in range(n):
    num = int(stdin.readline())

    if num == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, [-num, num]) # [우선순위, 저장할 숫자]
