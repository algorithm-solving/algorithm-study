from sys import stdin

read = stdin.readline

PRIORITIES = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
}

postfix = ''
stack = []
infix = read().strip()
for char in infix:
    if priority := PRIORITIES.get(char):
        while stack and priority <= PRIORITIES.get(stack[-1], 0):
            postfix += stack.pop()
        stack.append(char)
    elif char == '(':
        stack.append(char)
    elif char == ')':
        while (popped := stack.pop()) != '(':
            postfix += popped
    else:
        postfix += char
while stack:
    postfix += stack.pop()
print(postfix)
