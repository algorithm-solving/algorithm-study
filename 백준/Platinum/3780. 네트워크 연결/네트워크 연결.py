from sys import stdin

read = stdin.readline


def find(v):
    stack = []
    while (parent := parents[v]) != v:
        stack.append(v)
        v = parent
    root = v
    while stack:
        v = stack.pop()
        distances[v] += distances[parents[v]]
        parents[v] = root


def union(v1, v2):
    parents[v1] = v2
    distances[v1] = abs(v1 - v2) % 1000


results = []
T = int(read())
for _ in range(T):
    N = int(read())
    parents = list(range(N + 1))
    distances = [0 for _ in range(N + 1)]
    while True:
        cmd = read().split()
        cmd_type = cmd[0]
        if cmd_type == 'O':
            break
        i = int(cmd[1])
        if cmd_type == 'E':
            find(i)
            results.append(distances[i])
        elif cmd_type == 'I':
            j = int(cmd[2])
            union(i, j)
print('\n'.join(map(str, results)))
