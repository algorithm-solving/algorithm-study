from collections import deque
from sys import stdin


def find(v):
    if parents[v] == v:
        return v
    parents[v] = find(parents[v])
    return parents[v]


def is_valid_index(v, v0):
    if not (0 <= v < max_area):
        return False
    if v // C != v0 // C and v % C != v0 % C:
        return False
    return True


def spread_waters(deq):
    for _ in range(len(deq)):
        v0 = deq.popleft()
        p0 = parents[v0]
        for dv in deltas:
            v = v0 + dv
            if not is_valid_index(v, v0):
                continue
            if parents[v] > -1:
                continue
            parents[v] = p0
            deq.append(v)


def union(v1, v2):
    p1, p2 = find(v1), find(v2)
    parents[p2] = p1


def union_waters(deq):
    for v0 in deq:
        p0 = parents[v0]
        for dv in deltas:
            v = v0 + dv
            if not is_valid_index(v, v0):
                continue
            if parents[v] in (-1, p0):
                continue
            union(v0, v)


def search(deq):
    depth = 0
    swan1, swan2 = swans
    while deq:
        union_waters(deq)
        if find(swan1) == find(swan2):
            return depth
        depth += 1
        spread_waters(deq)


R, C = map(int, stdin.readline().split())
deltas = (-C, -1, 1, C)
max_area = R * C
parents = [-1 for _ in range(max_area)]
swans, waters = [], deque([])
lake = stdin.read().replace('\n', '')
for i, obj in enumerate(lake):
    if obj == 'X':
        continue
    parents[i] = i
    waters.append(i)
    if obj == 'L':
        swans.append(i)
print(search(waters))
