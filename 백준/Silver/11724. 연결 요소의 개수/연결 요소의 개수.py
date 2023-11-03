# 연결 요소의 개수
# https://www.acmicpc.net/problem/11724

'''
 dfs 와 연결 리스트 활용 기본 문제
'''
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
node = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
cnt = 0

def dfs(v):
    visited[v] = True
    for i in node[v]:
        if not visited[i]:
            dfs(i)

for _ in range(m):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        cnt += 1
print(cnt)
