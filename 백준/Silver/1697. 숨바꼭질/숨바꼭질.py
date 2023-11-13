# 숨바꼭질

import sys
from collections import deque
input = sys.stdin.readline
MAX_POSITION = 100000

position, target = map(int, input().split())
que = deque()
que.append((position, 0))
visit = [0] * (MAX_POSITION + 1)
visit[position] = 1

while que:
  now, cnt = que.popleft()
  if now == target:
    print(cnt)
    break
  if now * 2 <= MAX_POSITION and not visit[now * 2]:
    visit[now * 2] = 1
    que.append((now * 2, cnt + 1))
  if now + 1 <= MAX_POSITION and not visit[now + 1]:
    visit[now + 1] = 1
    que.append((now + 1, cnt + 1))
  if now - 1 >= 0 and not visit[now - 1]:
    visit[now - 1] = 1
    que.append((now - 1, cnt + 1))
