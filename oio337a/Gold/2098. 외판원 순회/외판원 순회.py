# 외판원 순회
# 비트마스킹 + DP + DFS

import sys
input = sys.stdin.readline

n = int(input())
INF = int(1e9)
dp = [[-1] * (1 << n) for _ in range(n)]

def dfs(x, visited):
  if visited == (1 << n) - 1: # 모든 도시를 방문했다면
    if graph[x][0]: # 출발점으로 가는 경로가 있을 때
      return graph[x][0]
    else:
      return INF
  
  if dp[x][visited] != -1: # 이미 최소비용이 계산되어 있다면
    return dp[x][visited]
  temp = INF
  for i in range(1, n): # 모든 도시를 탐방
    if not graph[x][i]: # 가는 경로가 업을 때
      continue
    if visited & (1 << i): # 이미 방문한 도시라면
      continue
    
    temp = min(temp, dfs(i, visited | (1 << i)) + graph[x][i])
  dp[x][visited] = temp
  return dp[x][visited]

graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))

print(dfs(0, 1))


'''
뒤에서 부터 생각하면 좀 더 이해하기 쉬울 것이다.

dp[next][nextvisit]이 next도시에서 남은 도시를 거쳐 시작점으로 돌아가는 최소비용이기 때문에

dp[cur][visit]은 dp[next][nextvisit]보다 graph[cur][next]만큼의 비용이 더 들 것이다.

즉, 다음 지점의 dp보다 다음 지점으로 가는데에 드는 비용만큼 더 들게 되는 것이다.

 

예를 들어, dp[0][0011(2)] = dp[0][3]은 현재 0번 도시이며, 0, 1번 도시를 방문하였고, 2, 3을 방문한 후 다시 시작점으로 돌아갈 때의 최소 비용이며

dp[2][0111(2)] = dp[2][7]은 현재 2번 도시이며 0,1,2 번 도시를 방문하였으며, 3을 방문한 후 다시 시작점으로 돌아갈 때의 최소비용이다.

즉, dp[0][0011] = dp[2][0111] + graph[0][2]이 되는 것이다.

 

이를 점화식으로 나타내면 다음과 같다.

dp[cur][visited] = min(dp[cur][visited], dp[next][visited | (1 << next)] + graph[cur][next])
'''