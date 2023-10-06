# 용돈 관리

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

left, right, top = min(arr), sum(arr), max(arr)
answer = 0

while left <= right:
  mid = (left + right) // 2

  count, temp = 1, mid
  for i in range(n):
    if temp < arr[i]:
      count += 1
      temp = mid
    temp -= arr[i]
  if count > m or mid < top:
    left = mid + 1
  else:
    right = mid - 1
    answer = mid
print(answer)