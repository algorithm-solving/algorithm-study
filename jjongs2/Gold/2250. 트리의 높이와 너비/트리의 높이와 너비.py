from sys import stdin

NIL = -1


def find_max_width(positions):
    endpoints = [(N, 1) for _ in range(N)]
    for level, col in positions:
        left, right = endpoints[level]
        endpoints[level] = min(left, col), max(right, col)
    max_level, max_width = 0, 0
    for level, (left, right) in enumerate(endpoints):
        width = right - left + 1
        if width > max_width:
            max_level, max_width = level, width
    return max_level + 1, max_width


def find_positions(node):
    positions = [None for _ in range(N)]
    level, col = -1, 1
    stack = []
    while stack or node != NIL:
        if node != NIL:
            level += 1
            stack.append((node, level))
            node = childrens[node][0]
            continue
        node, level = stack.pop()
        positions[node - 1] = level, col
        col += 1
        node = childrens[node][1]
    return positions


def find_root():
    node = 1
    while (parent := parents[node]) > 0:
        node = parent
    return node


N = int(stdin.readline())
parents = [0 for _ in range(N + 1)]
childrens = [None for _ in range(N + 1)]
for line in stdin.read().splitlines():
    node, *children = map(int, line.split())
    childrens[node] = children
    for child in children:
        if child == NIL:
            continue
        parents[child] = node
root = find_root()
node_positions = find_positions(root)
print(*find_max_width(node_positions))
