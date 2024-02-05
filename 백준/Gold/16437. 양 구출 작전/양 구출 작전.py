from collections import deque
from sys import stdin

ROOT = 1

N = int(stdin.readline())
childrens = [[] for _ in range(N + 1)]
parents = [0 for _ in range(N + 1)]
sheeps = [0 for _ in range(N + 1)]
for node, line in enumerate(stdin.read().splitlines(), start=2):
    t, a, p = line.split()
    a, p = int(a), int(p)
    sheeps[node] = a if t == 'S' else -a
    parents[node] = p
    childrens[p].append(node)
stack = []
deq = deque([ROOT])
while deq:
    node = deq.popleft()
    stack.append(node)
    for child in childrens[node]:
        deq.append(child)
while stack:
    node = stack.pop()
    sheeps[parents[node]] += max(0, sheeps[node])
print(sheeps[ROOT])
