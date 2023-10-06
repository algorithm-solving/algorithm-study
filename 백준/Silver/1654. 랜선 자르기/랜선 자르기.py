# 랜선 자르기

import sys
input = sys.stdin.readline

k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]

left, right = 1, max(arr)
while left <= right:
  mid = (left + right) // 2
  
  count = 0
  for i in range(k):
    count += arr[i] // mid
    
  if count >= n:
    left = mid + 1
  else:
    right = mid - 1

print(right)