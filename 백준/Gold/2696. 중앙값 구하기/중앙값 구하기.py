# 중앙값 구하기

import sys
import heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  # 입력 받기
  m = int(input())
  data = []
  if m % 10 == 0:
    for _ in range(m//10):
      data.extend(list(map(int, input().split())))
  else:
    for _ in range(m//10+1):
      data.extend(list(map(int, input().split())))
  
  # 해결
  s_heap = []
  b_heap = []
  middle = data[0]
  res = [middle]
  for i, val in enumerate(data[1:], 1):
    if val > middle:
      heapq.heappush(b_heap, val)
    else:
      heapq.heappush(s_heap, (-val, val))
    
    if i % 2 == 0:
      if len(s_heap) < len(b_heap):
        heapq.heappush(s_heap, (-middle, middle))
        middle = heapq.heappop(b_heap)
      elif len(s_heap) > len(b_heap):
        heapq.heappush(b_heap, middle)
        middle = heapq.heappop(s_heap)[1]
      res.append(middle)
  # 정답 출력
  print(len(res))
  for i in range(len(res)):
    if i != 0 and (i+1) % 10 == 1:
      print()
    print(res[i], end=' ')
  print()