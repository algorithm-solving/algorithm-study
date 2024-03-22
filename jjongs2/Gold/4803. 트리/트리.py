from sys import stdin

read = stdin.readline


def is_tree(start, visited):
    edge_count, v_count = 0, 0
    stack = [start]
    while stack:
        v0 = stack.pop()
        v_count += 1
        edge_count += len(adj[v0])
        for v in adj[v0]:
            if visited[v]:
                continue
            visited[v] = True
            stack.append(v)
    edge_count //= 2
    return edge_count < v_count


def count_tree(total_v_count):
    tree_count = 0
    visited = [False for _ in range(total_v_count + 1)]
    for v in range(1, total_v_count + 1):
        if visited[v]:
            continue
        visited[v] = True
        if is_tree(v, visited):
            tree_count += 1
    return tree_count


def make_result(case_index, tree_count):
    if tree_count == 0:
        return f'Case {case_index}: No trees.'
    if tree_count == 1:
        return f'Case {case_index}: There is one tree.'
    return f'Case {case_index}: A forest of {tree_count} trees.'


results = []
index = 1
while True:
    n, m = map(int, read().split())
    if n == 0:
        break
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        v1, v2 = map(int, read().split())
        adj[v1].append(v2)
        adj[v2].append(v1)
    T = count_tree(n)
    result = make_result(index, T)
    results.append(result)
    index += 1
print('\n'.join(results))
