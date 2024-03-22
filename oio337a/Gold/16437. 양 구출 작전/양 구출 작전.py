# 양 구출 작전
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
arr = [[0,0], [0,0]]

for i in range(2, n + 1):
  type, num, node = input().split()
  arr.append([type, int(num)])
  graph[int(node)].append(i)

def dfs(v):
  res = 0
  for i in graph[v]:
    res += dfs(i)
  if arr[v][0] == 'S':
    res += arr[v][1]
  else:
    res -= arr[v][1]
    if res < 0:
      res = 0
  return res
print(dfs(1))

