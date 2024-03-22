# 친구 네트워크

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x):
  if p[x] != x:
    p[x] = find(p[x])
  return p[x]

def union(x, y):
  a = find(x)
  b = find(y)

  if a != b:
    p[b] = a
    num[a] += num[b]
  print(num[a])

t = int(input())
for _ in range(t):
  f = int(input())
  p, num = {}, {}
  for _ in range(f):
    a, b = map(str, input().split())
    if a not in p:
      p[a] = a
      num[a] = 1
    if b not in p:
      p[b] = b
      num[b] = 1
    union(a, b)