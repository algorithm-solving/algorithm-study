# 카드 정렬하기

import sys
import heapq
input = sys.stdin.readline

n = int(input())
cards = []

for _ in range(n):
  num = int(input())
  heapq.heappush(cards, num)

answer = 0
while len(cards) > 1:
  a = heapq.heappop(cards)
  b = heapq.heappop(cards)
  
  answer += a + b
  heapq.heappush(cards, a + b)

print(answer)