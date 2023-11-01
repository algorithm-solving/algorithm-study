# 스택

import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
  command = list(input().split())
  if command[0] == 'push':
    stack.append(command[1])
  elif command[0] == 'pop':
    print(-1) if len(stack) == 0 else print(stack.pop())
  elif command[0] == 'size':
    print(len(stack))
  elif command[0] == 'empty':
    print(1) if len(stack) == 0 else print(0)
  elif command[0] == 'top':
    print(-1) if len(stack) == 0 else print(stack[-1])