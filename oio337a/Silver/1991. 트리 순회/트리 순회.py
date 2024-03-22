# 트리순회

import sys
input = sys.stdin.readline

n = int(input())
binary_tree = dict()

for _ in range(n):
  node, left, right = input().rstrip().split()
  binary_tree[node] = [left, right]

def preorder(node):
  if node != '.':
    print(node, end='')
    preorder(binary_tree[node][0])
    preorder(binary_tree[node][1])

def inorder(node):
  if node != '.':
    inorder(binary_tree[node][0])
    print(node, end='')
    inorder(binary_tree[node][1])

def postorder(node):
  if node != '.':
    postorder(binary_tree[node][0])
    postorder(binary_tree[node][1])
    print(node, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')