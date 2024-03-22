# 큐

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
que = deque()

for _ in range(n):
  command = list(input().split())
  if command[0] == 'push':
    que.append(command[1])
  elif command[0] == 'pop':
    print(que.popleft()) if que else print(-1)
  elif command[0] == 'size':
    print(len(que))
  elif command[0] == 'empty':
    print(0) if que else print(1)
  elif command[0] == 'front':
    print(que[0]) if que else print(-1)
  elif command[0] == 'back':
    print(que[-1]) if que else print(-1)