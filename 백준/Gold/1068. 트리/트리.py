from sys import stdin

read = stdin.readline


def count_leaf(node):
    if not (children := childrens[node]):
        return 1
    count = 0
    for child in children:
        if child == target:
            continue
        count += count_leaf(child)
    return count


N = int(read())
parents = map(int, read().split())
target = int(read())
childrens = [[] for _ in range(N)]
for node, parent in enumerate(parents):
    if parent == -1:
        if node == target:
            leaf_count = 0
            break
        root = node
    elif node != target:
        childrens[parent].append(node)
else:
    leaf_count = count_leaf(root)
print(leaf_count)
