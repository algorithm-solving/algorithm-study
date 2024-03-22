#촌수계산

import sys
from collections import deque
input = sys.stdin.readline


def bfs(node):
  que = deque()
  que.append(node)
  while que:
    node = que.popleft()
    for n in net[node]:
      if not check[n]:
        check[n] = check[node] + 1
        que.append(n)

n = int(input())
point, target = map(int, input().split())

net = [[] for _ in range(n + 1)]
for _ in range(int(input())):
  p, c = map(int, input().split())
  net[p].append(c)
  net[c].append(p)

check = [0] * (n + 1)
bfs(point)
print(check[target] if check[target] > 0 else -1)
  
  
