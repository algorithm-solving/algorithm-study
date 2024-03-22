# 후위 표기식 2

import sys
input = sys.stdin.readline

n = int(input())
str = input().rstrip()
nums = [int(input()) for _ in range(n)]
alpha = [chr(ord('A') + i) for i in range(n)]
mapping = {}

for i in range(n):
  mapping[alpha[i]] = nums[i]
stack = []

for token in str:
  if token.isalpha():
    stack.append(mapping[token])
  else:
    num2 = stack.pop()
    num1 = stack.pop()
    if token == '*':
      stack.append(num1 * num2)    
    elif token == '/':
      stack.append(num1 / num2)    
    elif token == '+':
      stack.append(num1 + num2)    
    elif token == '-':
      stack.append(num1 - num2)

print('%.2f'%stack[0])
