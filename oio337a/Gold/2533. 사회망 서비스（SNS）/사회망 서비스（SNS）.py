# 사회망 서비스

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n - 1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

dp = [[0, 0] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
def dfs(s):
  visited[s] = 1
  if len(graph[s]) == 0:
    dp[s][1] = 1
    dp[s][0] = 0
  else:
    for i in graph[s]:
      if visited[i] == 0:
        dfs(i)
        dp[s][1] += min(dp[i][0], dp[i][1])
        dp[s][0] += dp[i][1]
    dp[s][1] += 1
dfs(1)
print(min(dp[1][0], dp[1][1]))