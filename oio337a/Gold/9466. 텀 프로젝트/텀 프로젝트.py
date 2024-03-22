# 텀 프로젝트

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x):
  global result
  visited[x] = True
  cycle.append(x) #사이클을 이루는 팀을 확인하기 위해 추가
  number = numbers[x]

  if visited[number]: #방문가능한 곳이 있는지
    if number in cycle: #사이클 가능 여부 확인
      result += cycle[cycle.index(number):] #사이클 되는 구간 부터만 팀을 이룸
    return
  else:
    dfs(number)

for _ in range(int(input())):
  N = int(input())
  numbers = [0] + list(map(int, input().split()))
  visited = [True] + [False] * N #방문 여부
  result = []

  for i in range(1, N + 1):
    if not visited[i]:
      cycle = []
      dfs(i)
  
  print(N - len(result))
  
  
