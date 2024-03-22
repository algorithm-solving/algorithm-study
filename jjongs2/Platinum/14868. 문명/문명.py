from array import array
from collections import deque
from sys import stdin


def find(v):
    if parents[v] < 0:
        return v
    parents[v] = find(parents[v])
    return parents[v]


def is_valid_index(v, v0):
    if not (0 <= v < max_area):
        return False
    if v // N != v0 // N and v % N != v0 % N:
        return False
    return True


def union(v1, v2):
    p1, p2 = find(v1), find(v2)
    if p1 != p2:
        parents[p1] += parents[p2]
        parents[p2] = p1
    return parents[p1]


def search(deq):
    depth = 0
    area = -K
    while deq:
        for v0 in deq:
            p0 = parents[v0]
            for dv in deltas:
                v = v0 + dv
                if not is_valid_index(v, v0):
                    continue
                p = parents[v]
                if p == -inf:
                    continue
                if p == p0 >= 0:
                    continue
                if union(v0, v) == area:
                    return depth
        depth += 1
        for _ in range(len(deq)):
            v0 = deq.popleft()
            for dv in deltas:
                v = v0 + dv
                if not is_valid_index(v, v0):
                    continue
                if parents[v] > -inf:
                    continue
                parents[v] = -1
                area -= 1
                if union(v0, v) == area:
                    return depth
                deq.append(v)


N, K = map(int, stdin.readline().split())
deltas = (-N, -1, 1, N)
max_area = N * N
inf = max_area + 1
parents = array('i', [-inf for _ in range(max_area)])
cradles = deque([])
for line in stdin.read().splitlines():
    x, y = map(int, line.split())
    index = N * (y - 1) + x - 1
    parents[index] = -1
    cradles.append(index)
print(search(cradles))
