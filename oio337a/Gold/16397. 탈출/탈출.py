# 탈출

import sys
from collections import deque
input = sys.stdin.readline

MAX = 100_000

N, T, G = map(int, input().split())
que = deque()
que.append((N, 0))
visit = [0] * MAX

while que:
  now, cnt = que.popleft()
  if visit[now] != 0:
    continue
  visit[now] = 1
  if now == G:
    print(cnt)
    break
  if cnt + 1 <= T:
    if now * 2 < MAX:
      temp = list(str(now * 2))
      temp[0] = str(int(temp[0]) - 1) if int(temp[0]) - 1 >= 0 else '0'
      num = int(''.join(temp))
      que.append((num, cnt + 1))
    if now + 1 < MAX:
      que.append((now + 1, cnt + 1))
else:
  print('ANG')