# 카드 2

import sys
from collections import deque
input = sys.stdin.readline

# n = int(input())
# arr = deque(i + 1 for i in range(n))

# while len(arr) != 1:
#   arr.popleft()
#   arr.append(arr.popleft())

# print(arr[0])


''' 버전 2 '''

n = int(input())
arr = deque(i + 1 for i in range(n))
result = 0

while True:
  result = arr.popleft()
  try:
    arr.append(arr.popleft())
  except:
    break
print(result)



