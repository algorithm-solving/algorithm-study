# 트리의 부모 찾기
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [0] * (n + 1)

def find(s):
  for i in graph[s]:
    if visited[i] == 0:
      visited[i] = s
      find(i)

find(1)

for x in range(2, n + 1):
  print(visited[x])
