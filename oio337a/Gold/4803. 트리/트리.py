# 트리

import sys
from collections import deque
input = sys.stdin.readline

def findCycle(start):
  isCycle = False
  q = deque()
  q.append(start)

  while q:
    node = q.popleft()
    if visited[node]:
      isCycle = True
    
    visited[node] = 1
    
    for next_node in graph[node]:
      if visited[next_node] == 0:
        q.append(next_node)
  return isCycle

case = 1
while True:
  n, m = map(int, input().split())
  if n == 0 and m == 0:
    break
  graph = [[] for _ in range(n + 1)]
  visited = [0] * (n + 1)
  count = 0
  for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
  
  for node in range(1, n + 1):
    if visited[node] == 0:
      if not findCycle(node):
        count += 1

  if not count:
      print(f'Case {case}: No trees.')
  elif count == 1:
      print(f'Case {case}: There is one tree.')
  else:
      print(f'Case {case}: A forest of {count} trees.')
  
  case += 1