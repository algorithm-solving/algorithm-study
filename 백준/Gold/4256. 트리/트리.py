# 트리

import sys
input = sys.stdin.readline

def solve(root, s, e):
  for i in range(s, e):
    if inorder[i] == preorder[root]:
      solve(root + 1, s, i)
      solve(root + i + 1 - s, i + 1, e)

      print(preorder[root], end=" ")

t = int(input())
for _ in range(t):
  n = int(input())
  preorder = list(map(int, input().split()))
  inorder = list(map(int, input().split()))
  solve(0, 0, n)
  print()