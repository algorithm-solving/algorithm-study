# 문명

import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, K = map(int, input().split())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

maps = [[0] * 2001 for _ in range(2001)]
civil = [x for x in range(100_001)]
civil_dq = deque()
bfs_dq = deque()

def is_valid_coord(y, x):
  return 0 <= y < N and 0 <= x < N

def find(x):
  if civil[x] == x:
    return x
  civil[x] = find(civil[x])
  return civil[x]

def union(x, y):
  a = find(x)
  b = find(y)
  if a != b:
    civil[a] = b

def is_same_parent(a, b):
  a = find(a)
  b = find(b)
  return a == b

def union_civil():
  global K
  while civil_dq:
    y, x = civil_dq.popleft()
    bfs_dq.append((y, x))
    for k in range(4):
      ny = y + dy[k]
      nx = x + dx[k]
      if (not is_valid_coord(ny, nx)) or maps[ny][nx] == 0:
        continue
      cur_civil = maps[y][x]
      neighbor_civil = maps[ny][nx]

      if cur_civil == neighbor_civil or is_same_parent(cur_civil, neighbor_civil):
        continue
      union(cur_civil, neighbor_civil)
      K -= 1

def bfs():
  while bfs_dq:
    y, x = bfs_dq.popleft()
    for k in range(4):
      ny = y + dy[k]
      nx = x + dx[k]
      if not is_valid_coord(ny, nx) or maps[ny][nx] != 0:
        continue
      maps[ny][nx] = maps[y][x]
      civil_dq.append((ny, nx))

for i in range(K):
  y, x = map(int, input().split())
  maps[y - 1][x - 1] = i + 1
  civil_dq.append((y - 1, x - 1))

year = 0
while K > 1:
  union_civil()
  if K == 1:
    print(year)
    break
  bfs()
  year += 1




