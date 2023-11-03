from collections import deque
from sys import stdin

read = stdin.readline

results = []
deq = deque()
N = int(read())
for _ in range(N):
    cmd = read().split()
    cmd_type = cmd[0]
    try:
        if cmd_type == 'push_front':
            deq.appendleft(cmd[1])
        elif cmd_type == 'push_back':
            deq.append(cmd[1])
        elif cmd_type == 'pop_front':
            results.append(deq.popleft())
        elif cmd_type == 'pop_back':
            results.append(deq.pop())
        elif cmd_type == 'size':
            results.append(str(len(deq)))
        elif cmd_type == 'empty':
            results.append('1' if not deq else '0')
        elif cmd_type == 'front':
            results.append(deq[0])
        elif cmd_type == 'back':
            results.append(deq[-1])
    except IndexError:
        results.append('-1')
print('\n'.join(results))
