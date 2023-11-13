# 스타트링크

import sys
from collections import deque
input = sys.stdin.readline

''' 시간 초과 '''
max_f, position, target, up, down = map(int, input().split())
que = deque()
que.append((position, 0))
visit = [0] * (max_f + 1)
visit[position] = 1

if (target < position and down == 0) or (
  target > position and up == 0
):
  que.pop()

while que:
  now, cnt = que.popleft()
  if now == target:
    print(cnt)
    break
  if now + up <= max_f and not visit[now + up]:
    que.append((now + up, cnt + 1))
    visit[now + up] = 1
  if 0 < now - down and not visit[now - down]:
    que.append((now - down, cnt + 1))
    visit[now - down] = 1
else:
  print("use the stairs")