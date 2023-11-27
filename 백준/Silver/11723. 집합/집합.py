from sys import stdin
from sys import stdout

BUF_SIZE = 512
MAX = 20

results = []
S = 0
M = int(stdin.readline())
for _ in range(M):
    cmd = stdin.readline().split()
    cmd_type = cmd[0]
    if len(cmd) == 2:
        mask = 1 << int(cmd[1])
    if cmd_type == 'add':
        S |= mask
    elif cmd_type == 'remove':
        S &= ~mask
    elif cmd_type == 'check':
        results.append('1\n' if S & mask != 0 else '0\n')
        if len(results) < BUF_SIZE:
            continue
        stdout.write(''.join(results))
        results = []
    elif cmd_type == 'toggle':
        S ^= mask
    elif cmd_type == 'all':
        S = (1 << MAX + 1) - 1
    elif cmd_type == 'empty':
        S = 0
stdout.write(''.join(results))
