# 여행 가자

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(n):
  if graph[n] < 0:
    return n
  graph[n] = find(graph[n])
  return graph[n]

def union(x, y):
  a = find(x)
  b = find(y)
  
  if a == b:
    return
  if graph[a] > graph[b]:
    graph[b] += graph[a]
    graph[a] = b
  else:
    graph[a] += graph[b]
    graph[b] = a

n = int(input())
m = int(input())

graph = [-1] * (n + 1)
node = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
  for idx, val in enumerate(node[i]):
    if val == 1:
      union(i + 1, idx + 1)

plan = list(map(int, input().split()))
answer = find(plan[0])
for i in plan:
  if answer != find(i):
    print("NO")
    break
else:
  print("YES")