from sys import stdin

read = stdin.readline


def find_postorder(start, end, postorder):
    if start == end:
        return
    base_node = next(preorder)
    if start == end - 1:
        postorder.append(inorder[start])
        return
    base_index = inorder.index(base_node, start, end)
    find_postorder(start, base_index, postorder)
    find_postorder(base_index + 1, end, postorder)
    postorder.append(base_node)


results = []
T = int(read())
for _ in range(T):
    n = int(read())
    preorder = map(int, read().split())
    inorder = tuple(map(int, read().split()))
    postorder = []
    find_postorder(0, n, postorder)
    results.append(postorder)
print('\n'.join(' '.join(map(str, result)) for result in results))
