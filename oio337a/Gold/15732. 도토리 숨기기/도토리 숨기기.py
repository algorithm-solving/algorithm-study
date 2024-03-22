# 도토리 숨기기

import sys
input = sys.stdin.readline

def find_last_box(n, d):
  left, right = 1, n

  while left <= right:
    mid = (left + right) // 2
    cnt = 0

    for s, e, step in arr:
      if s > mid: continue
      if mid > e:
        cnt += (e - s) // step + 1
      else:
        cnt += (mid - s) // step + 1
      if cnt >= d:
        right = mid - 1
        answer = mid
        break
    else:
      left = mid + 1
  return answer

n, k, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

print(find_last_box(n, d))