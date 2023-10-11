# 회전하는 큐

'''
1 2 3 4 5 6 7 8 9 10
  o     o       o
2 3 4 . . . 10 1
1
10
9 10
1
3
4
5
'''

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
position = list(map(int, input().split()))
que = deque([i for i in range(1, n + 1)])

count = 0

for i in position:
  while 1:
    if que[0] == i:
      que.popleft()
      break
    else:
      if que.index(i) < len(que)/2:
        while que[0] != i:
          que.rotate(-1)
          count += 1
      else:
        while que[0] != i:
          que.rotate(1)
          count += 1
print(count)
