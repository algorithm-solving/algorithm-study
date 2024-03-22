# 소수의 곱

import sys
import heapq
input = sys.stdin.readline

k, n = map(int, input().split())
nums = list(map(int, input().split()))
heap = []

for d in nums:
  heapq.heappush(heap, d)

for _ in range(n):
  num = heapq.heappop(heap)
  for i in range(k):
    temp = num * nums[i]
    heapq.heappush(heap, temp)

    if num % nums[i] == 0:
      break

print(num)