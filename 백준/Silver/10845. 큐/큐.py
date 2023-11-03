from sys import stdin

read = stdin.readline

results = []
queue = []
N = int(read())
for _ in range(N):
    cmd = read().split()
    cmd_type = cmd[0]
    try:
        if cmd_type == 'push':
            queue.append(cmd[1])
        elif cmd_type == 'pop':
            results.append(queue.pop(0))
        elif cmd_type == 'size':
            results.append(str(len(queue)))
        elif cmd_type == 'empty':
            results.append('1' if not queue else '0')
        elif cmd_type == 'front':
            results.append(queue[0])
        elif cmd_type == 'back':
            results.append(queue[-1])
    except IndexError:
        results.append('-1')
print('\n'.join(results))
