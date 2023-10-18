from sys import stdin

read = stdin.readline

N = int(read())
postfix = read().strip()
values = {chr(ord('A') + i): int(read()) for i in range(N)}
operators = set('+-*/')
operands = []
for char in postfix:
    if char not in operators:
        operands.append(values[char])
        continue
    right = operands.pop()
    left = operands.pop()
    if char == '+':
        left += right
    elif char == '-':
        left -= right
    elif char == '*':
        left *= right
    elif char == '/':
        left /= right
    operands.append(left)
print(f'{operands.pop():.2f}')
