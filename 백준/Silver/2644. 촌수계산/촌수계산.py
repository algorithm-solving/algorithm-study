from collections import deque
from sys import stdin


def search(start, end):
    count = 0
    visited = [False for _ in range(n + 1)]
    visited[start] = True
    deq = deque([start])
    while deq:
        count += 1
        for _ in range(len(deq)):
            vertex = deq.popleft()
            for v in adj[vertex]:
                if visited[v]:
                    continue
                if v == end:
                    return count
                visited[v] = True
                deq.append(v)
    return -1


n = int(stdin.readline())
adj = [[] for _ in range(n + 1)]
v1, v2 = map(int, stdin.readline().split())
m = int(stdin.readline())
for line in stdin.read().splitlines():
    x, y = map(int, line.split())
    adj[x].append(y)
    adj[y].append(x)
print(search(v1, v2))
