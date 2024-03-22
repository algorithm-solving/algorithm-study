import sys
input = sys.stdin.readline

def DFS(now,bit,cnt):
  if graph[now][0] >= cnt:
    DP[now][bit] = cnt
  for next in range(1,K+1):
    if bit&(1<<next) or graph[now][next]<cnt:
      continue
    if not DP[next][bit|(1<<next)]:
      DFS(next,bit|(1<<next),cnt+1)
    DP[now][bit] = max(DP[now][bit],DP[next][bit|(1<<next)])

def makegraph():
  newgraph = [[0]*(K+1) for i in range(K+1)]
  for i in range(K+1):
    for j in range(K+1):
      newgraph[i][j] = graph[jewel[i]][jewel[j]]
  return newgraph

N,M,K = map(int,input().split())
jewel = [0]+[int(input())-1 for i in range(K)]

graph = [[-1]*N for i in range(N)]
for i in range(M):
  x,y,w = map(int,input().split())
  graph[x-1][y-1] = graph[y-1][x-1] = w
for i in range(N):
  graph[i][i] = 100
for k in range(N):
  for i in range(N):
    for j in range(N):
      if graph[i][j] < min(graph[i][k],graph[k][j]):
        graph[i][j] = min(graph[i][k],graph[k][j])

graph = makegraph()
result = 0
DP = [[0]*(1<<(K+1)) for i in range(K+1)]
DFS(0,1,0)
print(DP[0][1])