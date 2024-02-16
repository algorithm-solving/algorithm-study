# 절댓값 힙

import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
  num = int(input())
  if not num:
    if heap:
      print(heapq.heappop(heap)[1])
    else:
      print(0)
  else:
    heapq.heappush(heap, [abs(num), num])