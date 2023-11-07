from sys import stdin

read = stdin.readline

N, M = map(int, read().split())
components = [{i} for i in range(1, N + 1)]
for _ in range(M):
    u, v = map(int, read().split())
    for i, c in enumerate(components):
        if u in c:
            u_i = i
        if v in c:
            v_i = i
    if u_i == v_i:
        continue
    components[u_i] |= components[v_i]
    components.pop(v_i)
print(len(components))
