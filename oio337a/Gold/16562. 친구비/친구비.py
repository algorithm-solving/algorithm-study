# https://www.acmicpc.net/problem/16562
# 친구비
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
costs = [0] + list(map(int, input().split()))
parent = [i for i in range(n + 1)]

def find(target):
    if target == parent[target]:
        return target
    parent[target] = find(parent[target])
    return parent[target]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        if costs[a] <= costs[b]:
            parent[b] = a
        else:
            parent[a] = b
for i in range(m):
    v, w = map(int, input().split())
    union(v, w)
ans = 0
for idx, root in enumerate(parent):
    if idx == root:
      ans += costs[idx]
if ans <= k:
    print(ans)
else:
    print("Oh no")