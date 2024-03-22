# Rest Stops

import sys
input = sys.stdin.readline

L, N, john, bessie = map(int, input().split())
v = [list(map(int, input().split())) for _ in range(N)]
v.sort(key=lambda x: -x[1])

current, res = 0, 0

for rest_point, get_taste in v:
  if rest_point < current:
    continue

  available = (rest_point - current) * (john - bessie)
  res += available * get_taste
  current = rest_point

print(res)