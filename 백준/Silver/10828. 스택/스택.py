from sys import stdin

read = stdin.readline

N = int(read())
stack = []
results = []
for _ in range(N):
    cmd = read().split()
    cmd_type = cmd[0]
    if cmd_type == 'push':
        stack.append(cmd[1])
    elif cmd_type == 'pop':
        results.append(stack.pop() if stack else '-1')
    elif cmd_type == 'size':
        results.append(str(len(stack)))
    elif cmd_type == 'empty':
        results.append('1' if not stack else '0')
    elif cmd_type == 'top':
        results.append(stack[-1] if stack else '-1')
print('\n'.join(results))
