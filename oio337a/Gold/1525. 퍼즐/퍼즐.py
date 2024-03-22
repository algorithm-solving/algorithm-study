# 퍼즐

import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
  while que:
    now = que.popleft()

    if now == '123456789':
      return cntDict[now]
    
    pos = now.find("9")
    x = pos // 3
    y = pos % 3

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < 3 and 0 <= ny < 3:
        nPos = nx * 3 + ny

        nextNum = list(now)
        nextNum[nPos], nextNum[pos] = nextNum[pos], nextNum[nPos]
        nextNum = "".join(nextNum)

        if not cntDict.get(nextNum):
          que.append(nextNum)
          cntDict[nextNum] = cntDict[now] + 1

start = ""
for _ in range(3):
  temp = input().rstrip().replace(' ', '')
  start += temp

start = start.replace('0', '9')

que = deque()
que.append(start)

cntDict = dict()
cntDict[start] = 0

result = bfs()
print(result if result != None else "-1")