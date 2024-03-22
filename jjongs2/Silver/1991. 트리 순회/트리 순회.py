from sys import stdin

ROOT = 'A'


def preorder(node, visited):
    if node == '.':
        return
    visited.append(node)
    left, right = children[node]
    preorder(left, visited)
    preorder(right, visited)


def inorder(node, visited):
    if node == '.':
        return
    left, right = children[node]
    inorder(left, visited)
    visited.append(node)
    inorder(right, visited)


def postorder(node, visited):
    if node == '.':
        return
    left, right = children[node]
    postorder(left, visited)
    postorder(right, visited)
    visited.append(node)


_ = stdin.readline()
children = dict()
for line in stdin.read().splitlines():
    node, left, right = line.split()
    children[node] = left, right
results = [[], [], []]
preorder(ROOT, results[0])
inorder(ROOT, results[1])
postorder(ROOT, results[2])
print('\n'.join(''.join(result) for result in results))
