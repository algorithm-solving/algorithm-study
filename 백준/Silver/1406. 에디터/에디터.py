from sys import stdin

read = stdin.readline

left = list(read().strip())
right = []
M = int(read())
for _ in range(M):
    cmd = read().strip()
    cmd_type = cmd[0]
    if cmd_type == 'L' and left:
        right.append(left.pop())
    elif cmd_type == 'D' and right:
        left.append(right.pop())
    elif cmd_type == 'B' and left:
        left.pop()
    elif cmd_type == 'P':
        left.append(cmd[-1])
left.extend(reversed(right))
print(''.join(left))
